import re
import math
from format_time import format_time, get_am_pm, num_days_later, get_day

def add_time(start, duration, day = ''):
  start_time = re.match("(\d+):(\d+)\s+(\w{2})", start)
  start_hrs = int(start_time.group(1))
  start_mins = int(start_time.group(2))
  start_am_pm = start_time.group(3)
  start_mins_tot = start_hrs * 60 + start_mins

  add_time = re.match("(\d+):(\d+)", duration)
  add_hrs = int(add_time.group(1))
  add_mins = int(add_time.group(2))
  add_mins_tot = add_hrs * 60 + add_mins

  mins_tot = start_mins_tot + add_mins_tot
  ans_hrs = math.floor(mins_tot / 60) % 12
  ans_mins = mins_tot % 60

  new_time = format_time(ans_hrs, ans_mins)

  new_am_pm = get_am_pm(start_am_pm, mins_tot)

  end_day = get_day(day, start_am_pm, mins_tot)

  days_later = num_days_later(start_am_pm, mins_tot)

  return new_time + new_am_pm + end_day + days_later