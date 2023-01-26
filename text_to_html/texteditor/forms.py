from django import forms
from ckeditor.widgets import CKEditorWidget



class EditorForm(forms.Form):
    body = forms.CharField(widget=CKEditorWidget(),label="Text Editor")
    