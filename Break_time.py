import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime());
while(break_count < total_breaks):
    webbrowser.open("https://www.youtube.com/watch?v=_dK2tDK9grQ")
    time.sleep(10)
    break_count += 1
    
