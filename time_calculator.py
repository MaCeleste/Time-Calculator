import re
def add_time(start, duration, day=None):

  #convert start time and duration to seconds
  startTime = re.split(':| ', start)
  startSeconds = int(startTime[0])*3600 + int(startTime[1])*60
  if startTime[2] == 'PM':
    startSeconds = startSeconds + 43200
  duration = re.split(':', duration)
  durationSeconds = int(duration[0])*3600 + int(duration[1])*60

  #calculate end time in seconds

  endTimeSeconds = startSeconds + durationSeconds

  #convert time in seconds to hh:mm:ss and calculate number of days

  endHour = endTimeSeconds // 3600
  numberOfDays = 0
  if endHour // 24 > 0:
    numberOfDays = endHour // 24
    endHour = endHour - (numberOfDays*24)
  endMin = (endTimeSeconds % 3600) // 60


  #convert min to str and apply format

  endMin = str(endMin)
  endMin = endMin.rjust(2, '0')

  #convert hour to AM/PM format and convert it to str

  if endHour > 12:
    endHour = endHour - 12
    endHour = str(endHour)
    pmOrAm = ' ' + 'PM'
  elif endHour == 12:
    endHour = str(endHour)
    pmOrAm = ' ' + 'PM'
  elif endHour == 0:
    endHour = '12'
    pmOrAm = ' ' + 'AM'
  else:
    endHour = str(endHour)
    pmOrAm = ' ' + 'AM'



  daysOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

  #concatenate the parts of the string to create the final output and calculate
  #the day of the week if a third argument is provided
  if day:
    day = day.capitalize()
    if numberOfDays == 0:
      newDay = day
      new_time =  endHour + ":" + endMin + pmOrAm + ', ' + newDay
    if numberOfDays != 0:
      if numberOfDays == 1:
        indexOfDay = daysOfTheWeek.index(day) + 1
        newDay = ', ' + daysOfTheWeek[indexOfDay]
        numberOfDays = ' (next day)'
      else:
        indexOfDay = (daysOfTheWeek.index(day)+ numberOfDays) % 7
        newDay = ', ' + daysOfTheWeek[indexOfDay]
        numberOfDays = ' (' + str(numberOfDays) + ' days later)'
      new_time =  endHour + ":" + endMin + pmOrAm + newDay + numberOfDays
  else:
    if numberOfDays == 0:
      new_time =  endHour + ":" + endMin + pmOrAm
    if numberOfDays != 0:
      if numberOfDays == 1:
        numberOfDays = ' (next day)'
      else:
        numberOfDays = ' (' + str(numberOfDays) + ' days later)'
      new_time =  endHour + ":" + endMin + pmOrAm + numberOfDays




  return new_time

print(add_time("11:40 AM", "0:25"))
print(add_time("3:30 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("2:59 AM", "24:00"))
print(add_time("8:16 PM", "466:02"))
print(add_time("5:01 AM", "0:00"))
print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("8:16 PM", "466:02", "tuesday"))
