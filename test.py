from twilio.rest import Client 


account_sid = 'ACc9a93827120de9e22ecaccd21610c94d' 
auth_token = '678b849a15cf4d0631e901a2f6af5a97' 
client = Client(account_sid, auth_token) 

def send_msg():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='I love you ❤️❤️❤️',      
                              to='whatsapp:+94711870149' 
                          ) 
 
    print(message.sid)