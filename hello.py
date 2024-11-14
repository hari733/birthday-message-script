import pywhatkit as kit
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# List of contacts with phone numbers (from environment variables)
contacts = [
    {'name': os.getenv('CONTACT_1_NAME'), 'phone': os.getenv('CONTACT_1_PHONE'), 'birthday': os.getenv('CONTACT_1_BIRTHDAY')},
    {'name': os.getenv('CONTACT_2_NAME'), 'phone': os.getenv('CONTACT_2_PHONE'), 'birthday': os.getenv('CONTACT_2_BIRTHDAY')},
    {'name': os.getenv('CONTACT_3_NAME'), 'phone': os.getenv('CONTACT_3_PHONE'), 'birthday': os.getenv('CONTACT_3_BIRTHDAY')},
    # Add more contacts here if needed
]

# Your birthday message (can be personalized)
message_template = 'Happy Birthday, {name}! 🎉🎂 Have a wonderful day!'

# Loop through each contact and send a message
for contact in contacts:
    # Personalize the message
    message = message_template.format(name=contact['name'])
    
    # Get the phone number
    phone_number = contact['phone']
    
    # Use pywhatkit to send a message immediately
    kit.sendwhatmsg_instantly(phone_number, message)
    
    # Add a small delay to avoid issues with message sending and WhatsApp login
    time.sleep(2)  # Adjust the sleep time if necessary

print("All birthday messages sent successfully!")
