from datetime import datetime


USERS = [
    {"name": "name_1", "birthday": datetime(year=2022, month=11, day=5).date()},
    {"name": "name_2", "birthday": datetime(year=2022, month=11, day=6).date()},
    {"name": "name_3", "birthday": datetime(year=2022, month=11, day=7).date()},
    {"name": "name_4", "birthday": datetime(year=2022, month=11, day=8).date()},
    {"name": "name_5", "birthday": datetime(year=2022, month=11, day=9).date()},
    {"name": "name_6", "birthday": datetime(year=2022, month=11, day=10).date()},
    {"name": "name_7", "birthday": datetime(year=2022, month=11, day=11).date()},
    {"name": "name_8", "birthday": datetime(year=2022, month=11, day=12).date()},
    {"name": "name_9", "birthday": datetime(year=2022, month=11, day=13).date()},
]

print(USERS)