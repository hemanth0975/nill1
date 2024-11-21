from django import forms
from .models import Student

# class Student_details(forms.Form):
    
#     name = forms.CharField(max_length=50)
#     usn = forms.CharField(max_length=10)
#     mobile = forms.IntegerField()
#     course = forms.CharField(max_length=20)

class Student_details(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','usn','mobile','course']       # (or) we cna use  " __all__ "
        labels = {
            'usn' : 'USN_Number'
        }
        widgets = {
            'name' : forms.Textarea(attrs={
                'rows' : 3,
                'cols' : 20,
                'placeholder' : 'add your name',
                'class' : 'text',
            }),

            'usn' : forms.Textarea(attrs={
                'rows' : 3,
                'cols' : 20,
                'placeholder' : 'add your university number',
                'class' : 'text',
            })
        }