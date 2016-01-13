from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests

@login_required
def device_search_form(request):
    total = ""
    message = ""
    if request.method == 'POST':
        search_string = request.POST['device_search']
        if search_string == "":
            message = "Search string cannot be blank. Please enter a search string"
            return render(request, 'JSSLabelWriter/device_search_form.html', {'message':message, 'search_string':search_string})
        else:
            url = "JSSResource/computers/match/*" + search_string + "*"
            results = get_jss_data(url)
            if results.status_code == 200:
                results = results.json()
                results = results['computers']
                total = len(results);
                if total == 0:
                    message = "No results. Try a different search string."
                    return render(request, 'JSSLabelWriter/device_search_form.html', {'message':message, 'search_string':search_string})
                else:
                    return render(request, 'JSSLabelWriter/device_search_form.html', {'message':message, 'results':results, 'search_string':search_string, 'total':total})
            else:
                message = "JSS Connection Error, please contact your system administrator."
                return render(request, 'JSSLabelWriter/device_search_form.html', {'message':message, 'search_string':search_string})
    else:
        return render(request, 'JSSLabelWriter/device_search_form.html', {})

@login_required
def label(request, device_id):
    url = 'JSSResource/computers/id/' + device_id
    results = get_jss_data(url)
    if results.status_code == 200:
        results = results.json()
        return render(request, 'JSSLabelWriter/label.html', {'results':results})
    else:
        message = "Record not found. Please try again"
        return render(request, 'JSSLabelWriter/label.html', {'message':message})
def get_jss_data(url):

    url = settings.JSS_URL + url
    headers = {'Accept':"application/json"}
    r = requests.get(url, headers = headers, auth=(settings.JSS_USERNAME, settings.JSS_PASSWORD))
    return r
