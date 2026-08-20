from django.contrib import admin
from .models import ContactRecord

@admin.register(ContactRecord)
class ContactRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')