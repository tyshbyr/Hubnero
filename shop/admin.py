from django.contrib import admin

from .models import Seller, Customer, Lot, Feedback, Deal,Status


admin.site.register(Seller)
admin.site.register(Customer)
admin.site.register(Lot)
admin.site.register(Feedback)
admin.site.register(Deal)
admin.site.register(Status)
