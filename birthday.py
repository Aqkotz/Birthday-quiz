"""
birthday.py
Author: Andy
Credit: None
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
name = input("Hello, what is your name? ")
birthmonth = input("Hi " + name + ", what was the name of the month you were born in? ")
birthyear = input("And what year were you born in, " + name + "? ")
birthday = input("And the day? ")
leapyear = input("Is it a leapyear? ")

birthyear = int(birthyear)
birthday = int(birthday)
print ("")
if leapyear not in ["Yes", "yes", "no", "No"]:
    print ("Not a valid response for 'is it a leapyear.'")
else:
    if birthmonth not in ["january", "January", "february", "February", "march", "March", "april", "April", "may", "May", "june", "June", "july", "July", "august", "August", "september", "September", "october", "October", "november", "November", "december", "December", "Janember"]:
        print ("Sorry, " + birthmonth + " is not a real month.")
        if birthmonth in ["september", "September", "april", "April", "june", "June", "november", "November"]:
            birthmonthlength = 30
        if birthmonth in ["january", "January", "march", "March", "may", "May", "july", "July", "august", "August", "december", "December", "Janember"]:
            birthmonthlength = 31
        if birthmonth in ["february", "February"] and leapyear in ["no", "No"]:
            birthmonthlength = 28
        if birthmonth in ["february", "February"] and leapyear in ["yes", "Yes"]:
            birthmonthlength = 29
        if birthday > birthmonthlength:
            print ("that is not a valid input for 'And the day?'")
    
    else:
        print ("Hi " + name + ", your birthday is " + birthmonth + " " + str(birthday) + ", " + str(birthyear) +".")
    
        if birthmonth == "january" or "January" or "february" or "February" or "december" or "December":
            birthseason = ("winter")
        if birthmonth == "march" or "March" or "april" or "April" or "may" or "May":
            birthseason = ("spring")
        if birthmonth == "june" or "June" or "july" or "July" or "august" or "August":
            birthseason = ("summer")
        if birthmonth == "september" or "September" or "october" or "October" or "november" or "November":
            birthseason = ("fall")
        if birthmonth == "Janember":
            birthseason = ("stupid")
        if birthday == 31 and (birthmonth == "october" or birthmonth == "October"):
            print ("You were born on Halloween!")
        if birthyear < 1989 and birthyear > 1980:
            print ("you were a " + birthseason + " baby of the eighties")
        if birthyear < 1999 and birthyear > 1990:
            print ("you were a " + birthseason + " baby of the nineties")
        if birthyear < 2009 and birthyear > 2000:
            print ("you were a " + birthseason + " baby of the two thousands")
        if birthyear < 2016 and birthyear > 2014:
            print ("you are a " + birthseason + " baby, and also an infant")
        if birthyear < 1979 and birthyear > 1970:
            print ("you were a " + birthseason + " baby of the seventies")
        if birthyear < 1969 and birthyear > 1960:
            print ("you were a " + birthseason + " baby of the sixties")
        if birthyear < 1959 and birthyear > 1950:
            print ("you were a " + birthseason + " baby of the nineties")

