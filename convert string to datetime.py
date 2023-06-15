#convert string to DateTime

from datetime import datetime

date="Oct 15 2023 2:58PM"
print(date)

date_time = datetime.strptime(date, "%b %d %Y %I:%M%p")

print(date_time)
print(type(date_time))