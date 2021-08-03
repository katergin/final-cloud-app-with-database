from django.contrib import admin
from .models import Choice, Course, Instructor, Learner, Lesson, Question


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionInline(admin.ModelAdmin):
    inlines = [ChoiceInline]
    model = Question
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title',)


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_time')


class LearnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'occupation', 'social_link')


# Register Question and Choice models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionInline)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Learner, LearnerAdmin)
