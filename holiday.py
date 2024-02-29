#task is to calculate total holiday cost
#create inputs first
#create functions
#print details

def holiday_cost(total_cost): #defined total function to sum all costs
    """ Function to add up all the others """
    print(f"Your total cost for your holiday is {total_cost}")


def plane_cost (destination): #used different cost for each destination
    """ Function to calculate flight cost based on destination"""
    if destination == "Mumbai" or destination == "mumbai" or destination == "MUMBAI":
        print ("Your flight cost is 800")
        return 800
    elif destination == "Dubai" or destination == "dubai" or destination == "DUBAI":
        print ("Your flight cost is 500")
        return 800
    elif destination == "Paris" or destination == "paris" or destination == "PARIS":
        print ("Your flight cost is 250")
        return 800
    elif destination == "Tokyo" or destination == "tokyo" or destination == "TOKYO":
        print ("Your flight cost is 1000")
        return 800
    else:
        input ("We do not offer holidays to that destination, please try again. ")

def hotel_cost (duration):
    """Function calculating total cost of staying"""
    room_rate = (int(duration) * 150) #150 is the base per night cost I am going to use
    print(f"Your hotel cost is {room_rate}")
    return room_rate

def car_rental (wheels):
    """Function calculating total rental cost of car"""
    motor = (int(wheels) * 75) #75 is the daily rental cost I am going to use
    print(f"Your car cost is {motor}")
    return motor


city_flight = input ("Where do you want to go? ")
plane_cost (city_flight)
num_nights = input ("How many nights do you want to stay for? ")
hotel_cost (num_nights)
rental_days = input ("For how many days will you be renting a car? ")
car_rental (rental_days)

PLANE_VALUE = int(plane_cost(city_flight))
hotel_value = int(hotel_cost(num_nights))
car_value = int(car_rental(rental_days))
holiday_cost (PLANE_VALUE + hotel_value + car_value)
