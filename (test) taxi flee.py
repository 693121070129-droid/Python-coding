distance = float(input("Enter distance (km): "))

if distance <= 5:
    fare = 40
else:
    fare = 40 + (distance - 5) * 10

print("Fare:", fare, "baht")