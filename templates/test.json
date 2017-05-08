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
h = json.dumps(hotel)
poi = json.dumps(poi)
res = json.dumps(res)