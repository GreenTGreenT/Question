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
    #items = Question.objects.get(id=question_id)
    if request.method == 'POST':
       answer = request.POST.get('choice')
       check_answer = Question.objects.get(id=question_id).choice_text
       vote = Vote.objects.get(connect=question_id)
      
       if answer == check_answer:
          vote.vote_true += 1
          vote.save()
          return render(request, 'results_t.html', {'vote':vote})
       else:
          vote.vote_false += 1
          vote.save()
          return render(request, 'results_f.html', {'vote':vote})

def create_page(request):
    return render(request, 'create.html')

def create(request):
    if request.method == 'POST':
        q = Question(question_text=request.POST.get('question', ''), choice_text=request.POST.get('answer', '') )
        q.save()
       
        v = Vote(vote_true=0, vote_false=0, connect=q)
        v.save()
        return redirect('/')
    items = Question.objects.all()
    return render(request, 'index.html', {'items': items})

