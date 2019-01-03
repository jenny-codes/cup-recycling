from django.contrib import admin
from interaction.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from interaction.forms.registration_forms import CustomerSignUpForm, CupUserChangeForm

# does the same thing as admin.site.register(Cup, CupAdmin)
@admin.register(Cup)
class CupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status', 'carrier_type', 'carrier')
    list_filter = ('carrier_type', 'status')

# FIX
class CupUserAdmin(UserAdmin):
    add_form = CustomerSignUpForm
    form = CupUserChangeForm
    model = CupUser
    list_display = ['email', 'username',]

admin.site.register(CupUser, CupUserAdmin)