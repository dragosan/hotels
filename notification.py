
from twilio.rest import Client

class Notification:
     
    def __init__(self,hotel_name,customer_name):

        # Your Account SID from twilio.com/console
        account_sid = "ACd95ddb0d056b56231f5521321ff915a7"
        # Your Auth Token from twilio.com/console
        auth_token  = "d60d41e9693b49685102dcf028df5c5f"

        client = Client(account_sid, auth_token)
        msg="we like to inform you that  reservation is confirmed at hotel: "+hotel_name+' for customer : '+customer_name

        message = client.messages.create(
        to="+201025132059", 
        from_="(207) 292-7442",
        body=(msg))
        
