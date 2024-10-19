from django.shortcuts import render

def view_home(request):
    return render(request, 'home.html')

def view_news(request):
    return render(request, 'news.html')

def view_management(request):
    return render(request, 'management.html')

def view_facts(request):
    return render(request, 'facts.html')

def view_contacts(request):
    return render(request, 'contacts.html')

def view_history(request):
    return render(request, 'history.html')

def view_history_people(request):
    return render(request, 'history_people.html')

def view_history_photos(request):
    return render(request, 'history_photos.html')

def page_not_found(request, exception):
    return render(request, 'news.html')

# Create your views here.
