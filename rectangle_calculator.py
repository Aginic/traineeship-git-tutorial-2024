
def get_area_of_rectangle( side_a, side_b):
    return 2 * (side_a + side_b)

def get_perimeter_of_rectangle( side_a, side_b):
    return 2 * (side_a + side_b)

if __name__ == "__main__":
    side_a = 6
    side_b = 8
    area = get_area_of_rectangle(side_a, side_b)
    perimeter = get_perimeter_of_rectangle(side_a, side_b)
    print(f"The area of a {side_a} by {side_b} rectangle is {area}!")
    print(f"The perimeter of a {side_a} by {side_b} rectangle is {perimeter}!")

