electricity = 0
presence = 1
socket = 1
mood = 'Happy'
Time = 0

while presence == 1:
    while electricity == 1:
        while socket == 1:
            if mood == "Happy":
                Time = Time + 3
                print("You can watch television or listen to music for:", Time, "hours.")
            else:
                print("Relax and go to sleep.")
            socket = 0  # To exit the socket loop after one iteration
        else:
            if socket != 1:
                print("Turn on the socket.")
                socket = 1  # Assuming you're simulating turning on the socket
            else:
                print("You can use your phone to stream.")
        electricity = 0  # To exit the electricity loop after one iteration
    else:
        if electricity != 1:
            print("Relax for the power company to restore electricity.")
            electricity = 1  # Assuming you're simulating the restoration of electricity
        presence = 0  # To exit the presence loop after one iteration
else:
    if presence != 1:
        print("Get home first to enjoy the amenities.")