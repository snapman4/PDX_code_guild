
#def miles_conversion():
miles_km = 1.60934
miles_ft = 5280
miles_m = 1609.34
miles_miles = 1

#def feet_conversion():
feet_mi = 0.000189394
feet_km = 0.0003048
feet_m = 0.3048
feet_feet = 1

#def kilometer_conversion():
km_mi = 0.621371
km_ft = 3280.84
km_m = 1000
km_kim = 1

#def meter_conversion():
meters_mi = 0.621371
meters_km = 0.001
meters_ft = 3.28084
meters_meters = 1


def user_distance():
    distance = input("Enter a distance: ")
    return float(distance)

#(user_distance())

def user_units():
    units = input("Enter units (miles, feet, kilometers, meters): ").lower()
    return units

#(user_units())

def target_units():
    target = input("Enter target units (miles, feet, kilometers, meters): ").lower()
    return target

#(target_units())

distance = user_distance()
units_to_be_converted = user_units()
convert_to = target_units()

def conversion():
    if units_to_be_converted == "miles":
        if convert_to == "kilometers":
            miles_kilometers = distance * miles_km
            return miles_kilometers
        elif convert_to == "feet":
            miles_feet = distance * miles_ft
            return miles_feet
        elif convert_to == "meters":
            miles_meters = distance * miles_m
            return miles_meters
        else:
            miles_miles = distance * 1
            return miles_miles
    elif units_to_be_converted == "kilometers":
        if convert_to == "miles":
            kilometers_miles = distance * km_mi
            return kilometers_miles
        elif convert_to == "feet":
            kilometers_feet = distance * km_ft
            return kilometers_feet
        elif convert_to == "meters":
            kilometers_meters = distance * km_m
            return kilometers_meters
        else:
            kilometers_kilometers = distance * 1
            return kilometers_kilometers
    elif units_to_be_converted == "feet":
        if convert_to == "miles":
            feet_miles = distance * feet_mi
            return feet_miles
        elif convert_to == "kilometers":
            feet_kilometers = distance * feet_km
            return feet_kilometers
        elif convert_to == "meters":
            feet_meters = distance * feet_m
            return feet_meters
        else:
            feet_feet = distance * 1
            return feet_feet
    elif units_to_be_converted == "meters":
        if convert_to == "miles":
            meters_miles = distance * meters_mi
            return meters_miles
        elif convert_to == "kilometers":
            meters_kilometers = distance * meters_km
            return meters_kilometers
        elif convert_to == "feet":
            meters_feet = distance * meters_ft
            return meters_feet
        else:
            meters_meters = distance * 1
            return meters_meters

conversion = conversion()
print("{} {} converts to {} {}".format(distance, units_to_be_converted, conversion, convert_to))
