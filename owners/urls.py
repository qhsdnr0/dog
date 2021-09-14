from owners.views import DogView, OwnerView
from django.urls import path, include

urlpatterns = [
    path('owners', OwnerView.as_view()),
    path('owners/dogs', DogView.as_view()),
]
