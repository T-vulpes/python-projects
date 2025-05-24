from collections import Counter
import string

def clean_text(text):
    return ''.join(char for char in text.lower() if char in string.ascii_lowercase)

def is_anagram(text1, text2):
    cleaned1 = clean_text(text1)
    cleaned2 = clean_text(text2)
    result = Counter(cleaned1) == Counter(cleaned2)
    
    if result:
        print(f"✅ '{text1}' and '{text2}' are anagrams.")
    else:
        print(f"❌ '{text1}' and '{text2}' are NOT anagrams.")

is_anagram("Listen!", "Silent")
is_anagram("The eyes", "They see")
is_anagram("Hello", "World")
