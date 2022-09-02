from crypt import methods
from django.shortcuts import render

# Create your views here.
def calculator(request):
    c=''
     
    if request.method=="POST":
        n1=eval(request.POST.get('num1'))
        n2=eval(request.POST.get('num2'))
        opr=request.POST.get('opr')
        if opr=="+":
            c=n1+n2 

        elif opr=="-":
            c=n1-n2 

        elif opr=="*":
            c=n1*n2 

        elif opr=="/":
            c=n1/n2
    
        print(n1,n2,opr) 
        print(c)

        return render(request,"calculator.html",{"c":c})