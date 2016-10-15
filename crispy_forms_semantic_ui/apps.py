from django.apps import AppConfig


class SemanticUIConfig(AppConfig):
    name = 'crispy_forms_semantic_ui'
    verbose_name = 'Crispy form templates for semantic UI'

    def ready(self):
        super(SemanticUIConfig, self).ready()