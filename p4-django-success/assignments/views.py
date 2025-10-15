from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Assignment, RubricCriterion
import json
import time


def index(request):
    """Home page with assignment creation form"""
    assignments = Assignment.objects.all()[:5]
    return render(request, 'assignments/index.html', {
        'assignments': assignments
    })


def create_assignment(request):
    """Handle assignment creation"""
    if request.method == 'POST':
        try:
            # Create assignment
            assignment = Assignment(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                answer_key=request.FILES.get('answer_key'),
                rubric_type=request.POST.get('rubric_type', 'ai_generated')
            )
            
            # Handle rubric based on type
            if assignment.rubric_type == 'uploaded' and 'rubric_file' in request.FILES:
                assignment.rubric_file = request.FILES['rubric_file']
            elif assignment.rubric_type == 'ai_generated':
                # Generate AI rubric
                rubric_data = generate_ai_rubric(request.FILES.get('answer_key'))
                assignment.rubric_data = rubric_data
                
                # Save to database
                assignment.save()
                
                # Create rubric criteria
                for i, criterion in enumerate(rubric_data['criteria']):
                    RubricCriterion.objects.create(
                        assignment=assignment,
                        name=criterion['name'],
                        points=criterion['points'],
                        description=criterion['description'],
                        grading_notes=criterion.get('grading_notes', ''),
                        order=i
                    )
            else:
                assignment.save()
            
            if assignment.rubric_type != 'ai_generated':
                assignment.save()
            
            messages.success(request, 'Assignment created successfully!')
            return redirect('assignment_detail', pk=assignment.pk)
            
        except Exception as e:
            messages.error(request, f'Error creating assignment: {str(e)}')
            return redirect('index')
    
    return redirect('index')


def assignment_detail(request, pk):
    """View assignment details"""
    assignment = get_object_or_404(Assignment, pk=pk)
    criteria = assignment.criteria.all()
    
    return render(request, 'assignments/detail.html', {
        'assignment': assignment,
        'criteria': criteria
    })


def assignment_list(request):
    """List all assignments"""
    assignments = Assignment.objects.all()
    return render(request, 'assignments/list.html', {
        'assignments': assignments
    })


def generate_rubric_ajax(request):
    """AJAX endpoint to generate rubric"""
    if request.method == 'POST':
        try:
            # Simulate AI processing
            time.sleep(1.5)
            
            rubric = generate_ai_rubric(None)
            return JsonResponse({
                'success': True,
                'rubric': rubric
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)


def generate_ai_rubric(answer_key_file):
    """
    Mock AI rubric generation.
    In production, this would call an LLM API.
    """
    return {
        'criteria': [
            {
                'name': 'Problem 1: Understanding',
                'points': 8,
                'description': 'Demonstrates clear understanding of fundamental concepts',
                'grading_notes': 'Look for key terminology and accurate definitions'
            },
            {
                'name': 'Problem 1: Solution Correctness',
                'points': 12,
                'description': 'Arrives at correct final answer with valid reasoning',
                'grading_notes': 'Partial credit for correct method with minor errors'
            },
            {
                'name': 'Problem 2: Methodology',
                'points': 10,
                'description': 'Selects and applies appropriate problem-solving approach',
                'grading_notes': 'Alternative valid methods are acceptable'
            },
            {
                'name': 'Problem 2: Calculations',
                'points': 8,
                'description': 'Performs calculations accurately and systematically',
                'grading_notes': 'Deduct 1-2 points for minor computational errors'
            },
            {
                'name': 'Problem 3: Critical Thinking',
                'points': 10,
                'description': 'Shows analytical thinking and justifies conclusions',
                'grading_notes': 'Award full points for well-reasoned explanations'
            },
            {
                'name': 'Presentation & Organization',
                'points': 7,
                'description': 'Work is clearly presented with all steps shown',
                'grading_notes': 'Deduct for missing work or unclear presentation'
            },
        ],
        'total_points': 55,
        'ai_confidence': 0.92,
        'generated_at': time.strftime('%Y-%m-%d %H:%M:%S')
    }

