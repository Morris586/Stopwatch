import time

def stopwatch():
    print("Simple stopwatch")
    print("Press 'enter' to start/stop, 'r' to reset an 'q' to quit the stopwatch")

    running = False
    start_time = 0
    elapsed_time = 0

    while True:
        user_input = input("Command: ").lower()
#Start the stopwatch
        if user_input == '':
            if not running: 
                running = True
                start_time = time.time() - elapsed_time
                print("Stopwatch started. ")

            else: 
                #Stop the stopwatch
                running = False

                elapsed_time = time.time() - start_time
                print(f"Stopwatch stopped: Elapsed time:{elapsed_time:.2f} seconds.")

        elif user_input == 'r':
            running = False
            elapsed_time = 0
            start_time = 0

        elif user_input == 'q':
            print("Thank you for your time. Goodbye")

        else:
            print("Invalid command. Press 'enter' to start/stop, 'r' to reset an 'q' to quit the stopwatch")
    

if __name__ == '__main__':
    stopwatch()






                
            

