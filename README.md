# Classification Chatbot 

### Step 1 local Server:
download ngrok for local development: https://ngrok.com/download

### Step 2 Repo Clone:
Clone this repo `git clone https://github.com/mustafaali96/Dialogflow-Classification-Chatbot.git`

### Step 3 Dialogflow: 
Import Dialogflow chatbot *chatbot.zip*

### Step 4 Libraries:
open cmd install req libraries: `pip install -r requirements.txt`

### Step 5 Run:
cmd > python classification.py
cmd > ngrok http 5000 > copy Forwarding URL like "https://cb3d-119-157-84-137.ap.ngrok.io"
open dialogflow Fulfillment enable Webhook enter ngrok URL and /webhook which is app.route > https://cb3d-119-157-84-137.ap.ngrok.io/webhook and save

### Step 6 Test:
copy any image url from google
Dialogflow chat > hi
                > Top 4 classes in the image https://imageio.forbes.com/specials-images/imageserve/5d35eacaf1176b0008974b54/0x0.jpg?format=jpg

