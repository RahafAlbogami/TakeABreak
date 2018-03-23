import webbrowser
import time


def CalculateBreakTime():
	# This Function will take the time from the users and calculate the number of breaks 
	#the user needs in the givin time
	study_hours = int(raw_input("How long you will study today "))
	time_in_minute = study_hours*60 
	no_of_breaks = time_in_minute/50 #it's recomanded to take a break every 50 minutes
	return int(round(no_of_breaks))


print ("This program starts at",time.ctime())

break_count = 0
no_of_breaks = CalculateBreakTime()
while(break_count<no_of_breaks):
	time.sleep(3000)# 50 Min in Sec
	webbrowser.open("https://www.youtube.com/watch?v=Hh9yZWeTmVM")#You Can Change the link 
	break_count+=1
