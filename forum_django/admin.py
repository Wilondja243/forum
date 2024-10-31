from django.contrib import admin
from .models import Student, QuestionModel


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['user_id','title','content','description','question_date']

admin.site.register(QuestionModel, QuestionAdmin)
admin.site.register(Student)
