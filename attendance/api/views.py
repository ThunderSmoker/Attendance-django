from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student,Batch
import json
# Create your views here.
arr=[
    {
      "id": 1,
      "batch": "s4",
      "prn": 21510051
    },
    {
      "id": 2,
      "batch": "s4",
      "prn": 21510052
    },
    {
      "id": 3,
      "batch": "s4",
      "prn": 21510053
    },
    {
      "id": 4,
      "batch": "s4",
      "prn": 21510054
    },
    {
      "id": 5,
      "batch": "s4",
      "prn": 21510055
    },
    {
      "id": 6,
      "batch": "s4",
      "prn": 21510056
    },
    {
      "id": 7,
      "batch": "s4",
      "prn": 21510057
    },
    {
      "id": 8,
      "batch": "s4",
      "prn": 21510058
    },
    {
      "id": 9,
      "batch": "s4",
      "prn": 21510060
    },
    {
      "id": 10,
      "batch": "s4",
      "prn": 21510062
    },
    {
      "id": 11,
      "batch": "s4",
      "prn": 21510063
    },
    {
      "id": 12,
      "batch": "s4",
      "prn": 21510064
    },
    {
      "id": 13,
      "batch": "s4",
      "prn": 21510065
    },
    {
      "id": 14,
      "batch": "s4",
      "prn": 21510066
    },
    {
      "id": 15,
      "batch": "s4",
      "prn": 21510067
    },
    {
      "id": 16,
      "batch": "s4",
      "prn": 21510068
    }
  ]

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
        if len(list(Student.objects.filter(date=body['date'],sub=body['sub'],batch=body['batch'],prn=body['prn']).values()))!=0:
            stud=Student.objects.get(prn=body['prn'])
            stud.present=body['present']
            stud.save()
            print(stud.present)
            return JsonResponse({"msg":"already attended"})
        else:
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
    if req.method=="POST":
        body=json.loads(req.body.decode("utf-8"))
        stud=list(Student.objects.filter(date=body['date'],sub=body['sub'],batch=body['batch']).values())
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
