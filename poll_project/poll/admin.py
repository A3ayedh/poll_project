from django.contrib import admin
from django.db.models import Count
from .models import Poll, Option, Response

# Register your models here.
class OptionInline(admin.TabularInline):
    model = Option
    extra = 1

class ResponseInline(admin.TabularInline):
    model = Response
    extra = 1

class PollAdmin(admin.ModelAdmin):
    inlines = [OptionInline, ResponseInline]
    list_display = ('question', 'active_until', 'status', 'response_count', 'question_and_options')
    search_fields = ['question']
    list_filter = ['status']

    def response_count(self, obj):
        return obj.option_set.aggregate(response_count=Count('response')).get('response_count', 0)

    response_count.short_description = 'Responses'

    def question_and_options(self, obj):
        options = obj.option_set.all()
        return ', '.join([option.text for option in options])
    question_and_options.short_description = 'Question and Options'

admin.site.register(Poll, PollAdmin)

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('name', 'time', 'option_text', 'poll_title')

    def option_text(self, obj):
        return obj.option.text
    option_text.short_description = 'Option'

    def poll_title(self, obj):
        return obj.option.poll.title
    poll_title.short_description = 'Poll'

admin.site.register(Response, ResponseAdmin)