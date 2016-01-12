def distance():#get distance in kilometers 
    try:
        race=int(raw_input("Please enter the distance run in kilometers: "))
    except ValueError:
        print "Invalid input, please input a number for distance"
        distance()
    return race

def time_run():#get the time in (hh:min:ss)
    try:
        time=raw_input("Please enter time (hh:min:ss): ")
        time=time.split(":")
        if len(time)==2:#cheack of one didnot enter hours
            time.insert(0, 0)
        elif len(time)<3 or len(time)>3:
            print "Invalid time entered, Try again"
            time_run() 
        time=int(time[0])+int(time[1])/60.0+int(time[2])/3600.0#convert time to hours
    except ValueError:
        print "Invalid input, please input numbers for hours, minutes and seconds"
        time_run()
    return time

if __name__ == '__main__':
    km=1/1.61#miles in one kilometer
    miles=km*distance()#convert the distance from kilometers to miles
    time=time_run()
    print "The average speed = ",miles/time, "miles per hour"

    
