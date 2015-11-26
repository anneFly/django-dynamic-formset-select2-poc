from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView

from poc.app.forms import BookFormset


class BookListView(FormView):
    template_name = 'book-list.html'
    form_class = BookFormset
    success_url = '/'


class BookListMultipleView(FormView):
    template_name = 'book-list-multiple.html'
    form_class = BookFormset
    success_url = reverse_lazy('book-list-multiple')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form_kwargs = self.get_form_kwargs()

        form_kwargs.update({'prefix': 'form-1'})
        form1 = form_class(**form_kwargs)

        form_kwargs.update({'prefix': 'form-2'})
        form2 = form_class(**form_kwargs)

        return [form1, form2]

    def post(self, request, *args, **kwargs):
        forms = self.get_form()
        if all([form.is_valid() for form in forms]):
            return self.form_valid(forms)
        else:
            return self.form_invalid(forms)
