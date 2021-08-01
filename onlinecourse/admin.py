from django.contrib import admin
# Import any new Models here
from .models import Choice, Course, Instructor, Learner, Lesson, Question


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionInline(admin.ModelAdmin):
    inlines = [ChoiceInline]
    model = Question
    extra = 5


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# Register Question and Choice models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionInline)
admin.site.register(Instructor)
admin.site.register(Learner)
