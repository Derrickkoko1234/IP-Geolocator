from django.shortcuts import redirect, render
import requests
from requests import get

# Create your views here.


def home(request):
    ip = get('https://api.ipify.org').text
    # print(ip)
    return redirect('/get_ip_data/'+ip)

# My URL https://api.ipgeolocation.io/ipgeo?ip=105.112.44.191&apiKey=a3b2f6eafe1f42eab09fbc46a2e790c7

def get_ip(request):
    if request.method == 'POST':
        gotten_ip = request.POST.get('address')
        return redirect('/get_ip_data/'+gotten_ip)
# my google api = AIzaSyAVjznPSZyM89RLPEMHsoW1raPe9pd3cCE
def get_ip_data(request, ip):
    response = requests.get('https://api.ipgeolocation.io/ipgeo?ip=' + ip + '&apiKey=a3b2f6eafe1f42eab09fbc46a2e790c7')
    user = response.json()
    if request.method == 'POST':
        response = requests.get('https://api.ipgeolocation.io/ipgeo?ip=' + ip + '&apiKey=a3b2f6eafe1f42eab09fbc46a2e790c7')
        user = response.json()
        
    return render(request, 'index.html', {'ip': ip, 'user': user})
