from django.contrib import admin
from Student_marksheet.models import student_info, student_marks

# Register your models here.


admin.site.register(student_info)
admin.site.register(student_marks)