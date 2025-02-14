import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request

app = Flask(__name__)

 # Define a route that handles POST requests
@app.route('/createJira', methods=['POST'])
def createJira():
     # The comment's body field in the GitHub payload
     comment_data = request.json.get("comment", {})
     comment_body = comment_data.get("body", "")

     # Check if the body field of the comment is "/jira"
     if comment_body == "/jira":
         print("Condition met. Proceeding with POST request...")

         # Jira API details
         url = "https://namratamansur.atlassian.net/rest/api/3/issue"
         API_TOKEN = "ATATT3xFfGF0GMrqkeOxJnaiaEEQVR6qlJ2GxeloRXRWZa5RoL0rrJLJWyMDw3S2uRRHPZK9FZs-qUY0fMnG5j04pKnysr8u9sY0ucQLopUk0fh07RDN0_HzdQLVco1Rrt9btF_MvOs0zXO7BU259DvN5rWP6FOZVH-N04he1TJ5INQRmoeFhI0=6F305B82"
         auth = HTTPBasicAuth("namratamansur@gmail.com", API_TOKEN)

         headers = {
             "Accept": "application/json",
             "Content-Type": "application/json"
         }

         payload = json.dumps({
             "fields": {
                 "description": {
                     "content": [
                         {
                             "content": [
                                 {
                                     "text": "Kiiyansh project ticket or issue creation",
                                     "type": "text"
                                 }
                             ],
                             "type": "paragraph"
                         }
                     ],
                     "type": "doc",
                     "version": 1
                 },
                 "project": {
                     "key": "KJ"    
                 },
                 "issuetype": {
                     "id": "10009"          
                 },
                 "summary": "create issue",           
             },
             "update": {}
         })

         # POST request to create an issue in Jira
         response = requests.post(url, data=payload, headers=headers, auth=auth)
         print("POST request response:", response.status_code, response.text)

         # Return the response back
         return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
     else:
         print("No matching comment found. POST request will not be made.")
         return json.dumps({"error": "No matching comment found. POST request was not made."}, sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
