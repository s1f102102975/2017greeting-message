from datetime import datetime

def greet(name):
    message = 'Hello, ' + name + '-san!'
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
        message = 'Hello'
    else:
        message = 'Good evening'
    print(message)

greet('Inoue')