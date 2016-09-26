from billing.models import Package
from django.forms import Form, ModelForm


class CreatePackageForm(ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'field2', 'field3']