from accounts.models import User, Vendor, Customer
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


class VendorSignUpForm(UserCreationForm):
    """
    Extending djabgo form method
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "username", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_vendor = True
        user.save()
        vendor = Vendor.objects.create(user=user)
        return user

class CustomerSignUpForm(UserCreationForm):
    """
    Customer sign up form
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        return user
