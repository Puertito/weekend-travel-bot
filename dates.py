from datetime import date, timedelta


def next_weekends(count=4):
    today = date.today()

    # Пятница = 4
    days_until_friday = (4 - today.weekday()) % 7

    if days_until_friday == 0:
        days_until_friday = 7

    first_friday = today + timedelta(days=days_until_friday)

    weekends = []

    for i in range(count):

        friday = first_friday + timedelta(days=i * 7)

        sunday = friday + timedelta(days=2)

        weekends.append(
            (
                friday.strftime("%Y-%m-%d"),
                sunday.strftime("%Y-%m-%d"),
            )
        )

    return weekends


if __name__ == "__main__":

    for friday, sunday in next_weekends():

        print(friday, sunday)