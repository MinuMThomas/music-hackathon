from django.contrib import admin
from . import models
<<<<<<< HEAD
=======

>>>>>>> 4d85d64e136ca3e29a6c4fd10256077de3fabc39

# Register your models here.
@admin.register(models.Question)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'answer',
        )
