from django import forms

class CreateNewTask(forms.Form):
  title = forms.CharField(label="Titulo de tarea", max_length=100, required=True)
  description = forms.CharField(label="Descripción de la tarea", widget=forms.Textarea)
