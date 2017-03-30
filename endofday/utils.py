import datetime
import math


def eod(dt=None):
    """Calculate the minutes until the end of the day"""
    # Get the difference between now and the end of the day
    if dt is None:
        dt = datetime.datetime.now()
    eod = datetime.datetime.now().replace(hour=17, minute=30, second=00)
    diff = eod - dt
    # Turn it into minutes, including fractions
    minutes = float(diff.seconds) / 60.0
    # Round up and return without fractions
    return "%d" % math.ceil(minutes)
