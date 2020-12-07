from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import RegularUser


class RegularUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = RegularUser
        fields = UserCreationForm.Meta.fields + (
            'email', 'phone_number', 'postal_code', 'age', 'sex',
        )


class RegularUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = RegularUser
        fields = UserChangeForm.Meta.fields
