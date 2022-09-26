import re

def add_time(start, duration):

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
  if endHour % 24 != 0:
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
  else:
    endHour = str(endHour)
    pmOrAm = ' ' + 'AM'

  new_time = ''
  new_time =  endHour + ":" + endMin + pmOrAm
  #print(formattedTime)

  return new_time

print(add_time("11:40 AM", "0:25"))
