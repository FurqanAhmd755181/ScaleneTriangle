def is_scalene_triangle(a, b, c):
    if a != b and b != c and a != c:
        return True
    else:
        return False

def main():
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))

    if is_scalene_triangle(a, b, c):
        print("It is a scalene triangle.")
    else:
        print("It is not a scalene triangle.")

if __name__ == "__main__":
    main()
