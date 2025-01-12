from django.shortcuts import render

def showHomePage(request):
    return render(request, "index.html")
