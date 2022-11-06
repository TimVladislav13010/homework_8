from datetime import datetime, timedelta


USERS = [
    {"name": "name_1", "birthday": datetime(year=2022, month=11, day=5).date()},
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
    {"name": "name_11", "birthday": datetime(year=2022, month=11, day=15).date()},
    {"name": "name_12", "birthday": datetime(year=2022, month=11, day=16).date()}
]

WEEK_DAY = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}


def day_of_week(data_time):
    return WEEK_DAY.get(data_time.weekday())


def get_birthdays_per_week(users):
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
    }

    date_time = datetime.now()
    for _ in range(1, 8):
        one_day = timedelta(days=1)
        date_time += one_day
        day.append(date_time.day)
        month.append(date_time.month)

    for user in USERS:
        day_birthday = user.get("birthday")
        birthday_month = day_birthday.month
        birthday_day = day_birthday.day
        if birthday_month in month and birthday_day in day:
            week_day = day_of_week(day_birthday)
            if week_day in "Monday":
                monday_list.append(user.get("name"))
            if week_day in "Tuesday":
                tuesday_list.append(user.get("name"))
            if week_day in "Wednesday":
                wednesday_list.append(user.get("name"))
            if week_day in "Thursday":
                thursday_list.append(user.get("name"))
            if week_day in "Friday":
                friday_list.append(user.get("name"))
            if week_day in "Saturday":
                saturday_list.append(user.get("name"))
            if week_day in "Sunday":
                sunday_list.append(user.get("name"))

    return result


def print_result(dict_birthday: dict):
    for key, val in dict_birthday.items():
        if len(val) != 0:
            list_name = ", ".join(val)
            print(f"{key}: {list_name}")


if __name__ == "__main__":

    print_result(get_birthdays_per_week(USERS))
