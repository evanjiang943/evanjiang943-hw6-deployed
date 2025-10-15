from django.contrib import admin
from .models import Assignment, RubricCriterion


class RubricCriterionInline(admin.TabularInline):
    model = RubricCriterion
    extra = 1


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'rubric_type', 'created_at']
    list_filter = ['rubric_type', 'created_at']
    search_fields = ['title', 'description']
    inlines = [RubricCriterionInline]


@admin.register(RubricCriterion)
class RubricCriterionAdmin(admin.ModelAdmin):
    list_display = ['name', 'assignment', 'points', 'order']
    list_filter = ['assignment']

