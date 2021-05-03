monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "Novmeber",
    "Dec" : "December"
}

print(monthConversions.get("Dec"))
print(monthConversions["Jul"])
print(monthConversions.get("october" , "Not a valid key"))