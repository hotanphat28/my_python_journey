import calendar


def run():
    year = int(input("Please input the year: "))  # Year
    month = int(input("Please input the month: "))  # Month

    # Display the calendar in month
    print(calendar.month(year, month))

if __name__ == "__main__":
    run()
