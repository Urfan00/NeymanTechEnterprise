from modeltranslation.translator import translator, TranslationOptions
from .models import Service, ServiceCard



class ServiceTranslationOptions(TranslationOptions):
    fields = ('service_title', 'service_slug', 'description')


class ServiceCardTranslationOptions(TranslationOptions):
    fields = ('service_card_title', 'service_card_content')



translator.register(Service, ServiceTranslationOptions)
translator.register(ServiceCard, ServiceCardTranslationOptions)
