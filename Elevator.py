from prettytable import PrettyTable
class MallNavigator:
    def __init__(self):
        self.t1 = "* MALL OF JAIPUR *"
        self.t2 = "* Manglam JTM Mall *"
        self.t3 = "* World Trade Park *"

    def Mall_of_Jaipur(self):
        print(self.t1.center(50))
        table = PrettyTable(["Floor", "Name"])
        table.add_rows([
            ["Lower Basement(LB)", "Parking\n"],
            ["Upper Basement(UB)", "Parking\n"],
            ["Ground Floor(G)", "Jewellery:\n1.GIVA Jewellery.\n2.OP Jewellers.\n3.JKJ Jewellers.\n"],
            ["First Floor(1)", "Shopping:\n1.Reliance Trends.\n2.H&m.\n3.Jockey.\n4.Raymond.\n"],
            ["Second Floor(2)", "Cafeteria:\n1.Rosado.\n2.Cafe Coffe.\n3.Dream Café.\n"],
            ["Third Floor(3)", "Cinema:\n1.PVR.\n2.Inox.\n"],
            ["Fourth Floor(4)", "Electronic:\n1.Gada Electronics.\n2.Croma.\n3.Pal Electronic.\n"],
            ["Fifth Floor(5)", "Gaming Zone:\n1.Masti-Game.\n2.Fun-City.\n3.Carzy Gaming.\n"],
            ["Sixth Floor(6)", "Furniture:\n1.Royal Furniture.\n2.Jangid Furniture.\n3.Jadish Furniture.\n"],
            ["Seventh Floor(7)", "Office's:\n1.Softraw IT Solutions Pvt. Ltd.\n2.CA.\n3.Start Bit IT Solutions.\n"],
            ["Eighth Floor(8)", "Hotel bars:\n1.Aza (Fairmont Hotel).\n2.Mercury Lounge & Rooftop.\n3.Ten 11 Lounge Disc & Bar.\n"]
        ])
        print(table)
        self.floor_optionsmoj= {
            "LB": self.Lower_Basement, "lb": self.Lower_Basement,
            "UB": self.Upper_Basement, "ub": self.Upper_Basement,
            "G": self.Ground_Floor, "g": self.Ground_Floor,
            "1": self.First_Floor,
            "2": self.Second_Floor,
            "3": self.Third_Floor,
            "4": self.Fourth_Floor,
            "5": self.Fifth_Floor,
            "6": self.Sixth_Floor,
            "7": self.Seventh_Floor,
            "8": self.Eight_FLoor
        }
        s = (str(input("Return to Main Menu(Press Y/y) :-")))
        if s == 'Y' or s == 'y':
            main()
        
        choice = input("Enter your preferred floor (e.g., LB, UB, G, 1-8): ").strip()
        if choice in self.floor_optionsmoj:
            print(self.floor_optionsmoj[choice]()) 
        else:
            print("Invalid choice! Please enter a valid floor option.")
            
        if choice == 'G':
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "GIVA Jewellery.","G-01"],
                [2,"OP Jewellers.","G-02"],
                [3,"JKJ Jewellers.","G-03"]
            ])
            print(table)
        elif choice == '1':
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "Reliance Trends",101],
                [2,"H&m",102],
                [3,"Jockey",103],
                [4,"Raymond",104]
            ])
            print(table)
        elif choice == '2':
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "Rosado-Cafe",201],
                [2,"Cafe Coffe",202],
                [3,"Dream Café",203]
            ])
            print(table)
        elif choice == '3':
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "PVR-Cinema",301],
                [2,"Inox-Cinema",302]
            ])
            print(table)
        elif choice == '4':
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "Gada Electronics",401],
                [2,".Croma",402],
                [3,"Pal Electronic",403]
            ])
            print(table)
        elif choice == '5':
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "Masti-Game",501],
                [2,"Fun-City",502],
                [3,"Carzy Gaming",503]
            ])
            print(table)
        elif choice == '6':
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "Royal Furniture",601],
                [2,"Jangid Furniture",602],
                [2,"Jadish Furniture",602]
            ])
            print(table)
        elif choice == '7':
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "Softraw IT Solutions Pvt. Ltd",701],
                [2,"Chartered Accountant Office",702],
                [3,"Start Bit IT Solutions",703]
            ])
            print(table)
        else:
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "Masti-Game",801],
                [2,"Fun-City",802],
                [3,"Carzy Gaming",803]
            ])
            print(table)
                
        
    def JTM(self):
        print(self.t2.center(50))
        table = PrettyTable(["Floor", "Name"])
        table.add_rows([
            ["Basement(B)", "Parking\n"],
            ["Ground Floor(G)", "Shopping:\n1.Reliance Trends.\n2. Zudio.\n3.Teamsprint\n"],
            ["First Floor(1)", "Gaming Zone:\n1.Rock Gaming.\n2.VR-Theme Park.\n"],
            ["Second Floor(2)", "Cafeteria:\n1.Sultanat Cafe Fort.\n2.Cafe Quaint.\n3.Cafe Lazy Mojo.\n"],
            ["Third Floor(3)", "Office's:\n1.VRM Group.\n2.Girnar Software."]
        ])
        print(table)
        self.floor_optionsjtm= {
            "LB": self.Lower_Basement, "lb": self.Lower_Basement,
            "B": self.Basement, "b": self.Basement,
            "UB": self.Upper_Basement, "ub": self.Upper_Basement,
            "G": self.Ground_Floor, "g": self.Ground_Floor,
            "1": self.First_Floor,
            "2": self.Second_Floor,
            "3": self.Third_Floor,
        }
        s = (str(input("Return to Main Menu(Press Y/N) :-")))
        if s == 'Y' or s == 'y':
            main()
        choice = input("Enter your preferred floor (e.g., LB, B, UB, G, 1-3): ").strip()
        if choice in self.floor_optionsjtm:
            print(self.floor_optionsjtm[choice]()) 
        else:
            print("Invalid choice! Please enter a valid floor option.")
        
        if choice == 'G':
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "Reliance Trends.","G-01"],
                [2," Zudio.","G-02"],
                [3,".Teamsprint","G-03"]
            ])
            print(table)
        elif choice == '1':
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "Rock Gaming",101],
                [2,"VR-Theme Park",102]
            ])
            print(table)
        elif choice == '2':
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "Sultanat Cafe Fort",201],
                [2,"Cafe Quaint",202],
                [3,"Cafe Lazy Mojo",203]
            ])
            print(table)
        else:
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "VRM Group",301],
                [2,"Girnar Software",302]
            ])
            print(table)
            
            
    def WTP(self):
        print(self.t3.center(50))
        table = PrettyTable(["Floor", "Name"])
        table.add_rows([
            ["Lower Basement(LB)", "Parking\n"],
            ["Basement(B)", "Parking\n"],
            ["Upper Basement(UB)", "Parking\n"],
            ["Ground Floor(G)", "Electronic's:\n1.Croma.\n2.Havells.\n3.Philips.\n"],
            ["First Floor(1)", "Shopping:\n1.Being Human.\n2.H&M.\n3.Peter England.\n"],
            ["Second Floor(2)", "Furniturer's:\n1.Lokepriya Home.\n2.Godrej.\n3.House Sutra.\n"],
            ["Third Floor(3)", "Cafeteria:\n1.Nibs Cafe & Chocolataria.\n2.Anokhi Café.\n3.Nothing Before Coffee.\n"],
            ["Fourth Floor(4)", "Cinema's:\n1.Miraj Cinema.\n2.IMAX- Cinema.\n"],
            ["Fifth Floor(5)", "Restarant's:\n1.Suvarna Mahal.\n2.Skyfall Restaurant.\n3.Peacock Restaurant.\n"]
        ])
        print(table)
        self.floor_optionswtp= {
            "LB": self.Lower_Basement, "lb": self.Lower_Basement,
            "B": self.Basement, "b": self.Basement,
            "UB": self.Upper_Basement, "ub": self.Upper_Basement,
            "G": self.Ground_Floor, "g": self.Ground_Floor,
            "1": self.First_Floor,
            "2": self.Second_Floor,
            "3": self.Third_Floor,
            "4": self.Fourth_Floor,
            "5": self.Fifth_Floor,
        }
        s = (str(input("Return to Main Menu(Press Y/N) :-")))
        if s == 'Y' or s == 'y':
            main()
        choice = input("Enter your preferred floor (e.g., LB, B, UB, G, 1-5): ").strip()
        if choice in self.floor_optionswtp:
            print(self.floor_optionswtp[choice]()) 
        else:
            print("Invalid choice! Please enter a valid floor option.")
            
        if choice == 'G':
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "Croma","G-01"],
                [2,"Havells","G-02"],
                [3,"Philips","G-03"]
            ])
            print(table)
        elif choice == '1':
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "Being Human",101],
                [2,"H&m",102],
                [3,"Peter England",103]
            ])
            print(table)
        elif choice == '2':
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "Lokepriya Home",201],
                [2,"Godrej",202],
                [3,"House Sutra",203]
            ])
            print(table)
        elif choice == '3':
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "Nibs Cafe & Chocolataria",301],
                [2,"Anokhi Café",302],
                [2,"Nothing Before Coffee",303]
            ])
            print(table)
        elif choice == '4':
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "Miraj Cinema",401],
                [2,"IMAX-Cinema",402]
            ])
            print(table)
        else:
            table = PrettyTable(["ID", "Name:", "Room No:"])
            table.add_rows([
                [1, "Suvarna Mahal",501],
                [2,"Skyfall Restaurant",502],
                [3,"Peacock Restaurant",503]
            ])
            print(table)


        
    def Lower_Basement(self):
        return "LB Floor.\nThank You... Visit Again"
    
    def Basement(self):
        return("B Floor.\nThank You... Visit Again")
    
    def Upper_Basement(self):
        return "UB Floor.\nThank You... Visit Again"
    
    def Ground_Floor(self):
        return "G Floor.\nThank You.... Visit Again"
    
    def First_Floor(self):
        return "01 Floor.\n Thank You.... Visit Again"
    
    def Second_Floor(self):
        return "02 Floor.\nThank You.... Visit Again"
    
    def Third_Floor(self):
        return "03 Floor.\nThank You....Visit Again"
    
    def Fourth_Floor(self):
        return "04 Floor\nThank You....Visit Again"
    
    def Fifth_Floor(self):
        return "05 Floor\nThank You.... Visit Again"
    
    def Sixth_Floor(self):
        return "06 Floor\nThank You.... Visit Again"
    
    def Seventh_Floor(self):
        return "07 Floor\nThank You.... Visit Again"
    
    def Eight_FLoor(self):
        return "8th Floor.\nThank You.... Visit Again"



def main():
    mall = MallNavigator()
    table = PrettyTable(["ID:", "Mall_Name:"])
    table.add_rows([
        [1, "Mall of Jaipur\n"],
        [2, " Manglam JTM Mall\n"],
        [3, "World Trade Park\n"],
    ])
    print(table)
    ch = int(input("Enter Which Mall You Want to Go:- \n"))
    if ch == 1:
        mall.Mall_of_Jaipur()
    elif ch == 2:
        mall.JTM()
    elif ch == 3:
        mall.WTP()
    else:
        print("Enter a valid Mall No:-")  
    return " "
print(main())   
        

