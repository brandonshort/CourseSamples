##Checks csv file for storms based on either event type or date of occurance
##Date works, but event works best for producing results
##All dates in csv file are in the year 2015

import csv
import datetime

event = "Dense Fog"
def storm_by_event(event):
    data = open("Indiana_Storms.csv", "r")
    events = list(csv.DictReader(data))
    for char in events:
        if char["EVENT_TYPE"] == event:
            print("A", char["EVENT_TYPE"], "happened on", char["BEGIN_DATE_TIME"].split(" ")[0], "in", char["CZ_NAME"], "county.")
            cont = input("Would you like to check another event? Y or N\n")
            if cont == "Y":
                entry = input("Please enter the type of weather you are searching for: ")
                storm_by_event(entry)
            return
    event = input("Please try another event.\n")
    print(event)
    storm_by_event(event)

##storm_by_event(event)

print()

date = datetime.date(2015, 5, 15)
date = date.strftime("%m/%d/%Y").strip("0")
def storm_by_date(date):
    data = open("Indiana_Storms.csv", "r")
    events = list(csv.DictReader(data))
    for char in events:
        if char["BEGIN_DATE_TIME"].split(" ")[0] == date:
            dateHold = datetime.date(int(date[5:9]), int(date[0]), int(date[2:4]))
            print()
            dateFormat = dateHold.strftime("%A the %d of %B Showers and thunderstorms pushed northeast into west-central and southwest Indiana during the evening hours of %b the %dth.")
            print("On", dateFormat, "These storms produced severe winds as they moved northeast into southwest and central Indiana. This was reported in", char["CZ_NAME"],"county.",
                  char["EVENT_NARRATIVE"])
##storm_by_date(date)

print()

EoT = input("Would you like to search by date or by event? ")
while True:
    if EoT.lower() == "event":
        print("Options are Flood, Hail, Thunderstorm Wind, Flash Flood, Winter Weather, Heavy Snow, Ice Storm, Dense Fog, Heavy Rain, Extreme Cold/Wind Chill, Cold/Wind Chill, or Blizzard")
        entry = input("Please enter the type of weather you are searching for: ")
        storm_by_event(entry)
        break
    elif EoT.lower() == "date":
        entry = input("Please enter your date in YYYY/MM/DD format: ")
        entry = entry[5:7] + "/" + entry[8:11] + "/" + entry[:4]
        entry = entry.strip("0")
        storm_by_date(entry)
        break
    else:
        print("That is not a valid selection. Please try again.")
        EoT = input("Would you like to search by date or by event? ")

