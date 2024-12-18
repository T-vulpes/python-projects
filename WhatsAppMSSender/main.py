import os
import time
import pyautogui
import datetime

def send_message_via_whatsapp(phone_number, message, delay=10):
    """
    :param phone_number: Phone number to send (ör. '+905xxxxxxxxx')
    :param message: Text of message to be sent
    :param delay: Waiting time after opening WhatsApp (default 10 seconds)
    """
    os.system("start whatsapp://send?phone=" + phone_number)
    time.sleep(delay)  # Uygulamanın açılması ve QR kodun taranması için bekle

    # Mesajı yaz ve gönder
    pyautogui.write(message)
    pyautogui.press("enter")

# Kullanıcıdan veri al
phone_number = input("Alıcı telefon numarasını girin (+90 ile başlayarak): ")
message = input("Gönderilecek mesajı yazın: ")

send_time = input("Mesajın gönderileceği zamanı girin (HH:MM formatında): ")
send_hour, send_minute = map(int, send_time.split(":"))

# Şu anki zamanı kontrol ederek bekle
now = datetime.datetime.now()
send_at = now.replace(hour=send_hour, minute=send_minute, second=0, microsecond=0)

if send_at < now:
    send_at += datetime.timedelta(days=1)

wait_time = (send_at - now).seconds
print(f"Mesaj gönderimi için {wait_time} saniye bekleniyor...")
time.sleep(wait_time)

send_message_via_whatsapp(phone_number, message)
