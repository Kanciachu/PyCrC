sandwich_orders = ["tuna", "cheese and mayo", "ham", "vege", "egg and ham"]

finished_sandwiches = []


while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"{current_sandwich} sandwich finished!")

    finished_sandwiches.append(current_sandwich)

print("finished orders:")
for sandwich in finished_sandwiches:
    print(sandwich)