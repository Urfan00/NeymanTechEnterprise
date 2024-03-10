from modeltranslation.translator import translator, TranslationOptions
from .models import Blog, BlogCategory



class BlogCategoryUsTranslationOptions(TranslationOptions):
    fields = ('blog_category_title',)


class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'content')


translator.register(BlogCategory, BlogCategoryUsTranslationOptions)
translator.register(Blog, BlogTranslationOptions)
