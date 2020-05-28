from rest_framework import serializers

class HelloSerializer(serializers.Serializer): #accepts a name input and then add it to our apiview and use it to test POST functionality of our apiview
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10) #creates a name field on our serializer that allows you to input text (char input)
