from django.forms import ModelForm, TextInput, Textarea
from .models import Books


class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = ("title", "author", "description", "image")

        widgets = {
            "title": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px; margin-bottom: 25px;",
                    "placeholder": "Enter Book Name",
                }
            ),
            "author": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px; margin-bottom: 25px;",
                    "placeholder": "Enter Book Author",
                }
            ),
            "description": Textarea(
                attrs={
                    "rows": "5",
                    "class": "form-control",
                    "style": "max-width: 300px; margin-bottom: 25px",
                    "placeholder": "Enter Book Description",
                }
            ),
        }
