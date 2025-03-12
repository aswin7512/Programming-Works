import math

def find_angle_MBC(AB, BC):
    # Calculate the length of AC using the Pythagorean theorem
    AC = math.sqrt(AB**2 + BC**2)
    
    # Calculate the angle MBC using arctangent
    angle_MBC = math.degrees(math.atan2(AB, BC))

    return angle_MBC

# Get user input for the lengths of AB and BC
AB = float(input("Enter the length of side AB: "))
BC = float(input("Enter the length of side BC: "))

# Find and print the angle MBC
angle_MBC = find_angle_MBC(AB, BC)
print(f"The angle MBC is: {angle_MBC:.2f} degrees")
