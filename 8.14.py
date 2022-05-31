cars = []

def make_car(manufacturer, model, **info):
    info['manufacturer'] = manufacturer
    info['model'] = model
    cars.append(info)

make_car("subaru","honda")
make_car("mitszubiszi","f5005")
make_car("subaru","impreza")
for car in cars:
    print(car)