from owners.views import DogView, OwnerView
from django.urls import path, include

urlpatterns = [
    path('', OwnerView.as_view()),
    path('/dogs', DogView.as_view()),
]
