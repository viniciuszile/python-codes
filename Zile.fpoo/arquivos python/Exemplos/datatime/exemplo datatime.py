# Timedelta function demonstration 
  
from datetime import datetime, timedelta
  
  
# Using current time

ini_time_for_now = datetime.now()

# printing initial_date
print ("hoje :",ini_time_for_now)
  
# Calculating future dates
# for two years
future_date_after_2yrs = ini_time_for_now + \
                        timedelta(days = 364)
  
future_date_after_2days = ini_time_for_now + \
                         timedelta(days = 2)
  
# printing calculated future_dates
print('future_date_after_2yrs:', str(future_date_after_2yrs))
print('future_date_after_2days:', str(future_date_after_2days))