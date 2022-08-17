from flask import Flask, request, Response

import os
import json
import requests

app = Flask(__name__)


mytoken="twisterster100"
token=""
# verify callback_url from cloud api side

@app.route("/webhook", methods=["GET"])
def webhooks():
    mode = request.args.get("hub.mode")
    challange = request.args.get("hub.challenge")
    token = request.args.get("hub.verify_token")


    if mode and token:

        if mode == "subscribe" and token == mytoken:
            Response.status(200).send(challange)
        else:
            Response.status(403)


@app.route('/webhook', methods=['POST'])
def webhook():
 
    body_param = request.get_json()

    print(json.dumps(body_param, indent=2))

    if body_param.object:

       print("inside body param")
       if body_param.entry and \
            body_param.entry[0].changes and \
            body_param.entry[0].changes[0].value.messages and \
            body_param.entry[0].changes[0].value.messages[0]:


            phon_no_id = body_param.entry[0].changes[0].value.metadata.phone_number_id
            from_ = body_param.entry[0].changes[0].value.messages[0]
            msg_body = body_param.entry[0].changes[0].value.messages[0].text.body

            print("phone number " + phon_no_id)
            print("from " + from_)
            print("body param " + msg_body)
            
            url = "https://graph.facebook.com/v13.0/"+107633372056139+"/messages?access_token="+token

            payload = {

                "messaging_product": "whatsapp",
                "to": "254741151005",
                "text": {
                                         
                    "body": "Hi.. I'm Prasath, your message is "+msg_body
                       }
            }


            headers = {

               "Content-Type": "application/json"
            }


            response = requests.post(url, data=payload, headers=headers)

            if response.status_code == 200:
                print("Success")
            else:
                print("Error:", response.status_code)

@app.route("/", methods=['GET'])
def index():
     return "Hello this is webhook setup"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
        






