from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

class SlideAdmin(admin.TabularInline):
    model = Slide

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('description', )

class FlashcardAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    inlines = [SlideAdmin]
    list_display = ['title', 'author', 'number_of_slides', 'date_created']
    summernote_fields = ('description', )

admin.site.register(Profile)
admin.site.register(FlashCard, FlashcardAdmin)
admin.site.register(Slide, PostAdmin)

# Register your models here.
