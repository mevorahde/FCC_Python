# 17th Excise: Dictionaries
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw

# App that will convert short aberration to the full spelling of the months
# I.E. Mar --> March
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

# If I call the key, it should output the value that is associated with the key
print(month_conversions["Nov"])
# Another way to get a value to a key
print(month_conversions.get("Dec"))

# dictionaries can also have number keys
month_number_conversions = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

print(month_number_conversions[2])
print(month_number_conversions.get(6))