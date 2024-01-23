def calculate_square_area(side_length):
    """
    Calculate the area of a square.

    This function takes the length of one side of a square as input
    and returns the area of the square.

    Parameters:
    - side_length (float): The length of one side of the square.

    Returns:
    float: The area of the square.

    Example:
    >>> side_length = 5.0
    >>> calculate_square_area(side_length)
    25.0
    """
    area = side_length ** 2
    return area
