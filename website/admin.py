from django.contrib import admin
from .models import Contact, Newsletter


class ContactAdmin(admin.ModelAdmin):
    """
    This class is for displaying contact in administration
    """
    date_hierarchy = 'created_date'
    list_display = ('name', 'email')
    list_filter = ('email',)
    search_fields = ('name', 'message')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)
