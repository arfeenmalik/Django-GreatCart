from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)


admin.site.register(models.Account, AccountAdmin)