from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
import json
# Create your views here.
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