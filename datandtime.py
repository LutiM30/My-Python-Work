### 7)Write a program that prints the current time on the screen. (Mandatory)
# from datetime import datetime

# now = datetime.now()

# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)
### 8)Write a program that prints the time in the format given : Day Month Date HH:MM:SS YYYY (Mandatory)
from datetime import datetime

now = datetime.now()

# dd/mm/YY
Day = now.strftime("%d/%m/%Y %H:%M:%S")
print("TODAY =", Day)