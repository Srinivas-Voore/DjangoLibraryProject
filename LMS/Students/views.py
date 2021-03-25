from django.shortcuts import render,redirect
from .models import Journal
from django.contrib import messages
from .models import Book
from .forms import JournalForm

# Create your views here.

def home(request):
    return render(request,"Students/home.html")

def login(request):
    return render(request,"Students/login.html")

def about(request):
    return render(request,"Students/about.html")

def viewjournals(request):
    return render(request,"Students/viewjournals.html",{'jlist':Journal.objects.all()})

def addjournal(request):
	if request.method == 'POST':
		form = JournalForm(request.POST)
		if form.is_valid():
			form.save()
			jname = form.cleaned_data.get('jname')
			messages.success(request, f'New Book {jname} added in LMS!')
			return redirect('Students-addjournal')
	else:
		form = JournalForm()
	return render(request, 'Students/addjournal.html', {'form': form})