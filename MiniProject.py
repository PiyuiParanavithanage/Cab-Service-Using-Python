from doctest import master
from tkinter import *
from PIL import ImageTk,Image
import json
root = Tk()
root.title("PW CAB SERVICE")

# customer function
def customer():
    while True:
            print("\n==========Welcome Customer==========")
            print(".....Available Vehicle Types.....\nCar\nVan\nWheeler\nTruck\nLorry\n")
            VehicleType = input("What is your expected vehicle:- ")

            # check user request vehicle
            if (VehicleType == "Car"):
                while True:
                    Passenger = int(input("How many passengers:- "))
                    # check passenger equal to 3 or 4
                    if (Passenger == 3 or Passenger == 4):
                        print("You Can Choice a Car\nYou Can Choose AC or NonAC\n")
                        break
                    else:
                        print("Please Select Valid Passenger Range(3 or 4)\n")

            elif (VehicleType == "Van"):
                while True:
                    Passenger = int(input("How many passengers:- "))
                    if (Passenger == 3 or Passenger == 4):
                        print("You Can Choice a Van\nYou Can Choose AC or NonAC\n")
                        break
                    else:
                        print("Please Select Valid Passenger Range(3 or 4)\n")
            elif (VehicleType == "Wheeler"):
                print("You Can Choose a 3-Wheeler")
            elif (VehicleType == "Truck"):
                print("Size: 7ft and 12ft\nYou Can Choose a Truck\n")
            elif (VehicleType == "Lorry"):
                print("Max Load & Size: 2500kg and 3500kg\nYou Can Choose a Lorry\n")

# admin function
def admin():
    while True:
        print("\n====================Welcome Admin====================\n")
        print(
            "(1) Add New Vehicle\n(2) Remove Vehicle\n(3) Assign a Vehicle\n(4) Release a Vehicle\n(5) Check Available Vehicles\n(99) EXIT\n")
        mainOption = input("Enter Choice: ")

        # option 99
        if mainOption == '99':
            print("====================Thank You For Join With Us=====================\n")
            break

        # option 01
        elif mainOption == '1':
            Addselection = input("Enter Vehicle Type to Add(Car/Van/Wheeler/Truck/Lorry): ")

            # check selection equal to car or not
            if (Addselection == "Car"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                cars = obj['cars']
                temCars = obj['temCars']
                name = input("Enter the Name: ")
                number = int(input("Enter the Number: "))
                driver = input('Enter the Driver Name: ')
                type = input('Enter the Type: ')

                newDic1 = {
                    'name': name,
                    'number': number,
                    'driver': driver,
                    'type': type
                }
                # add items
                cars.append(newDic1)
                print("==========Vehicle Added Successfully==========\n")
                f.close()

                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

            # check selection equal to van or not
            elif (Addselection == "Van"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                vans = obj['vans']
                temVans = obj['temVans']
                name = input("Enter the Name: ")
                number = int(input("Enter the Number: "))
                driver = input('Enter the Driver Name: ')
                type = input('Enter the Type: ')

                newDic2 = {
                    'name': name,
                    'number': number,
                    'driver': driver,
                    'type': type
                }
                # add items
                vans.append(newDic2)
                print("==========Vehicle Added Successfully==========\n")
                f.close()

                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

            # check selection equal to wheeler or not
            elif (Addselection == "Wheeler"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                wheelers = obj['wheelers']
                temWheelers = obj['temWheelers']
                name = input("Enter the Name: ")
                number = int(input("Enter the Number: "))
                driver = input('Enter the Driver Name: ')

                newDic3 = {
                    'name': name,
                    'number': number,
                    'driver': driver,
                }
                # add items
                wheelers.append(newDic3)
                print("==========Vehicle Added Successfully==========\n")
                f.close()

                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

            # check selection equal to truck or not
            elif (Addselection == "Truck"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                trucks = obj['trucks']
                temTrucks = obj['temTrucks']
                name = input("Enter the Name: ")
                number = int(input("Enter the Number: "))
                driver = input('Enter the Driver Name: ')

                newDic4 = {
                    'name': name,
                    'number': number,
                    'driver': driver,
                }
                # add items
                trucks.append(newDic4)
                print("==========Vehicle Added Successfully==========\n")
                f.close()

                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

            # check selection equal to lorry or not
            elif (Addselection == "Lorry"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                lorries = obj['lorries']
                temLorrys = obj['temLorrys']
                name = input("Enter the Name: ")
                number = int(input("Enter the Number: "))
                driver = input('Enter the Driver Name: ')

                newDic5 = {
                    'name': name,
                    'number': number,
                    'driver': driver,
                }
                # add items
                lorries.append(newDic5)
                print("==========Vehicle Added Successfully==========\n")
                f.close()

                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

        # option 02
        elif mainOption == '2':
            Removeselection = input("Enter Vehicle Type to Remove(Car/Van/Wheeler/Truck/Lorry): ")

            if (Removeselection == "Car"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                cars = obj['cars']
                temCars = obj['temCars']
                for car in cars:
                    print("ID", cars.index(car), " Name:", car['name'], "   Number:", car['number'], "  Driver Name:",
                          car['driver'], "  Type:", car['type'])
                remId1 = int(input("Select the ID: "))
                cars.pop(remId1)
                print("==========Vehicle Removed Successfully==========\n")
                f.close()

                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (Removeselection == "Van"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                vans = obj['vans']
                temVans = obj['temVans']
                for van in vans:
                    print("ID", vans.index(van), " Name:", van['name'], "   Number:", van['number'], "  Driver Name:",
                          van['driver'], "  Type:", van['type'])
                remId2 = int(input("Select the ID: "))
                vans.pop(remId2)
                print("==========Vehicle Removed Successfully==========\n")
                f.close()

                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (Removeselection == "Wheeler"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                wheelers = obj['wheelers']
                temWheelers = obj['temWheelers']
                for wheeler in wheelers:
                    print("ID", wheelers.index(wheeler), " Name:", wheeler['name'], "   Number:", wheeler['number'],
                          "  Driver Name:", wheeler['driver'])
                remId3 = int(input("Select the ID: "))
                wheelers.pop(remId3)
                print("==========Vehicle Removed Successfully==========\n")
                f.close()

                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (Removeselection == "Truck"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                trucks = obj['trucks']
                temTrucks = obj['temTrucks']
                for truck in trucks:
                    print("ID", trucks.index(truck), " Name:", truck['name'], "   Number:", truck['number'],
                          "  Driver Name:", truck['driver'])
                remId4 = int(input("Select the ID: "))
                trucks.pop(remId4)
                print("==========Vehicle Removed Successfully==========\n")
                f.close()

                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (Removeselection == "Lorry"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                lorries = obj['lorries']
                temLorrys = obj['temLorrys']
                for lorry in lorries:
                    print("ID", lorries.index(lorry), " Name:", lorry['name'], "   Number:", lorry['number'],
                          "  Driver Name:", lorry['driver'])
                remId5 = int(input("Select the ID: "))
                lorries.pop(remId5)
                print("==========Vehicle Removed Successfully==========\n")
                f.close()

                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

        #  option 03
        elif mainOption == '3':
            Assignselection = input("Enter Vehicle Type to Assign(Car/Van/Wheeler/Truck/Lorry): ")

            if (Assignselection == "Car"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                cars = obj['cars']
                temCars = obj['temCars']
                for car in cars:
                    print("ID", cars.index(car), " Name:", car['name'], "   Number:", car['number'], "  Driver Name:",
                          car['driver'], "  Type:", car['type'])
                print("Enter \"A\" for select AC car\nEnter \"B\" for select Non AC car\n")
                userSelection = input("Enter Selection: ")

                if userSelection == 'A':
                    for car in cars:
                        if car['type'] == 'AC':
                            dic = car
                            id = cars.index(car)
                            break
                            f.close()

                elif userSelection == 'B':
                    for car in cars:
                        if car['type'] == 'NonAC':
                            dic = car
                            id = cars.index(car)
                            break
                            f.close()
                temCars.append(dic)
                cars.pop(id)
                print("==========Vehicle Assigned Successfully==========\n")
                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (Assignselection == "Van"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                vans = obj['vans']
                temVans = obj['temVans']
                for van in vans:
                    print("ID", vans.index(van), " Name:", van['name'], "   Number:", van['number'], "  Driver Name:",
                          van['driver'], "  Type:", van['type'])
                print("Enter \"A\" for select AC van\nEnter \"B\" for select Non AC van\n")
                userSelection = input("Enter Selection: ")
                if userSelection == 'A':
                    for van in vans:
                        if van['type'] == 'AC':
                            dic = van
                            id = vans.index(van)
                            break
                            f.close()

                elif userSelection == 'B':
                    for van in vans:
                        if van['type'] == 'NonAC':
                            dic = van
                            id = vans.index(van)
                            break
                            f.close()
                temVans.append(dic)
                vans.pop(id)
                print("==========Vehicle Assigned Successfully==========\n")
                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (Assignselection == "Wheeler"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                wheelers = obj['wheelers']
                temWheelers = obj['temWheelers']
                for wheeler in wheelers:
                    print("ID", wheelers.index(wheeler), " Name:", wheeler['name'], "   Number:", wheeler['number'],
                          "  Driver Name:", wheeler['driver'])
                    for wheeler in wheelers:
                        dic = wheeler
                        id = wheelers.index(wheeler)
                        break
                        f.close()
                temWheelers.append(dic)
                wheelers.pop(id)
                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (Assignselection == "Truck"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                trucks = obj['trucks']
                temTrucks = obj['temTrucks']
                for truck in trucks:
                    print("ID", trucks.index(truck), " Name:", truck['name'], "   Number:", truck['number'],
                          "  Driver Name:", truck['driver'])
                    for truck in trucks:
                        dic = truck
                        id = trucks.index(truck)
                        break
                        f.close()
                temTrucks.append(dic)
                trucks.pop(id)
                print("==========Vehicle Assigned Successfully==========\n")
                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (Assignselection == "Lorry"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                lorries = obj['lorries']
                temLorrys = obj['temLorrys']
                f.close()
                for lorry in lorries:
                    print("ID", lorries.index(lorry), " Name:", lorry['name'], "   Number:", lorry['number'],
                          "  Driver Name:", lorry['driver'])
                    for lorry in lorries:
                        dic = lorry
                        id = lorries.index(lorry)
                        break
                        f.close()
                temLorrys.append(dic)
                lorries.pop(id)
                print("==========Vehicle Assigned Successfully==========\n")
                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

        # option 4
        elif mainOption == '4':
            Releaseselection = input("Enter Vehicle Type to Release(Car/Van/Wheeler/Truck/Lorry): ")

            if (Releaseselection == "Car"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                cars = obj['cars']
                temCars = obj['temCars']
                f.close()
                for car in temCars:
                    print("ID", temCars.index(car), "Name: ", car['name'], "  Number:", car['number'],
                          "  Driver Name: ", car['driver'], "  Type: ", car['type'])
                userSelection = int(input("Enter the id: "))
                obj = temCars[userSelection]
                temCars.pop(userSelection)
                print("==========Vehicle Released Successfully==========\n")
                f.close()

            elif (Releaseselection == "Van"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                vans = obj['vans']
                temVans = obj['temVans']

                for van in temVans:
                    print("ID", temVans.index(van), "Name: ", van['name'], "  Number:", van['number'],
                          "  Driver Name: ", van['driver'], "  Type: ", van['type'])
                userSelection = int(input("Enter the id: "))
                obj = temVans[userSelection]
                vans.append(obj)
                temVans.pop(userSelection)
                print("==========Vehicle Released Successfully==========\n")
                f.close()

            elif (Releaseselection == "Wheeler"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                wheelers = obj['wheelers']
                temWheelers = obj['temWheelers']

                for wheeler in temWheelers:
                    print("ID", temWheelers.index(wheeler), "Name: ", wheeler['name'], "  Number:", wheeler['number'],
                          "  Driver Name: ", wheeler['driver'])
                userSelection = int(input("Enter the id: "))
                obj = temWheelers[userSelection]
                wheelers.append(obj)
                temWheelers.pop(userSelection)
                print("==========Vehicle Released Successfully==========\n")
                f.close()

            elif (Releaseselection == "Truck"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                trucks = obj['trucks']
                temTrucks = obj['temTrucks']

                for truck in temTrucks:
                    print("ID", temTrucks.index(truck), "Name: ", truck['name'], "  Number:", truck['number'],
                          "  Driver Name: ", truck['driver'])
                userSelection = int(input("Enter the id: "))
                obj = temTrucks[userSelection]
                trucks.append(obj)
                temTrucks.pop(userSelection)
                print("==========Vehicle Released Successfully==========\n")
                f.close()

            elif (Releaseselection == "Lorry"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                lorries = obj['lorries']
                temLorrys = obj['temLorrys']

                for lorry in temLorrys:
                    print("ID", temLorrys.index(lorry), "Name: ", lorry['name'], "  Number:", lorry['number'],
                          "  Driver Name: ", lorry['driver'])
                userSelection = int(input("Enter the id: "))
                obj = temLorrys[userSelection]
                lorries.append(obj)
                temLorrys.pop(userSelection)
                print("==========Vehicle Released Successfully==========\n")
                f.close()

        # option 05
        elif mainOption == '5':
            print("==========Available Vehicles==========")
            Seeselection = input("Enter Vehicle Type to Check Availability(Car/Van/Wheeler/Truck/Lorry): ")

            if (Seeselection == "Car"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                cars = obj['cars']
                temCars = obj['temCars']

                for car in cars:
                    print("ID", cars.index(car), "Name: ", car['name'], "  Number: ", car['number'], "  Driver Name: ",car['driver'], "  Type: ", car['type'],"\n")
                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (Seeselection == "Van"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                vans = obj['vans']
                temVans = obj['temVans']

                for van in vans:
                    print("ID", vans.index(van), " Name:", van['name'], "   Number:", van['number'], "  Driver Name:",van['driver'], "  Type:", van['type'],"\n")
                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (Seeselection == "Wheeler"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                wheelers = obj['wheelers']
                temWheelers = obj['temWheelers']

                for wheeler in wheelers:
                    print("ID", wheelers.index(wheeler), " Name:", wheeler['name'], "   Number:", wheeler['number'],"  Driver Name:", wheeler['driver'],"\n")
                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (Seeselection == "Truck"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                trucks = obj['trucks']
                temTrucks = obj['temTrucks']

                for truck in trucks:
                    print("ID", trucks.index(truck), " Name:", truck['name'], "   Number:", truck['number'],"  Driver Name:", truck['driver'],"\n")
                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

            elif (Seeselection == "Lorry"):
                f = open('vehicles.json', 'r')
                obj = json.load(f)
                lorries = obj['lorries']
                temLorrys = obj['temLorrys']

                for lorry in lorries:
                    print("ID", lorries.index(lorry), " Name:", lorry['name'], "   Number:", lorry['number'],"  Driver Name:", lorry['driver'],"\n")
                f = open('vehicles.json', 'w')
                json.dump(obj, f)
                f.close()

back=Image.open('C:\\pycharm\\image.jpg')
back_end=ImageTk.PhotoImage(back)
root.geometry("600x500")
lbl=Label(master,image=back_end)
lbl.place(x=0,y=0)

# Heading
topic=Label(root, text="WELCOME TO PARANAVITHANAGE CAB SERVEICE ", font="arial 17 bold ")
topic.place(x=4, y=30)

customerlabel1 = Label(root, text='Customer Section', font=('Arial bold', 15))
customerlabel1.place(x=160, y=200)

Custbtn = Button(text="CUSTOMER", command=customer)
Custbtn.place(x=380, y=203)

adminLabel = Label(root, text='Admin Section', font=('Arial bold', 15))
adminLabel.place(x=177, y=273)

Adminbtn = Button(text="ADMIN", command=admin)
Adminbtn.place(x=390, y=275)

root.mainloop()

# ============================ End of the Project ========================================