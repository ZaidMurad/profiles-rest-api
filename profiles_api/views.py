#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response #used to return responses from APIViews

# Create your views here.

class HelloApiView(APIView): #allows us to define the app logic for our endpoint we assign to this view
    """Test API View"""

    def get(self, request, format=None): #allows us to accept and respond to GET request to our API
        """Returns a list of APIView features"""
        #the request argument is passed in by DRF and contains details of the request made to the API
        #the format argument is used to add format suffix to the end of the endpoint url (we will not use it here)
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    #def POST(self, request, format=):
        """"""
