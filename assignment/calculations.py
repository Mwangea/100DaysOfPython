print("Calculate Area, Surface Area, and Volume of a Cuboid")

length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))

area = 2 * (length * width + width * height + height * length)
surface_area = 2 * (length * width + width * height + height * length)
volume = length * width * height

print("\nCuboid Dimensions:")
print(f"Length: {length}")
print(f"Width: {width}")
print(f"Height: {height}")

print("\nCalculations:")
print(f"Area: {area:.2f}")
print(f"Surface Area: {surface_area:.2f}")
print(f"Volume: {volume:.2f}")
