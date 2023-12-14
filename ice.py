from icecream import ic

cars=[]

def main():
    while(True):
        ic("a - add a car")
        ic("p - print all cars")
        ic("x - exit")
        user_selection= input("your selection")

        if user_selection == "a": cars.append({"color":input("car color?")})
        if user_selection == "p": ic(cars)
        if user_selection == "x": exit()






if __name__ == "__main__":
    main()

