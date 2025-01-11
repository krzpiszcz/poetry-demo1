from datetime import datetime, timedelta

def run_dt(startdate:datetime, enddate:datetime, holiday_ar):
    # Set initial default variables
    worktiming = [8, 17]
    weekends = [6, 7]
    holidays = holiday_ar
    print(type(holiday_ar))
    
    # Normalize holidays to ensure all are datetime.date objects
    holidays = [datetime.strptime(holiday, "%Y-%m-%d").date() if isinstance(holiday, str) else holiday for holiday in holiday_ar]
    print(f"Holidays normalized: {holidays}")
      
    day_hours = (worktiming[1]-worktiming[0])
    day_minutes = day_hours * 60 # minutes in a work day

    dt_start = startdate    # datetime of start
    dt_end = enddate       # datetime of end
    worktime_in_seconds = 0
    
    if dt_start.date() == dt_end.date():
        # starts and ends on same workday
        full_days = 0
        print("Err: start and end the same")
        return 0        
    elif (dt_end-dt_start).days < 0:
        # ends before start
        print("Err: end before start")
        return 0
    else:
        # start and ends on different days
        current_day = dt_start  # marker for counting workdays
        while not current_day.date() == dt_end.date():
            if current_day.date() in holidays:
              worktime_in_seconds +=1
            current_day += timedelta(days=1)  # next day
    print(holidays, worktime_in_seconds)
    return holidays

def is_holiday(current_day,holidays):
    """
    Returns True if current_day lands on a holiday.
    """
    return current_day.date() in holidays    

def main():
    #run_dt('2024-11-12', '2024-11-15', ['2024-11-12','2024-11-13'])
    start_date = datetime.strptime('2024-11-12', '%Y-%m-%d')
    end_date = datetime.strptime('2024-11-15', '%Y-%m-%d')
    run_dt(start_date, end_date, ['2024-11-12','2024-11-13'])
    
if __name__ == "__main__":
    main()
    
    