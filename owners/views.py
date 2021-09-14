from django.db.models.fields.related import ForeignKey
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views import View
from .models import Dog, Owner
# Create your views here.

class OwnerView(View) :
    def post(self, request) :
        data = json.loads(request.body)
        
        
        owner = Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age'],
        )
        
        
        # dog = owner.dog_set.create (
        #     name = data['dog_name'],
        #     age = data['dog_age'],
        # )
              
        return JsonResponse({'MESSAGE' : 'CREATED'}, status = 201)

class DogView(View) :
    def post(self, request) :
        data = json.loads(request.body)

        dog = Dog.objects.create(
            name = data['name'],
            age = data['age'],
            owner = Owner.objects.get(pk=data['owner_id'])
        )
        

        
        
        return JsonResponse({'MESSAGE' : 'CREATED'}, status = 201)
        