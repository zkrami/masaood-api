from django.contrib import admin

# Register your models here.
from .models import User , UserAdmin

admin.site.register(User , UserAdmin)
admin.register(User , UserAdmin)