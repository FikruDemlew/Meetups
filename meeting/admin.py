from django.contrib import admin

from .models import Meeting
# Register your models here.
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Meeting, MeetingAdmin)