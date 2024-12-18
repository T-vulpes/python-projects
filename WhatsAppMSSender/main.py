#+90 -  represents Turkey's country code.
#5xx -  is the mobile carrier code (mobile numbers in Turkey).
import os
import time
import pyautogui
import datetime

def send_message_via_whatsapp(phone_number, message, delay=10):
    """
    :param phone_number: Phone number to send ('+905xxxxxxxxx')
    :param message: Text of message to be sent
    :param delay: Waiting time after opening WhatsApp (default 10 seconds)
    """
    os.system("start whatsapp://send?phone=" + phone_number)
    time.sleep(delay) 

    pyautogui.write(message)
    pyautogui.press("enter")

phone_number = input("Enter the recipient phone number (starting with +90):")
message = input("Type the message to send: ")

send_time = input("Enter the time to send the message (in HH:MM format): ")
send_hour, send_minute = map(int, send_time.split(":"))

now = datetime.datetime.now()
send_at = now.replace(hour=send_hour, minute=send_minute, second=0, microsecond=0)

if send_at < now:
    send_at += datetime.timedelta(days=1)

wait_time = (send_at - now).seconds
print(f"Waiting for {wait_time} seconds to send message...")
time.sleep(wait_time)

send_message_via_whatsapp(phone_number, message)
