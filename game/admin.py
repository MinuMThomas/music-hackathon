from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Question)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'answer',
        )
