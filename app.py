from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/webhook',methods = ['GET','POST'])
def webhook():

    data = request.get_json(silent=True)
    if data['queryResult']['intent']['displayName'] == 'image':
        reply = processImage(data)
        return jsonify(reply)

def processImage(data):
    try:
        print(data)  # This will print the payload in the console we need to find our image in the payload.

        #If image is coming in url
        image = data['originalDetectIntentRequest']['payload']['data']['image']['url']

        #If image is uploaded via files param
        image = request.files.get('image')

        reply={
            "fulfillmentText": f"{image}",
        }
    except Exception as e:
        print(e)
    return reply
if __name__ == '__main__':
    app.run(debug=True)