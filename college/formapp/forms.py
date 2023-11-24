from django import forms
from . models import Registeration,Courses

class RegisterForm(forms.ModelForm):
    class Meta:
        model=Registeration
        fields = '__all__'
        widgets = {'dob': forms.DateInput(attrs={'type': 'date'}),
                    'gender': forms.RadioSelect(),
                  'materials':forms.CheckboxSelectMultiple(choices=(('chart','Chart Paper'),('files','Files'),('pencil','Pencil'),('note','Notebook'),('pen','Pen'),('exam','Exam Papers')))
                    }
#'materials':forms.CheckboxSelectMultiple


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['course'].queryset = Courses.objects.none()


        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Courses.objects.filter(department_id=department_id).order_by('name')

            except(ValueError , TypeError):
                pass

        elif self.instance.pk:
            self.fields['course'].queryset= self.instance.department.course_set.order_by('name')




