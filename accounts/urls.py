from django.urls import path
from accounts.views import (
    UserDeleteView,
    UserListView,
    UserUpdateView,
    CustomerDeleteView,
    CustomerDetailView,
    CustomersSignUpView,
    CustomerUpdateView,
    VendorDeleteView,
    VendorDetailView,
    VendorUpdateView,
    VendorsSignUpView,
    SignUpView,
    UserDetailView,
)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signup/vendor/", VendorsSignUpView.as_view(), name="vendor-signup"),
    path("signup/customer/", CustomersSignUpView.as_view(), name="customer-signup"),
    path("users/", UserListView.as_view(), name="users"),
    path("user/<int:pk>/detail/", UserDetailView.as_view(), name="user-detail"),
    path("user/<int:pk>/update/", UserUpdateView.as_view(), name="user-update"),
    path("user/<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"),
    path("profile/<int:pk>/vendor/", VendorDetailView.as_view(), name="vendor-profile"),
    path("update/<int:pk>/vendor/", VendorUpdateView.as_view(), name="vendor-update"),
    path("delete/<int:pk>/vendor/", VendorDeleteView.as_view(), name="vendor-delete"),
    path(
        "profile/<int:pk>/customer/",
        CustomerDetailView.as_view(),
        name="customer-profile",
    ),
    path(
        "update/<int:pk>/customer/",
        CustomerUpdateView.as_view(),
        name="customer-update",
    ),
    path(
        "delete/<int:pk>/customer/",
        CustomerDeleteView.as_view(),
        name="customer-delete",
    ),
]
