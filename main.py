from diary import add_entry, view_entries, search_by_date


def main():
    diary_file = input("Enter diary file name: ").strip()

    if not diary_file:
        diary_file = "diary.txt"

    while True:
        print("\n--- My Diary ---")
        print("1. Add diary entry")
        print("2. View all entries")
        print("3. Search entries by date")
        print("4. Change diary file")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            entry = input("Write your diary entry: ")
            add_entry(diary_file, date, entry)

        elif choice == "2":
            view_entries(diary_file)

        elif choice == "3":
            date = input("Enter date (YYYY-MM-DD): ")
            search_by_date(diary_file, date)

        elif choice == "4":
            diary_file = input("Enter new diary file name: ").strip()
            if not diary_file:
                diary_file = "diary.txt"
            print("Diary file changed to:", diary_file)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()