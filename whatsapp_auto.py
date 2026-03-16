import pywhatkit

# configure the message details
phone_number = "+917827869541"
message = "hello! this an automated message sent using python."
hours = 20
minutes = 8

#logic to send the message
print("the script has started. please wait for a moment..")

    # this fuction opens the browser and sends the message automatically
    
pywhatkit.sendwhatmsg(phone_number,message,hours,minutes)

print("done! browser will open soon.")
    
    
    