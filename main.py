from datetime import datetime, timedelta
from calendar import isleap


# Реалізована функція для виведення списку колег яких потрібно привітати з днем народження.
# Функція виводить список колег на тиждень вперед, якщо дивитесь 1 числа то буде виведено список колег з 2-8 число.
# Реалізована перевірка високосного року на (29 лютого) стр. 101-126


USERS = [
    {"name": "name_1", "birthday": datetime(year=2022, month=11, day=5).date()},
    {"name": "name_1*", "birthday": datetime(year=2020, month=2, day=29).date()},
    {"name": "name_1**", "birthday": datetime(year=2022, month=2, day=28).date()},
    {"name": "name_1***", "birthday": datetime(year=2022, month=2, day=27).date()},
    {"name": "name_1****", "birthday": datetime(year=2022, month=2, day=26).date()},
    {"name": "name_11", "birthday": datetime(year=2020, month=2, day=29).date()},  # ДН для високосного рік
    {"name": "name_2", "birthday": datetime(year=2022, month=11, day=6).date()},
    {"name": "name_3", "birthday": datetime(year=2022, month=11, day=7).date()},  # 1 day
    {"name": "name_4", "birthday": datetime(year=2022, month=11, day=8).date()},  # 2 day
    {"name": "name_5", "birthday": datetime(year=2022, month=11, day=9).date()},  # 3 day
    {"name": "name_6", "birthday": datetime(year=2022, month=11, day=10).date()},  # 4 day
    {"name": "name_6*", "birthday": datetime(year=2022, month=11, day=10).date()},  # 4 day
    {"name": "name_6**", "birthday": datetime(year=2022, month=11, day=10).date()},  # 4 day
    {"name": "name_7", "birthday": datetime(year=2022, month=11, day=11).date()},  # 5 day
    {"name": "name_8", "birthday": datetime(year=2022, month=11, day=12).date()},  # 6 day
    {"name": "name_9", "birthday": datetime(year=2022, month=11, day=13).date()},  # 7 day
    {"name": "name_10", "birthday": datetime(year=2022, month=11, day=14).date()},
    {"name": "name_12", "birthday": datetime(year=2022, month=11, day=16).date()}
]  # Список колег

WEEK_DAY = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}  # Список назв днів


def day_of_week(data_time):  # функція для вибору дня тижня
    return WEEK_DAY.get(data_time.weekday())


def get_birthdays_per_week(users):  # функція для пошуку колег у яких дн
    monday_list = []
    tuesday_list = []
    wednesday_list = []
    thursday_list = []
    friday_list = []
    saturday_list = []
    sunday_list = []
    day = []
    month = []

    result = {
        "Monday": monday_list,
        "Tuesday": tuesday_list,
        "Wednesday": wednesday_list,
        "Thursday": thursday_list,
        "Friday": friday_list,
        "Saturday": saturday_list,
        "Sunday": sunday_list
    }  # результат

    date_time = datetime.now()
    date_time_plus = datetime.now()

    # date_time = datetime(year=2022, month=2, day=22)  # для тесту 29 лютого
    # date_time_plus = datetime(year=2022, month=2, day=22)  # для тесту 29 лютого

    for _ in range(1, 8):

        one_day = timedelta(days=1)
        date_time_plus += one_day
        day.append(date_time_plus.day)
        month.append(date_time_plus.month)

    for user in USERS:  # цикл по списку колег

        day_birthday = user.get("birthday")
        birthday_month = day_birthday.month
        birthday_day = day_birthday.day

        if birthday_month in month and birthday_day in day:
            week_day = day_of_week(day_birthday)

            if week_day in result.keys():
                lists = result[week_day]
                lists.append(user.get("name"))

        if not isleap(date_time.year):  # перевірка поточного року якщо не високосний заходимо в середину

            if isleap(day_birthday.year) and day_birthday.day == 29 and day_birthday.month == 2:  # перевірка ДН колеги якщо 29 лютого...

                date_time_22_february = datetime(year=date_time.year, month=2, day=22)
                date_time_28_february = datetime(year=date_time.year, month=2, day=28)

                if date_time_22_february <= date_time <= date_time_28_february:

                    date_time_1_march = datetime(year=date_time.year, month=3, day=1)
                    week_day_1_march = day_of_week(date_time_1_march)

                    if week_day_1_march in result.keys():
                        lists = result[week_day_1_march]
                        lists.append(user.get("name") + " - " + "birthday 29 february")

    return result


def print_result(dict_birthday: dict):  # функція для виведення результату
    for key, val in dict_birthday.items():
        
        if len(val) != 0:
            if key in "Saturday":
                list_name = ", ".join(val)
                print(f"To congratulate in Monday: {list_name}. Birthday people {key}.")

            elif key in "Sunday":
                list_name = ", ".join(val)
                print(f"To congratulate in Monday: {list_name}. Birthday people {key}.")
            
            else: 
                list_name = ", ".join(val)
                print(f"{key}: {list_name}")


if __name__ == "__main__":
    print_result(get_birthdays_per_week(USERS))
