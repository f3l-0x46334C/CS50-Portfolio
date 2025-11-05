def main():
    user_time = input(" - Enter time (24h: HH:MM or 12h: H:MM a.m./p.m.) : ")
    time = (convert(user_time))
    
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    
    
def convert(time):
    #----------ADDITIONAL CHALLANGE FOR 12h FORMAT----------#
    if " " in time:
        hmtime, period = time.split(" ")
        hour, minute = hmtime.split(":")
        period = period.lower().strip()
        
        hour, minute = float(hour), float(minute) / 60

        if period == "a.m.":
            if hour == 12:
                hour = 0
        elif period == "p.m.":
            if hour != 12:
                hour = hour + 12
    #----------ADDITIONAL CHALLANGE FOR 12h FORMAT----------#
    
    else:
        hour, minute = time.split(":")
        hour, minute = float(hour), float(minute) / 60
    return hour + minute
            
if __name__ == "__main__":
    main()
