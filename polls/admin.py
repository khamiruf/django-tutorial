from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Owner', {'fields': ['owner']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question',        {'fields': ['question']}),
        ('Choices',         {'fields' : ['choice_text']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
