from django.shortcuts import render
from post.models import Contact, Post
from datetime import date, datetime
from django.contrib import  messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    obj = Post.objects.all()
    print(obj)
    context = {
        'posts': obj
    }
    
    return render (request , 'index.html', context)

def about(request):
    return render (request , 'about.html')
    #return HttpResponse("This is about us")

def service(request):
    return render (request , 'services.html')


'''
When a page is requested, Django creates an HttpRequest object that contains metadata about the request. 
Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function. 
Each view is responsible for returning an HttpResponse object.
'''
def contact(request):
#    print(type(request.POST))
    if request.method=='POST':
       name = request.POST.get('name') # request.POST is a dictionary and .get method is applied to get values
       email = request.POST.get('email')
       phone = request.POST.get('phone')
       msg = request.POST.get('msg')
       contact = Contact(name=name,phone=phone,email=email,msg=msg,date=datetime.today())
       contact.save()
       messages.success(request, 'Congrats! You have been heard !! We"ll reach you shortly.') ## sending alert message
       # Printing request objects available methods , Not related to the project but practice
       print(f"printing request : ",type(request))
       print(f"printing request : ",request.scheme)
       print(f"printing request : ",request.body)
       print(f"printing request : ",request.path)
       print(f"printing request : ",request.path_info)
       print(f"printing request : ",request.method)

    return render (request , 'contact.html')
   # return HttpResponse("This is contact")

def create_blog(request):
    if request.method=='POST':
       title = request.POST.get('title') # request.POST is a dictionary and .get method is applied to get values
       description = request.POST.get('description')
       intro = request.POST.get('intro')
       slug = intro.replace(" ","-")
       print(slug)    
       post = Post(title=title,description=description,slug=slug)
       post.save()
       messages.success(request, 'Your Blog has been Saved')
      
    return render(request, 'create_blog.html',{})
    
def post_details(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request,'post_detail.html',{'post':post})


def registerationPage(request):
    form = UserCreationForm()
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request,"registration.html",context)

def loginPage(request): 
    return render(request,"login.html",{})