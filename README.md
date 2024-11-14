WhatsApp Birthday Message Automation 🎉

This project automates sending birthday wishes to contacts on WhatsApp using Python! 🥳

Overview

Purpose: Automatically sends a personalized birthday message to contacts on their specific birthday.
Libraries: pywhatkit for WhatsApp messaging, dotenv for managing contact details securely, and datetime for date checks.
Environment: Contacts and their information are stored in a .env file for security.

How It Works

Contacts List: Loads contacts from a .env file with each contact's name, phone number, and birthday date.
Date Check: Compares each contact's birthday with today’s date to determine if a message should be sent.
Message Sending: Sends a customized birthday message to any contact whose birthday matches the current date.
