from django.shortcuts import render
import requests

url = "http://localhost:4444/predict"

# Create your views here.
def potato_disease_classifcation(request):
    predictions = {}
    if request.method == 'POST' and 'fileup' in request.FILES:
       # Handle the file
       image = request.FILES['fileup']
       # Prepare the files to be sent in the POST request
       print(image)
       files = {'file': image}
       response = requests.post(url,files = files)
       predicted_class = response.json()['class']
       confidence = response.json()['confidence']
       print(confidence)
       predictions = {
           'img' : image,
           'predicted_class': predicted_class,
           'confidence':confidence
       }
    else:
        predictions = {
           'img' : None,
           'predicted_class': None,
           'confidence':None
       }

    return render(request,'form/form.html',predictions)
