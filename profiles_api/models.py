from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

#These are the standard base classes you need when overriding the default django user models

#This code is written based on the documentation through: https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None): #this is what django CLI use when creating user
        """Create a new user profile"""
        if not email: #email is empty string or null for example
            raise ValueError('User must have an email address') #exception to catch the error and display the msg

        email = self.normalize_email(email) #Normalizes email addresses by lowercasing the domain portion of the email address.
        user = self.model(email=email, name=name,) #creates a new user model that this manager is describing

        user.set_password(password) #This sets and encrypts the password
        user.save(using=self._db) #Save the user model specifying the database in case there is more than one (best practice)
        return user

    def create_superuser(self, email, name, password): #this is what django CLI use when creating superuser (we cannot allow password to be none here because its an admin)
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password) #use the method above to create a User

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system""" #This is python standard for writing doc strings to describe classes and functions to describe them
    email = models.EmailField(max_length=255, unique=True) #create an email column that is unique for each user
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) #a field for permission system to determine is a user is active or not which allows us to deactivate users if we want in the future
    is_staff = models.BooleanField(default=False) #allows us to change a user to be a staff or not to have access to admin page

    objects = UserProfileManager()

    USERNAME_FIELD = 'email' #A string describing the name of the field on the user model that is used as the unique identifier
    REQUIRED_FIELDS = ['name'] #A list of the additional field names that will be prompted for when creating a user

    def get_full_name(self): #optional
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self): #optional
        """Retrieve short name of user"""
        return self.name

    def __str__(self): #optional (recommended always)
        """Return string representation of our user"""
        return self.email
