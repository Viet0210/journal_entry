import datetime
import os


def main():
    # file journal.txt will be created or edited
    filename = "journal.txt"

    # Console menu items
    while True:
        print("\nMy Journal")
        print("1. Add Entry")
        print("2. Read Journal")
        print("3. Clear Journal")
        print("4. Exit")
        choice = input("Choose an option: ")

        # User can select one of four options 1, 2, 3, or 4
        if choice == "1":
            add_entry(filename)  # calls the add_entry function
        elif choice == "2":
            read_journal(filename)  # calls the read_journal function
        elif choice == "3":
            clear_journal(filename)  # calls the clear_journal function
        elif choice == "4":
            print("Goodbye!")
            exit()  # exists the application
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


# option 1. Add a new journal entry
def add_entry(filename):
    # Attempts to locate the file journal.txt
    try:
        with open(filename, "a") as file:  # Tried to read the file journal.txt, if it exist but creates one if it doesnt
            # Get the current date and time
            now = datetime.datetime.now()
            date_str = now.strftime("%m/%d/%Y %I:%M %p")  # Cheatsheet for date time https://strftime.org/

            # User will be asked to put in an entry
            print("\nEnter your journal entry:")
            content = input()
            entry = f"\nDate: {date_str}\n{content}\n---"

            # File is written to the journal.txt
            file.write(entry)
            print("Entry added successfully.")
    except Exception as e:  # fails to find or create the file journal.txt
        print(f"An error occurred: {e}")


# option 2. Read all the entries and print it to the console
def read_journal(filename):
    # Attempts to locate the file journal.txt
    try:
        with open(filename, "r") as file:
            print("\nJournal Entries:\n")
            print(file.read())  # Once found, prints the entries to the console
    except Exception as e:  # fails to find the journal.txt
        print(f"An error occurred: {e}")


def clear_journal(filename):
    try:
        os.remove("journal.txt")
        print("Journal cleared successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")



# run the application
if __name__ == "__main__":
    main()  # Runs the main function
