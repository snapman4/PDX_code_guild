time_number = (int(input("What time is it? (hour only): ")))
time_ampm = input("AM or PM?: ")

if time_ampm == "AM":
    if time_number >= 7 and time_number <= 9:
        print("It's time for breakfast.")
    elif time_number >= 1 or time_number <= 4:
        print("Stop, it's Hammer Time.")
elif time_ampm == "PM":
    if time_number >= 12 or time_number <= 2:
        print("It's lunch time.")
elif time_ampm == "PM":
    if time_number >= 7 or time_number <= 9:
        print("It's dinner time.")
elif time_ampm == "PM":
    if time_number >= 10 or time_number <= 11:
        print("Stop, it's Hammer Time.")
else:
    print("Not time to eat, wait until later.")
