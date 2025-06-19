from django.shortcuts import render, redirect

from ads.forms import AdForm
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
