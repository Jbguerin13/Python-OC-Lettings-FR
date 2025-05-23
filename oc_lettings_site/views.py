from django.shortcuts import render
from django.http import Http404

def index(request):
    return render(request, 'index.html')

def test_404(request):
    raise Http404("Page de test 404")

def test_500(request):
    # Forcer une erreur 500 en divisant par zéro
    division_by_zero = 1 / 0
    return render(request, 'index.html')
