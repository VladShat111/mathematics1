from django.contrib import admin
from .models import Lesson, Feedback
# Register your models here.
admin.site.register(Lesson)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'text')