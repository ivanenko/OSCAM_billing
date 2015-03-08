from django.core.urlresolvers import reverse


def get_menu(request):

    return {
        "menu": [
            {"name": "Home", "url": reverse("home")},
            {"name": "Users", "subitems": [
                {"name": "All users", "url": reverse("user_list")},
                {"name": "Only dealers", "url": reverse("dealer_list")} if request.user.is_superuser==True else None,
                {"name": "Create New User", "url": reverse("create_user")},
            ]},
            {"name": "Payments", "subitems": [
                {"name": "All payments", "url": reverse("payments")},
                {"name": "Add payment manually", "url": reverse("create_payment")},
            ]},
            {"name": "Packages", "url": reverse("package_list")},

        ]
    }
