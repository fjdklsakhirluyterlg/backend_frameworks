from django import forms

class TodoForm(forms.Form):
    title = forms.CharField(max_length=350)