import datetime

#Timezone aware Date-Time, using timezone class
#UTC offset +5:30 for SriLanka

sri_lanka_offset = datetime.timezone(datetime.timedelta(hours=5, minutes=30), )
now_sri_lanka = datetime.datetime.now(sri_lanka_offset)
print(f"Current datetime in Sri Lanka {now_sri_lanka}")