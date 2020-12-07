from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegularUserChangeForm, RegularUserCreationForm
from .models import RegularUser


class RegularUserAdmin(UserAdmin):
    add_form = RegularUserCreationForm
    form = RegularUserChangeForm
    model = RegularUser
    list_display = [
        'username', 'phone_number', 'email', 'postal_code',
    ]


admin.site.register(RegularUser, RegularUserAdmin)
