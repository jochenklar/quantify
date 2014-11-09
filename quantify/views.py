from csv import writer as csv_writer
from csv import QUOTE_NONNUMERIC
from datetime import date as datetime_date
from datetime import timedelta as datetime_timedelta

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils.dateparse import parse_date
from django.contrib.auth import authenticate as auth_authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from forms import LoginForm,EntryForm
from data.models import Entry,Group,Field,Record

def index(request):
    return HttpResponseRedirect('/form/')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            values = form.cleaned_data
            user = auth_authenticate(username=values['username'], password=values['password'])
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect('/')
    else:
        form = LoginForm()

    return render(request,'login.html',{'form': form})

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')

@login_required
def form(request, date=None):
    if request.user.is_authenticated():
        # get the date
        if date == None:
            date = datetime_date.today()
        else:
            date = parse_date(date)

        # get the entry
        try:
            entry = Entry.objects.filter(user=request.user).get(date=date)
        except Entry.DoesNotExist:
            entry = Entry(user=request.user,date=date)
            entry.save()

        if request.method == 'POST':
            # construct the form
            form = EntryForm(request.POST,groups=Group.objects.filter(user=request.user))

            if form.is_valid():
                values = form.cleaned_data

                for key in values:
                    field_id = key.split('_')[1]
                    value = values[key]

                    field = Field.objects.get(id=field_id)

                    record = Record.objects.filter(entry=entry).get(field=field)
                    record.value = value
                    record.save()
            else:
                print form.errors

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:

            fieldsets = []
            for group in Group.objects.filter(user=request.user):
                fieldset = {
                    'name': group.name,
                    'elements': []
                }

                for field in group.fields.all():
                    try:
                        record = field.records.get(entry=entry)
                    except Record.DoesNotExist:
                        record = Record(entry=entry,field=field)
                        record.save()

                    fieldset['elements'].append({
                        'field': field,
                        'record': record
                    })

                fieldsets.append(fieldset)

            return render(request,'form.html', {
                'fieldsets': fieldsets,
                'yesterday': date - datetime_timedelta(1),
                'today': date,
                'tomorrow': date + datetime_timedelta(1),
                'auth': True,
                'user': request.user
            })
    else:
        return HttpResponseRedirect('/login/')

@login_required
def csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="quantify.csv"'

    writer = csv_writer(response,delimiter=',',quotechar='"',quoting=QUOTE_NONNUMERIC)

    cols = ['Date']
    for field in Field.objects.all():
        cols.append(field.name)
    writer.writerow(cols)

    for entry in Entry.objects.all():
        row = [entry.date]
        for col in cols[1:]:
            try:
                row.append(entry.records.get(field__name=col).value)
            except Record.DoesNotExist:
                row.append('')
        writer.writerow(row)

    return response
