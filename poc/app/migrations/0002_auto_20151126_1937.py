# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def add_data(apps, schema_editor):
    Book = apps.get_model('app', 'Book')
    books = []
    for i in range(100):
        books.append(Book(title='Book nr. {}'.format(i)))

    Book.objects.bulk_create(books)


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_data)
    ]
