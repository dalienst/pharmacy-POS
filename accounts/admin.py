from django.contrib import admin

from accounts.models import User, Vendor, Customer

admin.site.register(User)
admin.site.register(Vendor)
admin.site.register(Customer)
