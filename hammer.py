# time_number = (int(input("What time is it? (hour only): ")))
# time_ampm = input("AM or PM?: ")
#
# if time_ampm == "AM":
#     if time_number >= 7 and time_number <= 9:
#         print("It's time for breakfast.")
#     elif time_number >= 1 or time_number <= 4:
#         print("Stop, it's Hammer Time.")
# elif time_ampm == "PM":
#     if time_number >= 12 or time_number <= 2:
#         print("It's lunch time.")
# elif time_ampm == "PM":
#     if time_number >= 7 or time_number <= 9:
#         print("It's dinner time.")
# elif time_ampm == "PM":
#     if time_number >= 10 or time_number <= 11:
#         print("Stop, it's Hammer Time.")
# else:
#     print("Not time to eat, wait until later.")

##this is the ideal way to do this, with the split()
time = input("What time is it? HH:AM/PM: ")#or could potentially put the .lower() here
time_split = time.split(":")
hour = int(time_split[0])#zero represents the first selection in the split [AM, PM], 1 represents the PM
meridian = time_split[1].lower() #but it's better here cause this is exactly what you want lowered

if hour in range(7, 10):
    if meridian == "am":
        print("Time for breakfast.")
    else:
        print("It's dinner time.")
elif hour in [12, 1, 2] and meridian == "pm":
    print("It's time for lunch.")
elif hour in range(10, 12) and meridian == "pm" or (hour == 12 or hour in range(1,5) and meridian == "am"):
    print("It's hammer time!")
else:
    print("not time to eat.")
