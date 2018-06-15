from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from myapp.models import Vote, Question

def index(request):
    question_list = Question.objects.all()
    return render(request, 'index.html', {'question_list':question_list})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})

def create_page(request):
    return render(request, 'create.html')

def create(request):
    if request.method == 'POST':
        Question.objects.create(question_text=request.POST.get('question', ''),
             choice_text=request.POST.get('answer', ''))
        return redirect('/')
    items = Question.objects.all()
    return render(request, 'index.html', {'items': items})

