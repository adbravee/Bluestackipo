from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Company, IPO, Document, CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_approved')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_approved')
    fieldsets = UserAdmin.fieldsets + (
        ('Approval', {'fields': ('is_approved',)}),
    )
    actions = ['approve_users']

    def approve_users(self, request, queryset):
        queryset.update(is_approved=True)
    approve_users.short_description = "Approve selected users"

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name',)
    search_fields = ('company_name',)

@admin.register(IPO)
class IPOAdmin(admin.ModelAdmin):
    list_display = ('company', 'status', 'open_date', 'close_date', 'listing_date')
    list_filter = ('status', 'open_date', 'close_date', 'listing_date')
    search_fields = ('company__company_name',)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('ipo', 'rhp_pdf', 'drhp_pdf')
    search_fields = ('ipo__company__company_name',)
