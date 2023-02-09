"""
To use predefined values, put them into tracks requested list except for the starting track and run the program. Enter the starting track and
press F on first track requested.

Otherwise, enter all your values manually via the terminal.
"""

tracks_requested = [10, 50, 150, 11, 30, 23, 3, 5, 2, 3, 45, 122, 34, 12, 12, 1, 1, 12, 2, 3, 24, 4, 5]
order_visited = []


def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\nEnter An Integer\n")


def get_tracks():
    while True:
        response = input("Enter Requested Track [Press F To Finish]: ")
        if response.upper() == "F":
            break
        try:
            tracks_requested.append(int(response))
        except ValueError:
            print("Please only enter an Integer or F")


def SSTF(current_track):
    while tracks_requested:
        order_visited.append(current_track)
        if len(tracks_requested) == 1:
            order_visited.append(tracks_requested[0])
            tracks_requested.pop(0)
        else:
            current_track = (min(tracks_requested, key=lambda suspect: abs(suspect - current_track)))
            tracks_requested.remove(current_track)


def construct_output():
    order_message = ""
    for i, track in enumerate(order_visited):
        order_message += str(track)
        if i != len(order_visited) - 1:
            diff = abs(track - order_visited[i + 1])
            if diff <= 5:
                order_message += " -> "
            elif diff <= 10:
                order_message += " --> "
            elif diff <= 15:
                order_message += " ---> "
            elif diff <= 30:
                order_message += " ----> "
            elif diff <= 40:
                order_message += " -----> "
            else:
                order_message += " ------> "

    print("-" * len(order_message))
    print(f"{'VISITATION ORDER':^{len(order_message)}}")
    print("-" * len(order_message))
    print(order_message)


def start():
    start_track = get_integer_input("Enter starting track: ")
    print()
    get_tracks()
    print("\nStarting Track:", start_track)
    print("Requested Tracks:", tracks_requested, "\n")
    SSTF(start_track)
    construct_output()


start()
