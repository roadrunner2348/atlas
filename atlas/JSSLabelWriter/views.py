from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

@login_required
def index(request):
    return render(request, 'JSSLabelWriter/index.html', {})

@login_required
def jss_device_search(request):

    r = requests.get('https://jss-client.keansburg.k12.nj.us:8443/JSSResource/computers/subset/basic')
    return render(request, 'JSSLabelWriter/index.html', {'r':r})
