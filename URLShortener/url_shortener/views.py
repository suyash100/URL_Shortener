from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LongToShort
# Create your views here.
def helloWorld(request):
    return HttpResponse("Hello ! I am great and I am learning Django !!!")

def Home_Page(request):
    #print(request.method)
    context={"Error":False,
    "submitted":False}
    if(request.method=="POST"):
        data=request.POST
        print(data)
        longurl=data['longurl']
        customname=data['custom_name']
        print(longurl,customname)
        #customname=request.build_absolute_uri()+customname
        try:
            obj=LongToShort(long_url=longurl, custom_name=customname)
            obj.save()
            context["submitted"]=True
            context["long_url"]=longurl
            context["custom_name"]=request.build_absolute_uri()+customname
            context["date"]=obj.created_date
            context["visited"]=obj.visit_count
        except:
            context["Error"]=True    

    return render(request, "index.html", context)    

def redirect_url(request, customname):
    #return HttpResponse(customname)
    row=LongToShort.objects.filter(custom_name=customname)
    print(row)
    if len(row)==0:
        return HttpResponse("This endpoint dosen't exist Error!!")
    obj=row[0]
    long_url=obj.long_url
    obj.visit_count+=1
    obj.save()
    return redirect(long_url)
    
def analytics(request):
    rows=LongToShort.objects.all()
    context={
        "rows":rows
    }
    return render(request,"analytics.html",context)



def task(request):
    context = {
        'name': ['Suyash Udchan', 'Varad Unhale', 'Vansh Teppalwar'],
        'company': "Trilogy Innovations"
    }
    return render(request, "task.html", context)

