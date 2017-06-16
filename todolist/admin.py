from django.contrib import admin
from .models import Task, Tasklist

# from .models import *
# from tags_input import admin as tags_input_admin
#
# class YourAdmin(tags_input_admin.TagsInputAdmin):
#     pass
#
# admin.site.register(models.YourModel, YourAdmin)
# Register your models here.
admin.site.register(Task)
admin.site.register(Tasklist)
