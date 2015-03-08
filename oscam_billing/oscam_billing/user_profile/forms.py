from crispy_forms.bootstrap import AppendedText
from crispy_forms.layout import Layout, Fieldset, HTML, Field, ButtonHolder, Submit
from django.contrib.auth.models import User
from django.forms import Form
from crispy_forms.helper import FormHelper
from django import forms

def get_dealer_list():
    users = User.objects.filter(is_staff=True)
    result = [(0, '-')]
    for user in users:
        result.append((user.id, user.username))
    return result


class CreateUserForm(Form):

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['select_dealer'] = forms.ChoiceField(choices=get_dealer_list())
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                'user_role',
                'username',
                'password',
                'email',
                AppendedText('comission', '$', active=True),
                'select_dealer',
                'notes'
            ),
            ButtonHolder(
                Submit('submit', 'Create', css_class='button white')
            )
        )

    user_role = forms.ChoiceField(
        label = 'Select user role',
        choices = (('dealer', "Dealer"), ('user', "User")),
        initial = '0',
        required = True,
    )

    username = forms.CharField(label = "User name", max_length = 80, required = True, )
    email = forms.EmailField(label = "Email", max_length = 80, required = False, )
    password = forms.CharField(label = "Password", max_length = 80, widget=forms.PasswordInput)
    comission = forms.IntegerField(label = "Comission", required = False,)
    notes = forms.CharField(label = "Notes", required = False, widget=forms.Textarea(attrs={'rows': 2}) )