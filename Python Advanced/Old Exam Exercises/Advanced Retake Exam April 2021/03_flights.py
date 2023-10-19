def flights(*args):
    flight_info = {}
    previous = None

    for arg in args:

        if arg == "Finish":
            break

        if type(arg) == int and previous:
            flight_info[previous] += arg        # arg will be the number of passengers in this case
            previous = None

        else:
            flight_info[arg] = flight_info.get(arg, 0)
            previous = arg

    return flight_info








print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))




