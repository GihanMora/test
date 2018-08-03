from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('''<html>
    
    <h1>new app</h1>
    dsasasa
    <script>
function receiveMessage(event)
{
  
  
  event.source.postMessage("hi there yourself!  the secret response " +"is: rheeeeet!",event.origin);
}

window.addEventListener("message", receiveMessage, false);
    </script>
    
    </html>
    ''')
