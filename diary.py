from datetime import datetime


def valid_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def add_entry(filename, date, entry):
    if not valid_date(date):
        print("Invalid date. Use YYYY-MM-DD.")
        return

    entry = " ".join(entry.splitlines())

    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{date}: {entry}\n")

    print("Entry saved!")


def view_entries(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            entries = file.readlines()

        if not entries:
            print("No diary entries found.")
        else:
            for entry in entries:
                print(entry.strip())

    except FileNotFoundError:
        print("Diary file not found.")


def search_by_date(filename, date):
    if not valid_date(date):
        print("Invalid date. Use YYYY-MM-DD.")
        return

    try:
        found = False

        with open(filename, "r", encoding="utf-8") as file:
            for entry in file:
                if entry.startswith(f"{date}:"):
                    print(entry.strip())
                    found = True

        if not found:
            print("No entries found for this date.")

    except FileNotFoundError:
        print("Diary file not found.")