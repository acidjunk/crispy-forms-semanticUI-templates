from __future__ import unicode_literals

from crispy_forms import bootstrap


class PrependedAppendedText(bootstrap.PrependedAppendedText):
    template = "%s/layout/prepended_appended_text.html"


class AppendedText(PrependedAppendedText):
    def __init__(self, field, text, *args, **kwargs):
        kwargs.pop('appended_text', None)
        kwargs.pop('prepended_text', None)
        self.text = text
        super(AppendedText, self).__init__(field, appended_text=text, **kwargs)


class PrependedText(PrependedAppendedText):
    def __init__(self, field, text, *args, **kwargs):
        kwargs.pop('appended_text', None)
        kwargs.pop('prepended_text', None)
        self.text = text
        super(PrependedText, self).__init__(field, prepended_text=text, **kwargs)


class FormActions(bootstrap.FormActions):
    template = "%s/layout/formactions.html"


class InlineCheckboxes(bootstrap.InlineCheckboxes):
    """
    Layout object for rendering checkboxes inline::

        InlineCheckboxes('field_name')
    """
    template = "%s/layout/checkboxselectmultiple_inline.html"


class InlineRadios(bootstrap.InlineRadios):
    """
    Layout object for rendering radiobuttons inline::

        InlineRadios('field_name')
    """
    template = "%s/layout/radioselect_inline.html"


class FieldWithButtons(bootstrap.FieldWithButtons):
    template = '%s/layout/field_with_buttons.html'
    field_template = '%s/layout/field.html'


class StrictButton(bootstrap.StrictButton):
    """
    Layout object for rendering an HTML button::

        Button("button content", css_class="extra")
    """
    template = 'bootstrap4/layout/button.html'
    field_classes = "ui button"

    def __init__(self, content, **kwargs):
        super(StrictButton, self).__init__(content, **kwargs)

        kwargs.setdefault('type', 'submit')


class UneditableField(bootstrap.UneditableField):
    """
    Layout object for rendering fields as uneditable in bootstrap

    Example::

        UneditableField('field_name', css_class="input-xlarge")
    """
    template = "%s/layout/uneditable_input.html"

    def __init__(self, field, *args, **kwargs):
        self.attrs = {'class': 'uneditable-input'}
        super(UneditableField, self).__init__(field, *args, **kwargs)


class InlineField(bootstrap.InlineField):
    template = "%s/layout/inline_field.html"
