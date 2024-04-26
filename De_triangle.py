def is_scalene_triangle(a, b, c):
    print(f"Sides: a = {a}, b = {b}, c = {c}")  # Debugging line
    if a != b and b != c and a != c:
        return True
    else:
        return False
