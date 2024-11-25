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
    "December"
]

while True:
    date = input("Date: ").strip()
    try:
        month, day, year = date.split("/")
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:
        try:
            former_month, former_day, year = date.split(" ")
            for i in range(len(months)):
                if former_month == months[i]:
                    month = i + 1
            if "," in former_day:
                day = former_day.removesuffix(",")
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            pass
print(f'{year}-{int(month):02}-{int(day):02}')
