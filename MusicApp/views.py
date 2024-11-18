from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def drinks(request):
    return render(request, 'drinks.html')
def events(request):
    return render(request, 'events.html')
def blogs(request):
    return render(request, 'blog.html')
def gallery(request):
    return render(request, 'gallery.html')
def menu(request):
    return render(request, 'menu.html')
def rates(request):
    return render(request, 'rates.html')
def rooms(request):
    return render(request, 'rooms.html')

