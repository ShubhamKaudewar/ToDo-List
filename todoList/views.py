from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from todoList.models import noteModel
from django.core.mail import send_mail
from datetime import datetime

def homePage(request):
    listNotes = noteModel.objects.all()
    starListNotes = noteModel.objects.filter(noteStar=True)
    notStarListNotes = noteModel.objects.filter(noteStar=False)
    context = {
        'listNotes':listNotes,
        'starListNotes':starListNotes,
        'notStarListNotes':notStarListNotes
    }
    return render(request,'todoList/index.html',context)

def noteAdd(request):
    if request.method == 'POST':
        noteValue = request.POST['noteValue']

        # Creation Date and Time
        if int(datetime.today().strftime('%H')) > 12:
            t = datetime.today().strftime(str(int(datetime.today().strftime('%H'))-12)+':%M PM')
        elif int(datetime.today().strftime('%H')) == 12:
            t = datetime.today().strftime(str(int(datetime.today().strftime('%H')))+':%M PM')
        elif int(datetime.today().strftime('%H')) == 0:
            t = datetime.today().strftime('12:%M AM')
        else:
            t = datetime.today().strftime('%H:%M AM')
        d = datetime.today().strftime('%d/%m/%Y')

        noteModel.objects.create(
            noteValue = noteValue,
            noteCreationDate = d,
            noteCreationTime = t
        )
        return HttpResponse('')

def noteUpdate(request):
    if request.method == 'POST':
        noteID = request.POST['noteID']
        noteValue = request.POST['noteValue']
        noteModel.objects.filter(id=noteID).update(
            noteValue = noteValue
        )
        return HttpResponse('')

def noteDelete(request):
    if request.method == 'POST':
        noteID = request.POST['noteID']
        noteModel.objects.filter(id=noteID).delete()
        return HttpResponse('')

def markStar(request):
    if request.method == 'POST':
        noteID = request.POST['noteID']
        noteModel.objects.filter(id=noteID).update(
            noteStar = True
        )
        return HttpResponse('')

def removeStar(request):
    if request.method == 'POST':
        noteID = request.POST['noteID']
        noteModel.objects.filter(id=noteID).update(
            noteStar = False
        )
        return HttpResponse('')
