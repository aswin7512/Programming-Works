#command based game
started = False
while True:
    command = input("> ").lower()
    if command == 'help':
        print("START - TO START THE CAR")
        print("STOP - TO STOP THE CAR")
        print("QUIT - TO EXIT THE GAME")
    elif command == 'start':
        if started:
            print("CAR ALREADY STARTED...")
        else:
            started = True
            print("CAR STARTED... READY TO GO.")
    elif command == 'stop':
        if started:
            print("CAR STOPPED.")
            started = False
        else:
            print("CAR HAVEN'T STARTED YET...")
    elif command == 'quit':
        print("GAME QUITTED SUCCESSFULLY...")
        break
    else:
        print("I don't understand that...")
