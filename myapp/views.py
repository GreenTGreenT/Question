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
    return render(request, 'results.html')   


def keep_results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    items = Question.objects.get(id=question_id)
    if request.method == 'POST':
       answer = request.POST.get('choice')
       check_answer = Question.objects.get(id=question_id).choice_text
       vote = Vote.object.get(connect=items)
       to_plus = vote.vote_true 
       if answer == check_answer:
          to_plus += 1
          vote.save()
          point = Vote.objects.get(connect=items).vote_true
          return render(request, 'results_t.html', {'point':point})
       else:
          keep = Vote.objects.get(connect=question_id)
          keep.vote_false += 1
          keep.save()
          
          point = Vote.objects.get(connect=question_id).vote_false
          return render(request, 'results_f.html', {'point':point})

def create_page(request):
    return render(request, 'create.html')

def create(request):
    if request.method == 'POST':
        q = Question(question_text=request.POST.get('question', ''), choice_text=request.POST.get('answer', '') )
        q.save()
       
        v = Vote(vote_true=0, vote_false=0, connect=q)
        v.save()
        #Question.objects.create(question_text=request.POST.get('question', ''),
             #choice_text=request.POST.get('answer', '')),
        return redirect('/')
    items = Question.objects.all()
    return render(request, 'index.html', {'items': items})

