
def show_messeges(list):
    for message in list:
        print(message)


def send_messeges(unsended_massages, sended_messeges):
    while unsended_massages:
        current_message = unsended_massages.pop()
        sended_messeges.append(current_message)


messeges = ["kij ci w oko", "twoja stara", "zapalniczka sabotażówka"]
sended_messeges = []


show_messeges(messeges)
send_messeges(messeges,sended_messeges)
show_messeges(sended_messeges)