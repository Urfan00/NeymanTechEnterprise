from modeltranslation.translator import translator, TranslationOptions
from .models import FAQ



class FAQTranslationOptions(TranslationOptions):
    fields = ('faq', 'answer')


translator.register(FAQ, FAQTranslationOptions)
