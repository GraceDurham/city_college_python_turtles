for item in range(000, 445, 111):
    print (item,)



total_secs = 7684
hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60

print("hours = ", hours, "mins = ", minutes, "secs = ", secs_finally_remaining)