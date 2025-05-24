from colorama import Fore, Style
import time

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
}

def analyze_word(word):
    print(f"{Fore.CYAN}Word: {word}{Style.RESET_ALL}\n")
    for char in word.upper():
        if char.isalpha():
            ascii_val = ord(char)
            binary_val = format(ascii_val, '08b')
            hex_val = hex(ascii_val)
            morse_val = morse_dict.get(char, "?")
            print(f"{Fore.YELLOW}{char}{Style.RESET_ALL} ➜ "
                  f"ASCII: {Fore.GREEN}{ascii_val}{Style.RESET_ALL} | "
                  f"BIN: {Fore.MAGENTA}{binary_val}{Style.RESET_ALL} | "
                  f"HEX: {Fore.BLUE}{hex_val}{Style.RESET_ALL} | "
                  f"MORSE: {Fore.RED}{morse_val}{Style.RESET_ALL}")
            time.sleep(0.3)

word = input("Enter a word: ")
analyze_word(word)
