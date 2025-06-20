from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login

from ads.forms import AdForm, RegisterForm
from ads.models import Ad

#http://127.0.0.1:8000
def ad_list(request):
    ads = Ad.objects.all().order_by('-created_at')
    return render(request, 'ad_list.html', { 'ads' : ads } )

#http://127.0.0.1:8000/add
def ad_create(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    if request.method == 'GET':
        form = AdForm()
        return render(request, 'ad_form.html', {'form' : form})

#http://127.0.0.1:8000/delete/5
def ad_delete(request, id):
    ad = get_object_or_404(Ad, id=id)
    ad.delete()
    return redirect('home')

#http://127.0.0.1:8000/edit/10
def ad_edit(request, id):
    ad = get_object_or_404(Ad, id=id)
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
        return redirect('home')
    if request.method == 'GET':
        form = AdForm(instance=ad)
        return render(request, 'ad_form.html', {'form' : form})
    
#http://127.0.0.1:8000/register
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('home')
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form' : form})