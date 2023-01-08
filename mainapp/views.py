from django.shortcuts import render

# Create your views here.
#def Home(request):
 #   return render(request,'homepage/index.html')

def Home(request):

  if request.method == 'GET':
        
      if request.user.is_authenticated:
        return render(request,'homepage/index.html')

      else :
        return render(request,'homepage/index.html')

