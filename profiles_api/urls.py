from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name = 'hello-viewset') #used to register a specific viewset with our Router
# the first argument is the name of the url, the 2nd is the viewset we want to register to this url, the 3rd is for retrieving the urls in our Router if we need to do that using the url retrieving function
router.register('profile', views.UserProfileViewSet) # since we provided a queryset in view.py, we don't need a basename here

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), #the as_view here is the standard function that we call to convert our api view class to be rendered by our url
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
