from django.shortcuts import render, redirect
import random

def index(request):
    request.session['counter'] = 0
    num = random.randint(1, 100 + 1)
    print(num)
    request.session['num'] = num
    return render(request, 'index.html')

def guessed_num(request):
    while request.session['counter'] != 5+1:
        if int(request.POST['num']) < request.session['num']:
            context = {
                "low_num": f"{request.POST['num']} is Too Low!"
            }
            request.session['counter'] += 1
            return render(request, 'low_num.html', context)
        elif int(request.POST['num']) > request.session['num']:
            context = {
                "high_num": f"{request.POST['num']} is Too High!"
            }
            request.session['counter'] += 1
            return render(request, 'high_num.html', context)
        else:
            context = {
                "correct_num": f"Guessed Right!!! {request.POST['num']} was the correct number!",
            }
            request.session['counter'] += 1
            return render(request, 'correct_num.html', context)
    return render(request, 'try_again.html')

def log_winner(request):
    if 'log' not in request.session:
        request.session['log'] = []
    request.session['log'].append(f"{request.POST['name']} - Attempted {request.session['counter']} times!")
    request.session.save()
    return redirect('/leader_board')

def leader_board(request):
    context = {
        "winners_names": request.session['log'],
    }
    return render(request, 'leader_board.html', context)