from django.contrib import admin
from questions.models import *

# Register your models here.

admin.site.register(Question)
admin.site.register(Label)
admin.site.register(LabelsQuestion)