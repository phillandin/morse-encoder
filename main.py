# -*- coding:utf-8 -*-
import time

# source for morse code: https://www.electronics-notes.com/articles/ham_radio/morse_code/characters-table-chart.php
morse_dict = {
    'A': '·_', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': ' / ',
    "'": '.----.', '!': '-.-.--'
}
print("Welcome to")
time.sleep(.5)
print("█▀▄▀█ █▀▀█ █▀▀█ █▀▀ █▀▀ 　 █▀▀ █▀▀█ █▀▀▄ █▀▀ 　 █▀▀ █▀▀▄ █▀▀ █▀▀█ █▀▀▄ █▀▀ █▀▀█\n"
      "█ ▀ █ █  █ █▄▄▀ ▀▀█ █▀▀ 　 █   █  █ █  █ █▀▀ 　 █▀▀ █  █ █   █  █ █  █ █▀▀ █▄▄▀\n"
      "▀   ▀ ▀▀▀▀ ▀ ▀▀ ▀▀▀ ▀▀▀ 　 ▀▀▀ ▀▀▀▀ ▀▀▀  ▀▀▀ 　 ▀▀▀ ▀  ▀ ▀▀▀ ▀▀▀▀ ▀▀▀  ▀▀▀ ▀ ▀▀")
time.sleep(1)
while True:
    message = input("Please enter your message to encode.\n  ").upper()
    time.sleep(.5)
    try:
        char_list = [morse_dict[letter] for letter in message]
        encoded_message = " ".join(char_list)
        print(f"\nYour message in morse code:\n  {encoded_message}")
    #     inform user of invalid character
    except KeyError as e:
        print(f"\nThe character '{e.args[0]}' is not an option for translating into Morse Code.\n")
    else:
        time.sleep(2)
        again = input("\nWould you like to encode another message? (Y/N)\n  ")
        if again.upper() == "N":
            print("\nThank you for using the morse code encoder.")
            break



