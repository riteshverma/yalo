
# Online IDE - Code Editor, Compiler, Interpreter
import requests
import time 

def get_bank_messages(url):

    authorization_string = 'Bearer 
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDMxNDM3ODMsImlzcyI6InBzVFBMU0VPeWdEWmdTOFE2UEswSjlHMlRiV1RFVjZjIn0.O3wfDR0PFDPzlXOjpb9ax7FQVdRuq_Y0VJaYMFcLJyU
    '
    headers_dict = {'Content-type': 'application/json' , 'Authorization' : authorization_string}
    request_body = '{
        "recipient_type": "individual",
        "to": "<phone>",
        "type": "text",
        "text": {
            "body": "Hello, your code is: *<code>*"
        }
    }'
    
    response = requests.post(url, data : request_body, headers = headers_dict)
    return response.status_code
 msx = 20
 i = 0 

start_time = time.time()
while ((time.time() - start_time) < 60 and  (i < max))
    url = "https://api-staging2.yalochat.com/awesome-bank/v1/messages"
    status_code = get_bank_messages(url)
    if status_code = '429':
        break
    i++
    


