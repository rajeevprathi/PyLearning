import webbrowser
import datetime

hour = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)
minute = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59)

try:
    user_time = input("Please enter the time for alarm (format HHMM): ")
    modified_user_time = datetime.datetime.strptime(user_time,"%H%M")
    print(time.strftime(modified_user_time))
except:
    print("Please enter the time in correct format")



"""
while str(user_time) != str(time.strftime("%H:%M")):
    print("Waiting for time to match")
    time.sleep(30)
    
webbrowser.open('https://www.youtube.com/watch?v=aBt8fN7mJNg', new=2)
    """