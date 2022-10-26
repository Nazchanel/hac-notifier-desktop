import requests
import functions


# Creates a session to maintain credentials
session_requests = requests.session()

current_time = functions.getTime()

temp = functions.userInput()

username = temp[0]
password = temp[1]
delay = temp[2]

login_url = 'https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f'

html = functions.login(session_requests, login_url, password, username)
grades_html = html[0]
name_html = html[1]
classes = functions.initializeClasses(grades_html, name_html)

class_names = classes[0]
class_grades = classes[1]
print(class_grades)

class_grades = [str(i) for i in class_grades]


class_grades = [i.replace("%", "") for i in class_grades]

class_grades = [float(i) for i in class_grades]

# For Debugging
print(f"Current Grades at {current_time}:\n")
for i in range(len(class_names)):
    print(f"{class_names[i]}: {class_grades[i]}\n")
