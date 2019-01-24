from django.contrib import admin
from polls.models import Choice, Question


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3
	

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['question_text']}),
       	('Date information', {'fields': ['pub_date']}),
	]
	list_display = ('question_text', 'pub_date')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
