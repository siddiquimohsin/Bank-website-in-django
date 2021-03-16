from django.shortcuts import render,redirect
from .models import Register
from .models import Comment
from.models import Deposit
from .models import WithDraw
from .models import Bill
from .forms import Registerform
from .forms import Commentform
from .forms import Depositform
from .forms import WithDrawform
from .forms import Billform
from .tag import sel
def index(request):
    now=sel()
    form=Registerform(initial={'account':sel.a})
    return(render(request, 'registration.html',{'form':form}))

def add_new(request):
    form=Registerform(request.POST)
    form.save()
    return redirect('/show')

def login(request):
    form=Registerform
    return(render(request, 'Login.html',{'form':form}))

def check(request):
    acc=Register.objects.values()
    form=Commentform
    em=request.GET['uname']
    pass1=request.GET['psw']
    eml=[]
    psl=[]
    namel=[]
    for s in acc:
        eml.append(s['Email'])
        psl.append(s['password'])
        namel.append(s['Name'])
    if em in eml and pass1 in psl and eml.index(em)==psl.index(pass1):
        a=namel[eml.index(em)]
        return(render(request, 'home.html',{'form':form}))
    else:
        return(render(request, 'dontshow.html'))

def deposit(request):
    return(render(request,'Deposit.html'))

def comment(request):
    che=Register.objects.values()
    em=request.GET['em']
    acc=request.GET['acc']
    eml=[]
    accl=[]
    for s in che:
        eml.append(s['Email'])
        accl.append(s['account'])

    if em in eml and acc in accl and eml.index(em)==accl.index(acc):
        print('yes')
        form=Commentform(initial={'Name':request.GET['usr'],'Email':em,'comment':request.GET['comment']})
        form.save()
        return (render(request,'sentcomment.html'))
    else:
        print('no')
        return (render(request,'notsendcomment.html'))
