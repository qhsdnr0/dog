from os import EX_TEMPFAIL, name
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
        Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age'],
        )
        # dog = owner.dog_set.create (
        #     name = data['dog_name'],
        #     age = data['dog_age'],
        # )
        return JsonResponse({'MESSAGE' : 'CREATED'}, status = 201)

    def get(self, request) :
        owner_list = []
        dog_list = []
        owners = Owner.objects.all()
        for ownera in owners :      
            owner_list.append(
                {
                    "name" : ownera.name,
                    "email" : ownera.email,
                    "age" : ownera.age,
                    "own_dog" : [{'dog_name' : dog.name, 'dog_age' : dog.age} for dog in Dog.objects.filter(owner=ownera.id)]
                }    
            )
        return JsonResponse({"result" : owner_list}, status = 200)
        

class DogView(View) :
    def post(self, request) :
        data = json.loads(request.body)

        dog = Dog.objects.create(
            name = data['name'],
            age = data['age'],
            owner = Owner.objects.get(pk=data['owner_id'])
        )

        return JsonResponse({'MESSAGE' : 'CREATED'}, status = 201)
        
    def get(self, request) :
        dog_list = []
        dogs = Dog.objects.all()

        for dog in dogs :
            dog_list.append(
                {
                    "name" : dog.name,
                    "age" : dog.age,
                    "owner_name" : Owner.objects.get(pk=dog.owner.id).name,
                    
                }
            )

        return JsonResponse({'result' : dog_list}, status = 200)