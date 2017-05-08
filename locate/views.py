from django.shortcuts import render
import json
# Create your views here.
from .models import Zone
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse

def ShowZonen(request):
    zone=Zone.objects.all()
    return render_to_response('zonen.html', {"zone": zone})


def showZoneDetail(request):
	zone=Zone.objects.all()
	count = zone.count()
	context = {
			"zone":zone,
			"count":count
			}


	return render_to_response('index.html', context)

def showZonewoTDetail(request):
	zone=Zone.objects.all()
	context = []
	values = {}


	return render_to_response('text.html', {"zone": zone})


def recommend(request,lat,lng):
		import json
		import requests
		var1 = 31.554
		var2 = 74.357
		response = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json"+
		                        "?location=%f,%f" % (var1,var2)+
		                        "&radius=500&types=lodging"+
		                        "&key=AIzaSyAquhljJg2jJkFgELhj0EKk-x8t8f432jg")
		r = response.json()
		new = []
		inside ={"name": "abc",
		         "vicinity": "xyz"}
		for i in range(len(r["results"])):
		    inside["name"] = r["results"][i]["name"]
		    inside["vicinity"] = r["results"][i]["vicinity"]
		    #print("inside",inside,"\n")
		    new.append(inside.copy())
		    #print("new",new,"\n")
		hotel = new
		req = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json"+
		                        "?location=%f,%f" % (var1,var2)+
		                        "&radius=1000&types=amusement_park|aquarium|art_gallery|bar|bowling_alley|casino|museum|shopping_mall|stadium|zoo"+
		                        "&key=AIzaSyAquhljJg2jJkFgELhj0EKk-x8t8f432jg")
		e = req.json()
		new2 = []
		inside2 ={'name': 'abc',
		         'vicinity': 'xyz'}
		for i in range(len(e["results"])):
		    inside2["name"] = e["results"][i]["name"]
		    inside2["vicinity"] = e["results"][i]["vicinity"]
		    #print("inside2",inside2,"\n")
		    new2.append(inside2.copy())
		    #print("new2",new2,"\n")
		poi=new2
		req = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json"+
		                        "?location=%f,%f" % (var1,var2)+
		                        "&radius=1000&types=bakery|bar|cafe|liquor_store|meal_takeaway|night_club|restaurant|shopping_mall"+
		                        "&key=AIzaSyAquhljJg2jJkFgELhj0EKk-x8t8f432jg")
		e = req.json()
		new3 = []
		inside3 ={'name': 'abc',
		         'vicinity': 'xyz'}
		for i in range(len(e["results"])):
		    inside3["name"] = e["results"][i]["name"]
		    inside3["vicinity"] = e["results"][i]["vicinity"]
		    #print("inside3",inside3,"\n")
		    new3.append(inside3.copy())
		    #print("new3",new3,"\n")
		res = new3

		context = {

			"hotel":hotel,
			"poi":poi,
			"res":res

		}
		context = json.dumps(context)


		
		return HttpResponse(context, content_type = 'application/json')

