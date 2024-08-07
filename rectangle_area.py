def get_area_of_rectangle( side_a, side_b):
    return 2 * (side_a + side_b)

if __name__ == "__main__":
    side_a = 5
    side_b = 8
    print(f"The area of a {side_a} by {side_b} rectangle is {get_area_of_rectangle(side_a, side_b)}!")