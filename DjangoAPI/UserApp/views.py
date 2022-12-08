from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UserApp.models import User
from UserApp.serializers import UserSerializer

###----------------- API Methods for User screen -----------------###
@csrf_exempt
def UserApi(request,id=0):
    ##------------------------GET------------------------##
    #   returns all data from User table in Json Format
    ##---------------------------------------------------##
    if request.method=='GET':   
        users = User.objects.all()
        users_serializer = UserSerializer(users,many = True)
        return JsonResponse(users_serializer.data, safe = False)

    ##-----------------------POST-----------------------##
    #   Used to insert new record into User Table
    ##--------------------------------------------------##
    elif request.method=='POST':
        user_data=JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)

        if user_serializer.is_valid(): 
            user_serializer.save()     
            return JsonResponse("Added Successfully!",safe = False) # if so then we save into db and return success msg
        return JsonResponse("Failed to Add.",safe =False)

    ##-----------------------PUT-----------------------##
    #   Used to update existing record
    ##-------------------------------------------------##
    elif request.method=='PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(UserId = user_data['UserId'])
        user_serializer = UserSerializer(user,data=user_data)

        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully!",safe = False)
        else: 
            return JsonResponse("Failed to Update.", safe = False)

    ##----------------------DELETE----------------------##
    #   Used to delete an existing record
    ##--------------------------------------------------##
    elif request.method=='DELETE':
        user = User.objects.get(UserId=id)
        user.delete()
        return JsonResponse("Deleted Successfully!",safe=False)
        
