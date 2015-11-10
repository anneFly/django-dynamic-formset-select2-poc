from django import forms
from django_select2.forms import ModelSelect2Widget
from poc.app.models import Book


class BookSelect2Widget(ModelSelect2Widget):
    search_fields = [
        'title__icontains',
    ]


class BooksForm(forms.Form):
    book = forms.ModelChoiceField(
        queryset=Book.objects.all(),
        widget=BookSelect2Widget,
    )


BookFormset = forms.formset_factory(BooksForm)
