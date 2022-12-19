from django.shortcuts import render

# Create your views here.
def homehome(request):
    name = 'pratyush'
    return render(request,'home/homehome.html',{
        'name':name
    })

