from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display=['email','first_name','last_name','last_login','is_active']
    filter_horizontal=()
    list_display_links=['email','first_name']
    # filter_horizontal=()
    list_filter=()
    # fieldsets-()


admin.site.register(Account,AccountAdmin)