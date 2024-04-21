def find_shirt_size(neck_circumference, chest_circumference, shirt_length, shoulder_width):
    size_chart = {
        "XS": {"shirt_length": (26, 27), "shoulder_width": (14, 14.5)},
        "S": {"shirt_length": (28, 29), "shoulder_width": (16, 16.5)},
        "M": {"shirt_length": (29, 30), "shoulder_width": (16.5, 17)},
        "L": { "shirt_length": (30, 31), "shoulder_width": (17, 17.5)},
        "XL": { "shirt_length": (31, 32), "shoulder_width": (17.5, 18)},
        "XXL": { "shirt_length": (32, 33), "shoulder_width": (18, 18.5)},
        "XXXL": {"shirt_length": (33, 34), "shoulder_width": (18.5, 19)},
    }

    for size, measurements in size_chart.items():
        if (measurements["neck"][0] <= neck_circumference <= measurements["neck"][1] and
            measurements["chest"][0] <= chest_circumference <= measurements["chest"][1] and
            measurements["shirt_length"][0] <= shirt_length <= measurements["shirt_length"][1] and
            measurements["shoulder_width"][0] <= shoulder_width <= measurements["shoulder_width"][1]):
            return size
    
  
    if not (13 <= neck_circumference <= 19.5):
        print("Invalid neck circumference:", neck_circumference)
    if not (30 <= chest_circumference <= 56):
        print("Invalid chest circumference:", chest_circumference)
    if not (26 <= shirt_length <= 34):
        print("Invalid shirt length:", shirt_length)
    if not (14 <= shoulder_width <= 19):
        print("Invalid shoulder width:", shoulder_width)
    
    return None

neck = float(input("Enter neck circumference in inches: "))
chest = float(input("Enter chest circumference in inches: "))
length = float(input("Enter shirt length in inches: "))
shoulder = float(input("Enter shoulder width in inches: "))

# Find shirt size
shirt_size = find_shirt_size(neck, chest, length, shoulder)
if shirt_size:
    print("The shirt size is:", shirt_size)
else:
    print("No matching shirt size found.")