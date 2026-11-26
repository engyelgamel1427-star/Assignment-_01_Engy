def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        date_str = input("Date: ").strip()

        try:
            if "/" in date_str:
                parts = date_str.split("/")
                if len(parts) != 3:
                    continue
                month = int(parts[0])
                day = int(parts[1])
                year = int(parts[2])
            elif "," in date_str:
                month_part, year_part = date_str.split(",")
                month_name, day_str = month_part.strip().split()
                month_name = month_name.capitalize()
                if month_name not in months:
                    continue
                month = months.index(month_name) + 1
                day = int(day_str.strip())
                year = int(year_part.strip())
            else:
                continue

            if not (1 <= month <= 12 and 1 <= day <= 31 and year >= 0):
                continue

            print(f"{year:04d}-{month:02d}-{day:02d}")
            break
        except ValueError:
            pass


if __name__ == "__main__":
    main()
