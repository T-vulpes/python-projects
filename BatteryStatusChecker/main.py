import psutil  
def format_time(seconds_left):
    minutes, seconds = divmod(seconds_left, 60)  
    hours, minutes = divmod(minutes, 60)  
    return "%d:%02d:%02d" % (hours, minutes, seconds)

battery_info = psutil.sensors_battery()
battery_percentage = battery_info.percent  
remaining_time = format_time(battery_info.secsleft) if battery_info.secsleft != -1 else "Calculating..."  

power_plugged_in = battery_info.power_plugged  

print("Battery Percentage:", battery_percentage, "%")
print("Power Plugged In:", power_plugged_in)
print("Estimated Battery Left:", remaining_time)
