from django.contrib import admin
from interaction.models import Cup, Business, User, Machine

# does the same thing as admin.site.register(Cup, CupAdmin)
@admin.register(Cup)
class CupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status', 'owner_type', 'owner_id')
    list_filter = ('owner_type', 'status')

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'active')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'phone','email', 'address')
        }),
        (None, {
            'fields': ('active',)
        }),
    )

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'active')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'phone','email')
        }),
        (None, {
            'fields': ('active',)
        }),
    )

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('pk', 'location', 'active')