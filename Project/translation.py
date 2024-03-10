from modeltranslation.translator import translator, TranslationOptions
from .models import Project



class ProjectTranslationOptions(TranslationOptions):
    fields = ('project_title', 'project_slug')


translator.register(Project, ProjectTranslationOptions)
