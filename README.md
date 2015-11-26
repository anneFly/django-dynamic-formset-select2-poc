# django-select2 & django-dynamic-formset demo
Working example that [django-select2](https://github.com/applegrew/django-select2) can work with [django-dynamic-formset](https://github.com/elo80ka/django-dynamic-formset).

If you have trouble setting up django-select2 and django-dynamic-formset together, this repository might help you.
Checkout [this example](https://github.com/anneFly/django-dynamic-formset-select2-poc/blob/master/poc/app/templates/book-list.html).
It contains everything you need. There is also [another example](https://github.com/anneFly/django-dynamic-formset-select2-poc/blob/master/poc/app/templates/book-list-multiple.html)
showing several formsets one page.

## Step by Step
Let's assume your formset is called `form` in your template context.

1) Create a hidden container for your template and render an `empty_form` inside. Give your container a class or an id so that you can use it later in the javascript, e.g. `id="formset-template"`

```
<div id="formset-template" style="display: none;">
    {{ form.empty_form }}
</div>
```


2) Render your formset inside some container that has a class or id which you can later use for initializing the dynamic formset. In this example it had the id "formset":
```
<form>
    {{ form.management_form }}
    <div id="formset">
        {% for f in form %}
            {{ f }}
        {% endfor %}
    </div>
    <button type="submit">submit</button>
</form>
```


3) Include jQuery and the django-dynamic-form js
```
<script src="//code.jquery.com/jquery-2.1.4.min.js"></script>
<script src="{% static 'jquery.formset.js' %}"></script>
```

4) Include form.media for django-select2 to work
In your html `head` include `{{ form.media.css }}`
At the end of your `body` include `{{ form.media.js }}`

5) Initialize dynamic-formset
Here is important, that you do pass a __copy__ of your formset template element: `formTemplate: $('#formset-template').clone()`.
In the `added` callback of django-dynamic-form you need to initialize your newly created form by calling `djangoSelect2()` on the new django-select2 element.
The whole code could look like this:
```
$('#formset').formset({
    formTemplate: $('#formset-template').clone(),
    added: function (row) {
        row.find('.django-select2').djangoSelect2();
    }
});
```

__Important__: It is necessary that the code from step 5 runs before the code from `{{ form.media.js }}`. This should automatically be the case if you do not wrap your code insde a jQuery `$(document).ready`. However, if you do want to wrap this code inside a `$(document).ready` then include it __before__ `{{ form.media.js }}`.
