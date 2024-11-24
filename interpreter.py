solve = input("Expreesion: ")
x, y, z = solve.split(" ")
x_new = float(x)
z_new = float(z)
if y == "+":
    print(x_new + z_new)
elif y == "-":
    print(x_new - z_new)
elif y == "*":
    print(x_new * z_new)
else:
    print(x_new / z_new)
