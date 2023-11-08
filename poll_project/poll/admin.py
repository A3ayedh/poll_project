from django.contrib import admin
from django.db.models import Count
from .models import Poll, Option, Response

# Register your models here.

class OptionInline(admin.TabularInline):   #TabularInlineused to display related model objects in a tabular, making it suitable for cases you have a list of related items to display and edit.
    model = Option
    num = 1

class ResponseInline(admin.TabularInline):
    model = Response
    num1 = 1

class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'active_until', 'status', 'response_count', 'question_and_options')
    search_fields = ['question']
    list_filter = ['status']
    inlines = [OptionInline, ResponseInline] #inlines attribute in an admin class is used to specify one or more inline classes that define how related models should be displayed and managed within the admin page for the primary model.

    def response_count(self, obj):
        return obj.option_set.aggregate(response_count=Count('response')).get('response_count', 0)   #we use .aggregate(response_count=Count('response')): to count respond

    response_count.short_description = 'Responses'  # to make it user friendly and readable 
 
    def question_and_options(self, obj):
        options = obj.option_set.all()  # obj.obtion_set is a queryset
        return ', '.join([option.text for option in options])
    question_and_options.short_description = 'Question and Options'

admin.site.register(Poll, PollAdmin)

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('name', 'time', 'option_text', 'poll_title')

    def option_text(self, obj):
        return obj.option.text
    option_text.short_description = 'Option'

    def poll_title(self, obj):   #obj is an instance of the model. 
        return obj.option.poll.title
    poll_title.short_description = 'Poll'

admin.site.register(Response, ResponseAdmin)
