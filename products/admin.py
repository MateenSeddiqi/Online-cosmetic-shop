from django.contrib import admin
from .models import Feedback, Product, contactUs
# Register your models here.

admin.site.register(Feedback)
admin.site.register(Product)
admin.site.register(contactUs)