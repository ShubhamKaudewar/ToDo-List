from django.contrib import admin

# Register your models here.
from todoList.models import noteModel

class noteModelList(admin.ModelAdmin):
    list_display = ('noteStar','noteStyle','noteBold','noteItalic','noteUnderline','noteTextColor','noteBackgroundColor')

admin.site.register(noteModel,noteModelList)