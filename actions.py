import datetime


def choose_action(action):
    text = "Looking for action..."

    if action == "hello":
        text = hello()
    elif action == "time":
        text = get_time()
    else:
        text = "No action matched!"

    return text


def hello():
    """
    Says "Hello World" to the user
    """
    print('hello action')

    text = "Hello World"
    return text


def get_time():
    """
    Tells the user the current time
    """
    print('time action')

    now = datetime.datetime.now()
    month = month.now
    day = day.now
    year = year.now
    hour = now.hour
    minute = now.minute
    second = now.second
    

    text = "The time is %d/%d/%d, %d:%d:%d:%d" % (month, day, year, hour, minute,second)
    return text
