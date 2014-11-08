from django.forms import Form,CharField,TextInput,PasswordInput

class LoginForm(Form):
    username = CharField(widget=TextInput(attrs={'class':'form-control'}))
    password = CharField(widget=PasswordInput(attrs={'class':'form-control'}))

class EntryForm(Form):

    def __init__(self, *args, **kwargs):
        self.groups = kwargs.pop('groups')
        super(EntryForm, self).__init__(*args, **kwargs)

        for group in self.groups:
            for field in group.fields.all():

                form_field = CharField(required=False)

                self.fields['field_%s' % field.id] = form_field
