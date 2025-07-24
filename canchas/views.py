from django.shortcuts import render

def test(request):
    
    # Page from the theme 
    return render(request, 'test/index.html')

