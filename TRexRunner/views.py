from django.shortcuts import render

# Create your views here.


def t_rex_runner(request):
    return render(request, "TRexRunner/index.html")