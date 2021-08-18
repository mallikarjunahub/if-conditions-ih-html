from django.shortcuts import render

# Create your views here.
d={'a':10,'b':100,'c':1000}
def hai(request):
    return render(request, 'hai.html',d)