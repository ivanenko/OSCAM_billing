from billing.models import Package
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, resolve_url, get_object_or_404
from django.views.generic import TemplateView, RedirectView, ListView, DetailView
from user_profile.models import UserProfile


def activate_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect('/user_list.html')


def deactivate_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect('/user_list.html')


def remove_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    try:
        if user.userprofile:
            profile = user.userprofile
            profile.delete()
    except :
        pass

    user.delete()
    return HttpResponseRedirect('/user_list.html')


class HomeRedirectPageView(RedirectView):

    def dispatch(self, request, *args, **kwargs):
        self.url = reverse("login")

        user = request.user

        if user.is_superuser:
            self.url = "superuser_index.html"
        elif user.is_staff:
            self.url = "dealer_index.html"

        return super(HomeRedirectPageView, self).dispatch(request, *args, **kwargs)


class SuperuserIndexPage(TemplateView):
    template_name = "superuser_index.html"


class DealerIndexPage(TemplateView):
    template_name = "dealer_index.html"


class UserProfilePage(TemplateView):
    template_name = "profile.html"


class CreateUserPage(TemplateView):
    template_name = "create_user.html"

    def get_context_data(self, **kwargs):
        context = super(CreateUserPage, self).get_context_data(**kwargs)
        context['user_form'] = CreateUserForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data['username'])
            user.set_password(form.cleaned_data['password'])
            user.is_staff = ( form.cleaned_data['user_role'] == 'dealer' )
            user.is_active = True
            user.save()

            user_profile = UserProfile()
            user_profile.user = user
            user_profile.notes = form.cleaned_data['notes']
            user_profile.comission = form.cleaned_data['comission']
            if not user.is_staff:
                dealer = User.objects.get(pk=form.cleaned_data['select_dealer'])
                user_profile.dealer = dealer
                user_profile.open_password = form.cleaned_data['password']
            user_profile.save()

        return HttpResponseRedirect('/user_list.html')

class UserListPage(ListView):
    template_name = "user_list.html"
    model = User
    paginate_by = 20


class DealerListPage(ListView):
    template_name = "user_list.html"
    paginate_by = 20
    queryset = User.objects.filter(is_staff = True)


class UserDetailsPage(DetailView):
    template_name = "user_details.html"
    model = User
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(UserDetailsPage, self).get_context_data(**kwargs)
        context['dealer_user_list'] = User.objects.filter(userprofile__dealer = self.object)
        context['not_used_packages'] = Package.objects.all()
        return context
