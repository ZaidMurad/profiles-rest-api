from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission): # BasePermission is the class that DRF provide to make your custom permissions
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj): # gets called everytime a request is made to the api that we assign the permission to. It will return True or False to determine whether the user has the permission to do the change he wanna do
        """Check user is trying to edit their own profile""" # obj is the object we are checking the permissions against
        if request.method in permissions.SAFE_METHODS: # we check the HTTP method being made in the request and see whether its in the safe methods list (like GET -because you don't change the object just see it-)
            return True # allow the request

        return obj.id == request.user.id # check whether the obj being updated matches their authenticated user profile (This returns a Boolean answer)
