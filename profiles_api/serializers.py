from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer): #accepts a name input and then add it to our apiview and use it to test POST functionality
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10) #creates a name field on our serializer that allows you to input text (char input)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta: # used to configure the serializer to point to a specific model in the app
        model = models.UserProfile # specify the connected model
        fields = ('id', 'email', 'name', 'password') # specify a list(tuple) of fields in the model we want to manage through the serializer (fields we want to make accessible in the api, or wanna use to create new model with the serializer)
        extra_kwargs = { # create an exception to the pass field since we only wanna use this when creating user in the app, we dont wanna allow user to retrieve pass hash for security purposes
            'password': { # custom configuration
                'write_only': True, # when you do a GET, you won't see the pass in the response
                'style': {'input_type': 'password'} # so that you won't see the input pass while you type it
            }
        }

    def create(self, validated_data): # overrides the default create function of DRF, since by default the model serializer use the default create function of the object manager, we override it to use our own create_user function so that the password gets created as a hash not clear-text since we already told it to do so by using set_password method in models.py file
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user( # create a new user from user profiles model manager by calling the create_user function defined in the models.py file
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
        )

        return user

    def update(self, instance, validated_data): # because when a user updates their profile, the password field is stored in cleartext, and they are unable to login. So, we need to override the default behaviour of the update() method of DRF ModelSerializer to hash the users password when updating.
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password') #pop() is an inbuilt function in Python that removes and returns a value from the dictionary for the given index value
            instance.set_password(password) # saves password as a hash

        return super().update(instance, validated_data) # to pass the values to the existing default DRF update() method, to handle updating the remaining fields.


#class ProfileFeedItemSerializer(serializers.ModelSerializer):
#    """Serializes profile feed items"""
#
#    class Meta:
#        model = models.ProfileFeedItem
#        fields = ('id', 'user_profile', 'status_text', 'created_on')
#        extra_kwargs = {'user_profile': {'read_only': True}}
