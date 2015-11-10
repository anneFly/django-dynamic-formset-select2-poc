from django.views.generic import FormView

from poc.app.forms import BookFormset


class BookView(FormView):
    template_name = 'books.html'
    form_class = BookFormset
    success_url = '/'
