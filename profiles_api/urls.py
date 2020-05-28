from django.urls import path
from . import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), #the as_view here is the standard function that we call to convert our api view class to be rendered by our url
]
