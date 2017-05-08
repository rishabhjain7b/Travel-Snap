import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='943f9f4e8a5d2e1f3c2e2173c9b368213bd587d0')

data=(json.dumps(visual_recognition.classify(images_url='http://campusghanta.com/wp-content/uploads/2016/03/Ladakh-bike-rental-slides-2014-7.jpg'), indent=2))


print(data)
d = json.loads(data)
val =d["images"]
val=val[0]
val=val['classifiers'][0]
val1=val['classes']
print (val1)
c = []
s = []

for i in val1:
        c.append((i['class']))
        s.append((i['score']))
        
