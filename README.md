# LCD-Marketing-Controller
## Overview

This Python script is designed to control an LCD display connected to a Raspberry Pi for advertising purposes. The project provides a graphical user interface (GUI) built using the Tkinter library to interact with the LCD display.
Features

## The main features of this code include:

    Single Text Display: Users can input a single text message and specify the line number on the LCD where the text should be displayed. Upon clicking the "Display s-text" button, the text will be shown on the specified line.

    Multiple Texts Display: Users can input multiple text messages separated by commas and specify the delay between each message's display. Additionally, users can select the line number for displaying these texts. Clicking the "Display M-texts" button will cycle through the provided texts on the specified line with the specified delay.

    Clearing the LCD: The "Clear LCD" button allows users to clear the LCD display.

    Stop Display: The "Stop Display" button interrupts the display of multiple texts if it's in progress.

## Usage

To use the LCD Marketing Controller:

    Make sure you have Python installed on your Raspberry Pi.
    Connect the LCD display to the Raspberry Pi.
    Run the Python script lcd_marketing_controller.py.
    The graphical user interface will appear, allowing you to interact with the LCD display.
