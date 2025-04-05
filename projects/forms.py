from django.forms import ModelForm, widgets
from django import forms
from .models import Projects, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'
        exclude = ['vote_total','vote_ratio','owner']
        widgets = {
            'tags' : forms.CheckboxSelectMultiple(),
        }
    def __init__(self, *args, **kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']
        labels = {'value': 'Place your vote','body': ' Add a comment'}
    def __init__(self, *args, **kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})



    
    