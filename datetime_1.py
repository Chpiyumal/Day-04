import datetime

#Current Date and Time
now = datetime.datetime.now()
print(f"Current datetime: {now}")

#Only current date
today = datetime.date.today()
print(f"Current Date is: {today}")

#Only Current Time
current_time = now.time()
print(f"Current Time is : {current_time}")