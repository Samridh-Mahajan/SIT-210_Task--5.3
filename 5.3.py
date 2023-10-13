import tkinter as tk
import RPi.GPIO as GPIO
import time

# Define Morse code mappings for letters and numbers
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
}

# GPIO pin for the LED
LED_PIN = 21

# Function to blink the LED using Morse code
def blink_morse_code(word):
    for letter in word.upper():
        if letter == ' ':
            time.sleep(3)  # Pause for 3 units between words
        elif letter in MORSE_CODE_DICT:
            morse_code = MORSE_CODE_DICT[letter]
            for symbol in morse_code:
                if symbol == '.':
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    time.sleep(0.2)  # Dot duration
                elif symbol == '-':
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    time.sleep(0.6)  # Dash duration
                GPIO.output(LED_PIN, GPIO.LOW)
                time.sleep(0.2)  # Pause between symbols
            time.sleep(0.4)  # Pause between letters

# Function to handle the button click event
def on_button_click():
    user_input = entry.get()[:12]  # Get the user input (max 12 characters)
    blink_morse_code(user_input)

# Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

# Create the GUI
root = tk.Tk()
root.title("Morse Code Blinker")

label = tk.Label(root, text="Enter a word (max 12 characters):")
label.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Blink Morse Code", command=on_button_click)
button.pack() 


label3 = tk.Label(root, text="Samridh Mahajan")
label3.pack()
label2 = tk.Label(root, text="2210994834")
label2.pack()

root.mainloop()

# Cleanup GPIO on program exit
GPIO.cleanup()
