from billing.forms import CreatePackageForm
from billing.models import Package, Payment
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView


class PackageListPage(ListView):
    template_name = "package_list.html"
    model = Package
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(PackageListPage, self).get_context_data(**kwargs)
        context['create_package_form'] = CreatePackageForm()
        return context


def remove_package(request, pk):
    package = get_object_or_404(Package, pk=pk)
    package.delete()
    return HttpResponseRedirect('/package_list.html')

def create_package(request):
    f = CreatePackageForm(request.POST)
    f.save()

    return HttpResponseRedirect('/package_list.html')

def add_package_to_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    package = get_object_or_404(Package, pk=request.POST["selected_package"])
    user.userprofile.packages.add(package)
    return HttpResponseRedirect(reverse("user_details", kwargs={'pk': user_id}))

class PaymentListPage(ListView):
    template_name = "payments.html"
    model = Payment
    paginate_by = 20

def remove_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    payment.delete()
    return HttpResponseRedirect('/payments.html')

def create_payment(request):
    # TODO
    # f = CreatePackageForm(request.POST)
    # f.save()
    return HttpResponseRedirect('/payments.html')