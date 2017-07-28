#Function in Python
def repeat(s, num, exclaim):
    """
    Returns a space-separated string with 's' repeated 'num' times.
    If exclaim is true, add exclamation marks.
    """
    result = s * num
    if exclaim:
        result = result + '!!!'
    return result
