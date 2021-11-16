from google.cloud import vision
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="cache/pyvision-331611-767b74d9e10c.json"

image_uri = 'https://i.redd.it/upt6ik778cy71.jpg'
# image_uri = 'https://i.redd.it/jxmramvjb8y71.png'

client = vision.ImageAnnotatorClient()
image = vision.Image()
image.source.image_uri = image_uri

# print(help(client.label_detection))
# response = client.label_detection(image=image, max_results=20)

# print('Labels (and confidence score):')
# print('=' * 30)
# for label in response.label_annotations:
#     print(label.description, '(%.2f%%)' % (label.score*100.))