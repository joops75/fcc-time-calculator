import math

def format_time(hrs, mins):
  h = str(hrs) if hrs else "12"
  m = str(mins) if mins >=10 else "0" + str(mins)

  return h + ":" + m + " "

def get_am_pm(start_am_pm, mins_tot):
  passes_through_12 = math.floor(mins_tot / (12  * 60))

  flip_am_pm = passes_through_12 % 2 != 0

  new_am_pm = 'AM' if start_am_pm == 'PM' else 'PM'

  return new_am_pm if flip_am_pm else start_am_pm

def get_days_later(start_am_pm, mins_tot):
  plus_mins = 12 * 60 if start_am_pm == 'PM' else 0

  passes_through_24 = math.floor((mins_tot + plus_mins) / (24  * 60))

  return passes_through_24

def num_days_later(start_am_pm, mins_tot):
  passes_through_24 = get_days_later(start_am_pm, mins_tot)

  message = " (next day)" if passes_through_24 == 1 else " (" + str(passes_through_24) + " days later)"

  return message if passes_through_24 else ""

days = [
  'monday',
  'tuesday',
  'wednesday',
  'thursday',
  'friday',
  'saturday',
  'sunday'
]

def get_day(start_day, start_am_pm, mins_tot):
  passes_through_24 = get_days_later(start_am_pm, mins_tot)

  try:
    start_day_index = days.index(start_day.lower())
  except:
    return ""
  
  end_day_index = (start_day_index + passes_through_24) % 7

  return ", " + days[end_day_index][0].upper() + days[end_day_index][1:]

  