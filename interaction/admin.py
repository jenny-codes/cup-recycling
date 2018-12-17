from django.contrib import admin
from interaction.models import *

# does the same thing as admin.site.register(Cup, CupAdmin)
@admin.register(Cup)
class CupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status', 'carrier_type', 'carrier')
    list_filter = ('carrier_type', 'status')

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('pk', 'location', 'active')

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerSignUpForm, CupUserChangeForm
from .models import CupUser


# FIX
class CupUserAdmin(UserAdmin):
    add_form = CustomerSignUpForm
    form = CupUserChangeForm
    model = CupUser
    list_display = ['email', 'username',]

admin.site.register(CupUser, CupUserAdmin)


# @admin.register(Business)
# class BusinessAdmin(admin.ModelAdmin):
#     list_display = ('name', 'phone', 'email', 'active')
#     fieldsets = (
#         ('Basic Information', {
#             'fields': ('name', 'phone','email', 'address')
#         }),
#         (None, {
#             'fields': ('active',)
#         }),
#     )