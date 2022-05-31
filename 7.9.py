sandwich_orders = ["tuna", "pastrami", "cheese and mayo",
                   "pastrami", "ham", "vege",
                   "pastrami", "egg and ham"]

finished_sandwiches = []

print("THE KITCHEN HAS RUN OUT OF PASTRAMI!!!")




while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if(current_sandwich != "pastrami"):

        print(f"{current_sandwich} sandwich finished!")

        finished_sandwiches.append(current_sandwich)

print("finished orders:")
for sandwich in finished_sandwiches:
    print(sandwich)