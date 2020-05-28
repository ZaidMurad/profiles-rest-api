#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response #used to return responses from APIViews
from rest_framework import status #it is a list of handy HTTP status codes that you can use when returning responses from your api
from . import serializers
# Create your views here.

class HelloApiView(APIView): #allows us to define the app logic for our endpoint we assign to this view
    """Test API View"""
    serializer_class = serializers.HelloSerializer #this is used to tell our apiview what data to expect when making post, put and patch requests

    def get(self, request, format=None): #allows us to accept and respond to GET request to our API
        """Returns a list of APIView features"""
        #the request argument is passed in by DRF and contains details of the request made to the API
        #the format argument is used to add format suffix to the end of the endpoint url (we will not use it here)
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ] # a list that describes all of the features of an APIView (just for demonstration)

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data) #retrieve the serializer and pass in the data sent in the request

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None): # the pk is to take the id of the object to be updated with the put request
        """handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Deletes an object"""
        return Response({'method': 'DELETE'})
