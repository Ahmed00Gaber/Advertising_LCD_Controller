import RPi.GPIO as GPIO
import time
from LCD import *
import tkinter as tk
import threading


#function display line
def Line_Display(line,text):
  if line == 1:
      lcd_string(text, LCD_LINE_1)
  elif line == 2:
      lcd_string(text, LCD_LINE_2)
  else:
        lcd_string("Wrong line", LCD_LINE_1)
        
# Function to handle the Apply button click event
def apply_text():
    text = LCD_Entry.get()
    line = int(Line_Entry.get())
    Line_Display(line,text)

# Function to clear the LCD
def clear_lcd():
    lcd_byte(0x01, LCD_CMD)  # Send command to clear the display

# Function to stop displaying multiple texts
def stop_multiple_text():
    global continue_display
    continue_display = False
    clear_lcd()  # Clear the LCD screen

# Function to display multiple texts with delay
'''
Breifly: we used threads to ahndle while loop in another thread
to let the GUI continously work 
'''
def display_multiple_texts(texts, delay, line):
    global continue_display  # Use global variable to control the loop
    continue_display = True
    def display_thread():
        while continue_display:
            for text in texts:
                lcd_string(text, line)
                time.sleep(delay)
                if not continue_display:
                    break
                clear_lcd()
    #code to start a new thread for display thread
    threading.Thread(target=display_thread).start() 

# Function to handle the Display button click event
def display_texts():
    texts = Texts_Entry.get().split(',')  # Get texts separated by comma
    delay = float(Delay_Entry.get())  # Get delay from entry
    line=int(MulLine_Entry.get())
    if line == 1:
      display_multiple_texts(texts, delay,LCD_LINE_1)
    elif line == 2:
      display_multiple_texts(texts, delay,LCD_LINE_2)
    else:
        lcd_string("Wrong line", LCD_LINE_1)
    
# Initialise display
lcd_init()

# Tkinter setup
root = tk.Tk()
root.title("LCD Controller")
root.geometry("500x300")
root.config(bg="lightblue")

# Frame for input fields
input_frame = tk.Frame(root, bg="lightblue")
input_frame.pack(pady=10)

# Label and Entry for LCD text
lcd_text_label = tk.Label(input_frame, text="LCD text:", bg="lightblue")
lcd_text_label.grid(row=0, column=0, padx=5, pady=5)

LCD_Entry = tk.Entry(input_frame, width=30)
LCD_Entry.grid(row=0, column=1, padx=5, pady=5)

# Label and Entry for line number
line_num_label = tk.Label(input_frame, text="Line num:", bg="lightblue")
line_num_label.grid(row=1, column=0, padx=5, pady=5)

Line_Entry = tk.Entry(input_frame, width=10)
Line_Entry.grid(row=1, column=1, padx=5, pady=5)

# Label and Entry for texts
texts_label = tk.Label(input_frame, text="Texts(comma-separated):", bg="lightblue")
texts_label.grid(row=2, column=0, padx=5, pady=5)

Texts_Entry = tk.Entry(input_frame, width=30)
Texts_Entry.grid(row=2, column=1, padx=5, pady=5)

# Label and Entry for Multiple Line
MulLine_label = tk.Label(input_frame, text="Line", bg="lightblue")
MulLine_label.grid(row=3, column=0, padx=5, pady=5)

MulLine_Entry = tk.Entry(input_frame, width=10)
MulLine_Entry.grid(row=3, column=1, padx=5, pady=5)


# Label and Entry for delay
delay_label = tk.Label(input_frame, text="Delay (seconds):", bg="lightblue")
delay_label.grid(row=4, column=0, padx=5, pady=5)

Delay_Entry = tk.Entry(input_frame, width=10)
Delay_Entry.grid(row=4, column=1, padx=5, pady=5)

# Button frame
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=5)

# Button to apply text to LCD
config_button = tk.Button(button_frame, text="Display s-text", command=apply_text, bg="white")
config_button.grid(row=0, column=0, padx=5, pady=5)

# Button to display multiple texts
display_button = tk.Button(button_frame, text="Display M-texts", command=display_texts, bg="white")
display_button.grid(row=0, column=1, padx=5, pady=5)

# Button to clear LCD
clear_button = tk.Button(button_frame, text="Clear LCD", command=clear_lcd, bg="white")
clear_button.grid(row=0, column=2, padx=5, pady=5)

# Button to stop displaying multiple texts
stop_button = tk.Button(button_frame, text="Stop Display", command=stop_multiple_text, bg="white")
stop_button.grid(row=0, column=3, padx=5, pady=5)

root.mainloop()
