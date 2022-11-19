from django.shortcuts import render
from django.db import models
from .models import Question

def game(request):
    questions = Question.objects.all()
    # if request.method == 'POST':
    #     print(request.POST)
    #     questions = Question.objects.all()
    #     clueOne = Question.clue1
    #     clueTwo = Question.clue2
    #     score = 500
    #     wrong = 0
    #     correct = 0
    #     total = 0
    #     for q in questions:
    #         total += 1
    #         print(request.POST.get(q.question))
    #         print(q.ans)
    #         print()
    #         if q.ans == request.POST.get(q.question):
    #             score += 50
    #             correct += 1
    #         else:
    #             wrong += 1
    #     percent = score/(total*10) * 100
    template_name = 'game/game.html'
    context = {
        'questions': questions
        # 'score': score,
        # 'time': request.POST.get('timer'),
        # 'correct': correct,
        # 'wrong': wrong,
        # 'percent': percent,
        # 'total': total
    }
    return render(request, template_name, context)
    # else:
    #     questions = Question.objects.all()
    #     template_name = 'game/game.html'
    #     context = {
    #         'questions': questions
    #     }
    #     return render(request, template_name, context)
