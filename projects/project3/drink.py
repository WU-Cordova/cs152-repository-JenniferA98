
##Menu implementation will be an array



class Drink:
    """Represents a single drink"""

    kind = {}
    size = {"small":12 , "medium":16, "large":20}
    def __init__(self):
        pass

    ## fixed base price based on size and then add a certain amount based on kind
    # array2D for each kind to save amount and quantity