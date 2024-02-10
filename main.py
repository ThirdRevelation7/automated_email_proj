import smtplib
import datetime as dt
import pandas as pd
import random

my_email = "my_email@gmail.com"
password = "password123"


def send_email():
    with open(random_letter) as letter:
        letter = letter.read()
        personalized_letter = letter.replace("[NAME]", f"{person["name"]}")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{person["email"]}",
            msg=f"Subject: Happy Birthday!!!\n\n{personalized_letter}"
        )


now = dt.datetime.today()
current_month = now.month
current_day = now.day

file_paths = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt"
]

random_letter = random.choice(file_paths)

data = pd.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")

for person in birthdays:
    if person["month"] == current_month and person["day"] == current_day:
        send_email()
    else:
        pass
