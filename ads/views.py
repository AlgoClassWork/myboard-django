from django.shortcuts import render

from ads.models import Ad

# Create your views here.
def ad_list(request):
    ads = Ad.objects.all().order_by('-created_at')
    return render(request, 'ad_list.html', { 'ads': ads } )