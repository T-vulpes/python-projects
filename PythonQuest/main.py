import random
import string
import time

def choose_language():
    print(">>> Which language would you like to play in?")
    print("1. English")
    print("2. Turkish")
    choice = input(">>> Please select a language (1/2): ").strip()
    if choice == '1':
        return 'en'
    elif choice == '2':
        return 'tr'
    else:
        print(">>> Invalid selection. Defaulting to Turkish.")
        return 'tr'

def welcome_message(lang):
    if lang == 'en':
        print(">>> Welcome to Python Hacker's Quest!")
        print(">>> You need to use your Python skills to solve the codes!")
    else:
        print(">>> Python Hacker's Quest'e Hoş Geldiniz!")
        print(">>> Python becerilerinizi kullanarak şifreleri çözmelisiniz!")
    time.sleep(2)

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def ask_for_hint(lang, hint):
    if lang == 'en':
        user_input = input(">>> Do you want a hint? (Y/N): ").strip().lower()
    else:
        user_input = input(">>> İpucu almak ister misin? (E/H): ").strip().lower()
    if user_input == 'e' or user_input == 'y':
        print(f">>> Hint: {hint}")
    else:
        if lang == 'en':
            print(">>> Let's continue then!")
        else:
            print(">>> O zaman devam edelim!")

def give_up(lang, correct_answer, explanation):
    if lang == 'en':
        user_input = input(">>> Do you want to give up? (Y/N): ").strip().lower()
    else:
        user_input = input(">>> Pes etmek ister misin? (E/H): ").strip().lower()
    if user_input == 'e' or user_input == 'y':
        if lang == 'en':
            print(f">>> Correct answer: {correct_answer}")
            print(f">>> How it was solved: {explanation}")
        else:
            print(f">>> Doğru cevap: {correct_answer}")
            print(f">>> Nasıl çözüldü: {explanation}")
        return True
    return False

def first_mission(lang):
    if lang == 'en':
        print("\n>>> Mission 1: Easy Code Solving")
        hint = "The code is encrypted using Caesar cipher. To find the original text, shift the letters backwards."
        explanation = "You found the original text by shifting the encrypted text backwards by {} units using Caesar Cipher."
        encrypted_text_message = "Encrypted text"
        enter_original_text_message = "Solve the cipher and enter the original text"
    else:
        print("\n>>> Görev 1: Kolay Şifre Çözme")
        hint = "Sezar şifrelemesi kullanılarak şifrelenmiştir. Orijinal metni bulmak için şifreyi çözdüğünde harfleri geriye kaydır."
        explanation = "Sezar şifrelemesi kullanarak şifrelenmiş metni {} birim sola kaydırarak orijinal metni buldun."
        encrypted_text_message = "Şifrelenmiş metin"
        enter_original_text_message = "Şifreyi çöz ve orijinal metni gir"
    
    time.sleep(1)
    shift = random.randint(1, 3)
    original_text = "Python"
    encrypted_text = caesar_cipher(original_text, shift)
    print(f">>> {encrypted_text_message}: {encrypted_text}")
    
    ask_for_hint(lang, hint)
    user_input = input(f">>> {enter_original_text_message}: ")
    
    if user_input == original_text:
        if lang == 'en':
            print(">>> Congratulations, you found the correct answer!")
            print(f">>> {explanation.format(-shift)}")
        else:
            print(">>> Tebrikler, doğru cevabı buldunuz!")
            print(f">>> {explanation.format(-shift)}")
    else:
        if give_up(lang, original_text, explanation.format(-shift)):
            return
        else:
            print(">>> Maalesef, cevap yanlış. Tekrar deneyin!")
            first_mission(lang)

def second_mission(lang):
    if lang == 'en':
        print("\n>>> Mission 2: Intermediate Code Solving")
        hint = "The code is encrypted using Caesar cipher. To find the original text, shift the letters backwards."
        explanation = "You found the original text by shifting the encrypted text backwards by {} units using Caesar Cipher."
        encrypted_text_message = "Encrypted text"
        enter_original_text_message = "Solve the cipher and enter the original text"
    else:
        print("\n>>> Görev 2: Orta Seviye Şifre Çözme")
        hint = "Sezar şifrelemesi kullanılarak şifrelenmiştir. Orijinal metni bulmak için şifreyi çözdüğünde harfleri geriye kaydır."
        explanation = "Sezar şifrelemesi kullanarak şifrelenmiş metni {} birim sola kaydırarak orijinal metni buldun."
        encrypted_text_message = "Şifrelenmiş metin"
        enter_original_text_message = "Şifreyi çöz ve orijinal metni gir"
    
    time.sleep(1)
    shift = random.randint(3, 5)
    original_text = "PythonRocks"
    encrypted_text = caesar_cipher(original_text, shift)
    print(f">>> {encrypted_text_message}: {encrypted_text}")
    
    ask_for_hint(lang, hint)
    
    user_input = input(f">>> {enter_original_text_message}: ")
    
    if user_input == original_text:
        if lang == 'en':
            print(">>> Great, you found the correct answer!")
            print(f">>> {explanation.format(-shift)}")
        else:
            print(">>> Harika, doğru cevabı buldunuz!")
            print(f">>> {explanation.format(-shift)}")
    else:
        if give_up(lang, original_text, explanation.format(-shift)):
            return
        else:
            print(">>> Maalesef, cevap yanlış. Tekrar deneyin!")
            second_mission(lang)

def third_mission(lang):
    if lang == 'en':
        print("\n>>> Mission 3: Hard Code Solving")
        hint = "The code is encrypted using Caesar cipher. To find the original text, shift the letters backwards."
        explanation = "You found the original text by shifting the encrypted text backwards by {} units using Caesar Cipher."
        encrypted_text_message = "Encrypted text"
        enter_original_text_message = "Solve the cipher and enter the original text"
    else:
        print("\n>>> Görev 3: Zor Şifre Çözme")
        hint = "Sezar şifrelemesi kullanılarak şifrelenmiştir. Orijinal metni bulmak için şifreyi çözdüğünde harfleri geriye kaydır."
        explanation = "Sezar şifrelemesi kullanarak şifrelenmiş metni {} birim sola kaydırarak orijinal metni buldun."
        encrypted_text_message = "Şifrelenmiş metin"
        enter_original_text_message = "Şifreyi çöz ve orijinal metni gir"
    
    time.sleep(1)
    shift = random.randint(5, 10)
    original_text = "AdvancedPython"
    encrypted_text = caesar_cipher(original_text, shift)
    print(f">>> {encrypted_text_message}: {encrypted_text}")
    
    ask_for_hint(lang, hint)
    
    user_input = input(f">>> {enter_original_text_message}: ")
    
    if user_input == original_text:
        if lang == 'en':
            print(">>> Great, you found the correct answer!")
            print(f">>> {explanation.format(-shift)}")
        else:
            print(">>> Harika, doğru cevabı buldunuz!")
            print(f">>> {explanation.format(-shift)}")
    else:
        if give_up(lang, original_text, explanation.format(-shift)):
            return
        else:
            print(">>> Maalesef, cevap yanlış. Tekrar deneyin!")
            third_mission(lang)

def fourth_mission(lang):
    if lang == 'en':
        print("\n>>> Mission 4: Find the Error in Python Code")
        hint = "There is a missing closing parenthesis in the code."
        explanation = "You corrected the code by adding the missing closing parenthesis."
    else:
        print("\n>>> Görev 4: Python Kodunda Hata Bulma")
        hint = "Kodda eksik bir kapatma parantezi var."
        explanation = "Eksik olan kapatma parantezini ekleyerek kodu düzelttiniz."
    
    time.sleep(1)
    code_snippet = '''
def multiply_numbers(a, b):
    return a * b

result = multiply_numbers(5, 10
print("Çarpım:", result)
'''
    
    print(f">>> Kod parçası:\n{code_snippet}")
    
    ask_for_hint(lang, hint)
    
    user_input = input(">>> Hatalı kısmı buldun mu? Doğru kodu yaz: ")
    
    correct_code = '''
def multiply_numbers(a, b):
    return a * b

result = multiply_numbers(5, 10)
print("Çarpım:", result)
'''
    
    if user_input.strip() == correct_code.strip():
        if lang == 'en':
            print(">>> Congratulations, you fixed the error correctly!")
        else:
            print(">>> Tebrikler, hatayı doğru şekilde düzelttiniz!")
    else:
        if give_up(lang, correct_code, explanation):
            return
        else:
            print(">>> Maalesef, cevap yanlış. Tekrar deneyin!")
            fourth_mission(lang)

def fifth_mission(lang):
    if lang == 'en':
        print("\n>>> Mission 5: Find the Error in Python Code")
        hint = "A colon (:) is missing at the end of the function definition."
        explanation = "You corrected the code by adding the missing colon."
    else:
        print("\n>>> Görev 5: Python Kodunda Hata Bulma")
        hint = "Fonksiyon tanımının sonunda eksik olan iki nokta üst üste işareti (:)."
        explanation = "Kodda eksik iki nokta üst üste işareti bulunuyordu."
    
    time.sleep(1)
    code_snippet = '''
def greet_user(name)
    print("Merhaba, " + name)
    
greet_user("Python")
'''
    
    print(f">>> Kod parçası:\n{code_snippet}")
    
    ask_for_hint(lang, hint)
    
    user_input = input(">>> Hatalı kısmı buldun mu? Doğru kodu yaz: ")
    
    correct_code = '''
def greet_user(name):
    print("Merhaba, " + name)
    
greet_user("Python")
'''
    
    if user_input.strip() == correct_code.strip():
        if lang == 'en':
            print(">>> Congratulations, you fixed the error correctly!")
        else:
            print(">>> Tebrikler, hatayı doğru şekilde düzelttiniz!")
    else:
        if give_up(lang, correct_code, explanation):
            return
        else:
            print(">>> Maalesef, cevap yanlış. Tekrar deneyin!")
            fifth_mission(lang)

def play_game():
    lang = choose_language()
    welcome_message(lang)
    
    first_mission(lang)
    second_mission(lang)
    third_mission(lang)
    fourth_mission(lang)
    fifth_mission(lang)
    
    if lang == 'en':
        print(">>> Congratulations! You have completed all missions!")
    else:
        print(">>> Tebrikler! Tüm görevleri tamamladınız!")

play_game()
