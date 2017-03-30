import datetime
import math


def eod():
    """Calculate the minutes until the end of the day"""
    # Get the difference between now and the end of the day
    now = datetime.datetime.now()
    eod = datetime.datetime.now().replace(hour=17, minute=30, second=00)
    diff = eod - now
    # Turn it into minutes, including fractions
    minutes = float(diff.seconds) / 60.0
    # Round up and return without fractions
    print "%d" % math.ceil(minutes)
