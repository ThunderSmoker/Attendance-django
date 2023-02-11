from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student,Batch
import json
import pymongo
# Create your views here.


#mongo db connection
# from pymongo import MongoClient
# import pymongo
# client = pymongo.MongoClient("mongodb://localhost:27017/")

# # Get a reference to the database
# db = client["test_database"]

# # Get a reference to a collection
# collection = db["test_collection"]



@csrf_exempt
def home(req):
    return HttpResponse("HELLO WORLD")
@csrf_exempt
def attend(req):
    if req.method=="POST":
        body=req.body.decode('utf-8')
        body=json.loads(body)
        stud=Student()
        stud.date=body['date']
        stud.prn=body['prn']
        stud.present=body['present']
        stud.batch=body['batch']
        stud.sub=body['sub']
        stud.save()
        data={
            "success":True
        }
        return  JsonResponse(data,safe = False)
    else:
        return JsonResponse({"success":False})

@csrf_exempt
def delete_attendance(req):
    if req.method=="POST":
        body=req.body.decode('utf-8')
        body=json.loads(body)
        stud=Student.objects.get(prn=body['prn'])
        print(stud)
        stud.delete()
        data={
            "success":True
        }
        return  JsonResponse(data,safe = False)

@csrf_exempt
def update_attendance(req):
    if req.method=="POST":
        body=req.body.decode('utf-8')
        body=json.loads(body)
        stud=Student.objects.get(prn=body['prn'])
        stud.date=body['date']
        stud.present=body['present']
        stud.batch=body['batch']
        stud.sub=body['sub']
        print(stud)
        stud.save()
        data={
            "success":True
        }
        return  JsonResponse(data,safe = False)

@csrf_exempt
def get_attendance(req):
    if req.method=="GET":
        stud=list(Student.objects.values())
        data={
            "data":stud
        }
        return  JsonResponse(data,safe = False)


@csrf_exempt
def getbatch(req):
    if req.method=="POST":
        body=json.loads(req.body.decode("utf-8"))
        print(body)
        batc=list(Batch.objects.filter(batch=body['batch']).values())
        data={
            "data":batc
        }
        return  JsonResponse(data,safe = False)
