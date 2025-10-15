from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
import json


class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    answer_key = models.FileField(upload_to='answer_keys/')
    rubric_type = models.CharField(
        max_length=20,
        choices=[
            ('ai_generated', 'AI Generated'),
            ('uploaded', 'Uploaded'),
        ]
    )
    rubric_file = models.FileField(upload_to='rubrics/', null=True, blank=True)
    rubric_data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_rubric_display_data(self):
        """Get rubric data for display"""
        if self.rubric_type == 'ai_generated' and self.rubric_data:
            return self.rubric_data
        return None


class RubricCriterion(models.Model):
    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
        related_name='criteria'
    )
    name = models.CharField(max_length=200)
    points = models.IntegerField()
    description = models.TextField()
    grading_notes = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.points} pts)"

