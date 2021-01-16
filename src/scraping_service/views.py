from django.shortcuts import render
import datetime

def home(request):
    date = datetime.datetime.now().date()
    name = "Dave"
    _context = {'date': date, 'name': name}
    return render(request, 'home.html', _context)
    
w3schools.com/html/html_forms.asp