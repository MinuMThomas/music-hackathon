import random
from django.shortcuts import render
from django.db import models
from .models import Question


def game(request):
    if request.method == 'POST':
        print(request.POST)
        questions = list(Question.objects.all())[:10]
        random.shuffle(questions)
        clueOne = Question.clue1
        clueTwo = Question.clue2
        score = 500
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.name))
            print(q.answer)
            if q.answer == request.POST.get(q.name):
                score += 50
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10) * 100
        template_name = 'game/game.html'
        context = {
            'questions': questions,
            'score': score
            # 'time': request.POST.get('timer'),
            # 'correct': correct,
            # 'wrong': wrong,
            # 'percent': percent,
            # 'total': total
        }
        return render(request, template_name, context)
    else:
        questions = list(Question.objects.all())[:10]
        random.shuffle(questions)
        template_name = 'game/game.html'
        context = {
            'questions': questions
        }
        return render(request, template_name, context)
