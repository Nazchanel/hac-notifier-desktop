# -*- coding: utf-8 -*-
"""
HAC Test: PENDING

Purpose: Make a program that sends me a desktop notification when grades are updated
"""

import requests
import time
import functions
from plyer import notification

temp = functions.userInput()

username = temp[0]
password = temp[1]
delay = temp[2]

login_url = 'https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f'

for i in range(9999999*9999999):

    current_time = functions.getTime()

    # Creates a session to maintain credentials
    session_requests = requests.session()

    if i == 0:
        html = functions.login(session_requests, login_url, password, username)
        grades_html = html[0]
        name_html = html[1]
        classes = functions.initializeClasses(grades_html, name_html)

        class_names = classes[0]
        class_grades = classes[1]
        class_grades = [float(i) for i in class_grades]
        time.sleep(delay * 60)
        continue

    html = functions.login(session_requests, login_url, password, username)
    grades_html = html[0]
    name_html = html[1]
    classes = functions.initializeClasses(grades_html, name_html)
    _class_grades_ = classes[1]
    class_grades_ = [float(i) for i in _class_grades_]

    is_updated = functions.isUpdated(class_grades, class_grades_)[0]
    index_of_updated = functions.isUpdated(class_grades, class_grades_)[1]

    # Check if a notification needs to be sent
    if is_updated:
        class_grades = class_grades_
        print("Updated")
        notification.notify(
            title='ALERT: Grade Updated',
            message=f"At {current_time}, {class_names[index_of_updated]} was updated to a {class_grades_[index_of_updated]}. The  ",
            app_icon='assets/favicon.ico',
            timeout=10,
        )
    else:
        notification.notify(
            title=f'No change detected',
            message=f"NO change was detected at {current_time}.",
            app_icon='assets/favicon.ico',
            timeout=10,
        )
    # Else send the notification

    time.sleep(delay * 60)
