from django.contrib import admin
from .models import *


# Register your models here.

#admin.site.register(Content)
admin.site.register(NewContent)
admin.site.register(Payment)
admin.site.register(Basket)
admin.site.register(ProductView)

admin.site.register(Profile)