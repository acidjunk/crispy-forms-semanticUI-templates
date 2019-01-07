# crispy-forms-semanticUI-templates

crispy-forms-semanticUI-templates contains a set of templates that can be used to get 
semantic UI formlayouts and error handling in [`django-crispy-forms`](https://github.com/maraujop/django-crispy-forms). 

Tested with Semantic-UI 2.2.4.

### Manual Install

1. Copy the `semantic-ui` folder to your main templates folder in your Django app.

2. Install [`django-crispy-forms`](https://github.com/maraujop/django-crispy-forms) and set `semantic-ui` as your `CRISPY_TEMPLATE_PACK` in your projects' `settings.py`:

```python
CRISPY_TEMPLATE_PACK = 'semantic-ui'
```

Be warned its a work in progress!!
Any help to complete it is appeciated.

### PIP based Install

1. `pip install crispy-forms-semantic-ui`

2. set `semantic-ui` as your `CRISPY_TEMPLATE_PACK` in your projects' `settings.py`

### Generic install steps

3. add `crispy_forms_semantic_ui` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'crispy_forms',
    'crispy_forms_semantic_ui',
    ...
]
```

4. Add `semantic-ui` to the allowed `CRISPY_ALLOWED_TEMPLATE_PACKS` array in your `settings`:

```python
CRISPY_ALLOWED_TEMPLATE_PACKS = ('bootstrap', 'uni_form', 'bootstrap3',
                                 'bootstrap4', 'semantic-ui',)
```
