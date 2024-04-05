from django.contrib import admin
from .models import Student,Aadhar
# Register your models here.

# ------------------- first method to show in admin pannel---------------------
# admin.site.register(Student)
# admin.site.register(Aadhar)

# ------------------- Second method to show in admin pannel---------------------
# @admin.register(Aadhar)
# class AadharAdmin(admin.ModelAdmin):
#     list_display = ['id','aadhar_no']

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['stu_name','aadhar_no']


# ------------------- Third method to show in admin pannel---------------------
class AadharAdmin(admin.ModelAdmin):
    list_display = ['id','aadhar']
admin.site.register(Aadhar,AadharAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','stu_name','stu_email','stu_contact','aadhar']
admin.site.register(Student,StudentAdmin)