from modeltranslation.translator import translator, TranslationOptions
from .models import DifferentUs



class DifferentUsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(DifferentUs, DifferentUsTranslationOptions)
