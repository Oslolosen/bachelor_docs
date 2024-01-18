import numpy as np

def calculate_circumference(radius):
    """
    Calculates the circumference of a circle given its radius.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The circumference of the circle.
    """
    return 2 * np.pi * radius

def calculate_diameter(radius):
    """
    Calculates the diameter of a circle given its radius.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The diameter of the circle.
    """
    return 2 * radius

def calculate_area(radius):
    """
    Calculates the area of a circle given its radius.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return np.pi * radius ** 2
