from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from accounts.models import User, Vendor, Customer
from accounts.forms import VendorSignUpForm, CustomerSignUpForm
from django.contrib.auth import login
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)


"""
Admin/staff views
Acccess all users
Update users status
Delete users
"""


class UserListView(UserPassesTestMixin, generic.ListView):
    """admin sees all users"""

    model = User
    template_name = "accounts/users_list.html"
    paginate_by = 6

    def test_func(self):
        return self.request.user.is_staff


class UserDetailView(UserPassesTestMixin, generic.DetailView):
    """details on specific users"""

    model = User
    template_name = "accounts/user_detail.html"

    def test_func(self):
        return self.request.user.is_staff


class UserUpdateView(UserPassesTestMixin, UpdateView):
    """
    admin updates user but only their roles
    """

    model = User
    template_name = "accounts/user_update.html"
    fields = [
        "is_customer",
        "is_vendor",
    ]
    success_url = reverse_lazy("users")

    def test_func(self):
        return self.request.user.is_staff


class UserDeleteView(UserPassesTestMixin, DeleteView):
    """
    admin deletes a user
    """

    model = User
    template_name = "accounts/user_delete.html"
    success_url = reverse_lazy("users")

    def test_func(self):
        return self.request.user.is_staff


"""
Sign up views for users
Both vendor and customer
"""


class SignUpView(TemplateView):
    """
    Give the option to sign up as a vendor or a customer
    """

    template_name = "registration/signup.html"


class VendorsSignUpView(CreateView):
    """
    vendors sign up
    """

    model = User
    form_class = VendorSignUpForm
    template_name = "registration/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "vendor"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("index")


class CustomersSignUpView(CreateView):
    """
    customers sign up
    """

    model = User
    form_class = CustomerSignUpForm
    template_name = "registration/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "customer"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("index")


"""
Detail views for users
"""


class VendorDetailView(LoginRequiredMixin, generic.DetailView):
    """
    Vendor sees their profile
    """

    model = Vendor
    template_name = "accounts/profile.html"


class CustomerDetailView(LoginRequiredMixin, generic.DetailView):
    """
    customer views their profile
    """

    model = Customer
    template_name = "accounts/profile.html"


"""
Update view classes for users
"""


class VendorUpdateView(LoginRequiredMixin, UpdateView):
    """
    vendor updates profile
    """

    model = Vendor
    fields = [
        "name",
        "contact",
        "location",
    ]
    template_name = "accounts/update_profile.html"
    success_url = reverse_lazy("index")


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    """
    customer updates profile
    """

    model = Customer
    fields = [
        "name",
        "contact",
        "location",
    ]
    template_name = "accounts/update_profile.html"
    success_url = reverse_lazy("index")


"""
Account deletion views
"""


class VendorDeleteView(LoginRequiredMixin, DeleteView):
    """
    vendor deletes their account completely
    """

    model = Vendor
    template_name = "accounts/delete_account.html"
    success_url = reverse_lazy("signup")


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    """
    customer deletes their account completely
    """

    model = Customer
    template_name = "accounts/delete_account.html"
    success_url = reverse_lazy("signup")
