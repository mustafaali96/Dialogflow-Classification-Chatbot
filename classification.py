import json
import cv2
import numpy as np
from urllib.request import urlopen
import urllib.request
from flask import Flask,jsonify,request

app = Flask(__name__)

# Split all the classes by a new line and store it in variable called rows.
rows = open('synset_words.txt').read().strip().split("\n")

# Splitting by comma after first space is found, grabbing the first element and storing it in a new list.
CLASSES = [r[r.find(" ") + 1:].split(",")[0] for r in rows]

# Print the first 50 processed class labels 
# print(CLASSES[0:50])

# Load the Model Weights.
weights = 'bvlc_googlenet.caffemodel'

# Load the googleNet Architecture.
architecture ='bvlc_googlenet.prototxt' 

# Here we are reading pre-trained caffe model with its architecture using opencv dnn module which accepts only 2 parameters 
net = cv2.dnn.readNetFromCaffe(architecture, weights)

@app.route("/webhook",methods=['GET','POST'])
def webhook():
    data = request.get_json()
    if data['queryResult']['intent']['displayName'] == 'classification':
        url = data['queryResult']['parameters']['url']
        resp = urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        res = imageClass(image)
        return jsonify(res)
    
    elif data['queryResult']['intent']['displayName'] == 'multiClassification':
        url = data['queryResult']['parameters']['url']
        nClass = int(data['queryResult']['parameters']['number'])
        resp = urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        res = nImageClass(image, nClass)
        return jsonify(res)

def imageClass(image):
    blob = cv2.dnn.blobFromImage(image, 1, (224, 224), (104, 117, 123))
    # Passing the blob as input through the network 
    net.setInput(blob)
    Output = net.forward()
    index = np.argmax(Output[0])
    image_class = CLASSES[index] 
    reply = {
             'fulfillmentText': image_class
                  }
    return reply

def nImageClass(image, nClass=5):
    blob = cv2.dnn.blobFromImage(image, 1, (224, 224), (104, 117, 123))
    # Passing the blob as input through the network 
    net.setInput(blob)
    Output = net.forward()
    top_n = np.argsort(Output[0])[::-1][:nClass] 
    image_class = []
    for index in top_n:
       image_class.append(CLASSES[index])
    reply = {
             'fulfillmentText': str(image_class)
                  }
    return reply


if __name__ == '__main__':
    app.run(debug=True)