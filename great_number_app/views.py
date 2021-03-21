from django.shortcuts import render, redirect
import random

def index(request):
    request.session['guess_count'] = 0
    request.session['guess_limit'] = 5
    request.session['num'] = random.randint(1, 100)
    print(f"Code is {request.session['num']}")
    return render(request, 'index.html')

def guessed_num(request):
    if request.session['guess_count'] != request.session['guess_limit']:
        if int(request.POST['num']) < request.session['num']:
            context = {
                "low_num": f"{request.POST['num']} is Too Low!"
            }
            request.session['guess_count'] += 1
            if request.session['guess_count'] == request.session['guess_limit']:
                return render(request, 'try_again.html')
            return render(request, 'low_num.html', context)
        elif int(request.POST['num']) > request.session['num']:
            context = {
                "high_num": f"{request.POST['num']} is Too High!"
            }
            request.session['guess_count'] += 1
            if request.session['guess_count'] == request.session['guess_limit']:
                return render(request, 'try_again.html')
            return render(request, 'high_num.html', context)
        else:
            context = {
                "correct_num": f"Guessed Right!!! {request.POST['num']} was the correct number!",
            }
            request.session['guess_count'] += 1
            return render(request, 'correct_num.html', context)

def log_winner(request):
    if 'log' not in request.session:
        request.session['log'] = []
    request.session['log'].append(f"{request.POST['name']} - Attempted {request.session['guess_count']} times!")
    request.session.save()
    return redirect('/leader_board')

def leader_board(request):
    context = {
        "winners_names": request.session['log'],
    }
    return render(request, 'leader_board.html', context)