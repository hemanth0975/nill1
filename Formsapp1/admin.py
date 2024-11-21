from django.contrib import admin
from .models import Student

# Register your models here.

class studentsss(admin.ModelAdmin):
    list_display = ["name", "usn", "mobile", "course"]
    list_display_links = ["name"]

admin.site.register(Student, studentsss)