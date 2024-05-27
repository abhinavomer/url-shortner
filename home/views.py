from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def index_form(request):
    if request.method == 'POST':
        long_url=request.POST.get('long_url')
        new_url=shorten_url(long_url)
        return render(request, 'new_url.html', {'url': new_url})
    return render(request,'index.html')

def shorten_url(url): 
    # define access token in headers 
    headers = { 
        'Authorization': 'Bearer 30223126010fc37520786e5b06b5634d8095bdf4', 
        # 'Authorization': 'Bearer {TOKEN}', 
        'Content-Type': 'application/json', 
    } 
  
    data_dict = {"long_url": url, "domain": "bit.ly"} 
  
    # convert data_dict to json 
    data = json.dumps(data_dict) 
  
    # getting response which will be in json string 
    response = requests.post( 
        'https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data) 
  
    # convert json string to dict 
    response_dict = json.loads(response.text) 
  
    print(response_dict) 
    return response_dict['link'] 
