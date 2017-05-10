# Import gcloud
from google.cloud import storage

from oauth2client.client import GoogleCredentials

import picamera

# Setup the camera such that it closes
# when we are done with it.
print("About to take a picture.")
with picamera.PiCamera() as camera:
    camera.resolution = (1280,720)
    camera.capture("/home/pi/travel-snap/WWW.YTS.AG.jpg")
print("Picture taken.")

GOOGLE_APPLICATION_CREDENTIALS = '/home/pi/travel-snap/application_default_credentials.json'
credentials = GoogleCredentials.get_application_default()

# Enable Storage
client = storage.Client('project')

# Reference an existing bucket.
bucket = client.get_bucket('travel-snap.appspot.com')

# Upload a local file to a new file to be created in your bucket.
rBlob = bucket.get_blob('/home/pi/travel-snap/WWW.YTS.AG.jpg')
rBlob.upload_from_filename(filename='WWW.YTS.AG.jpg')
