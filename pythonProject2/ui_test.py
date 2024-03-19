import PySimpleGUI as sg
import tkinter
import customtkinter
import datetime

filename="journal.txt"
# System settings
#from journal_vl import add_entry
def add_entry(filename, inp_str):
    # Attempts to locate the file journal.txt
    try:
        with open(filename, "a") as file:  # Tried to read the file journal.txt, if it exist but creates one if it doesnt
            # Get the current date and time
            now = datetime.datetime.now()
            date_str = now.strftime("%m/%d/%Y %I:%M %p")  # Cheatsheet for date time https://strftime.org/

            # User will be asked to put in an entry
            content = inp_str
            entry = f"\nDate: {date_str}\n{content}\n---"

            # File is written to the journal.txt
            file.write(entry)
            print("Entry added successfully.")
    except Exception as e:  # fails to find or create the file journal.txt
        print(f"An error occurred: {e}")


def main():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    # app frame
    app = customtkinter.CTk()
    app.geometry("720x480")
    app.title("New Window")

    # UI Elements
    title = customtkinter.CTkLabel(app, text="User Journal")
    title.pack(padx = 10, pady = 10)

    # Input
    entry_str = tkinter.StringVar()
    entry = customtkinter.CTkEntry(app, width=250, height=20, textvariable=entry_str)
    entry.pack()

    # Button
    enter = customtkinter.CTkButton(app, text="Enter New Journal Entry", command=add_entry(filename, entry_str))
    enter.pack(padx=20, pady= 10)

    app.mainloop()
# run app
main()   # Runs the main function
