reference_time = '10:30'  # UTC +00.00 Tuesday

custom_input = int(input())

utc_reference_time = 10.5

if custom_input + utc_reference_time < 0:
    print("Monday")
elif custom_input + utc_reference_time >= 0 and custom_input + utc_reference_time < 24:
    print("Tuesday")
else:
    print("Wednesday")
