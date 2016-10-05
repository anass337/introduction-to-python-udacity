import time
import webbrowser
total_breaks = 3
break_count = 0
print("the program is on at "+ time.ctime() )
while(break_count < total_breaks):
    time.sleep(7200)
    webbrowser.open("https://www.youtube.com/watch?v=T-rFeBsaESU")
    break_count = break_count+1
