from django.shortcuts import render, redirect

from .forms import CreatePollForm

# Create your views here.
def home(request):
    context = {}
    return render(request, 'poll/home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = CreatePollForm()

    context = {'form' : form}
    return render(request, 'poll/create.html', context)

def results(request):
    context = {}
    return render(request, 'poll/results.html', context)

def vote(request):
    context = {}
    return render(request, 'poll/vote.html', context)