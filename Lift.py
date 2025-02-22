from prettytable import PrettyTable

class MallNavigator:
    def __init__(self):
        self.malls = {
            1: "Mall of Jaipur",
            2: "Manglam JTM Mall",
            3: "World Trade Park"
        }
        self.floors = {
            "Mall of Jaipur": [
                ("LB", "Parking"),
                ("UB", "Parking"),
                ("G", "Jewellery: GIVA, OP, JKJ"),
                ("1", "Shopping: Reliance Trends, H&M, Jockey, Raymond"),
                ("2", "Cafeteria: Rosado, Cafe Coffee, Dream Café"),
                ("3", "Cinema: PVR, Inox"),
                ("4", "Electronic: Gada, Croma, Pal"),
                ("5", "Gaming Zone: Masti-Game, Fun-City, Crazy Gaming"),
                ("6", "Furniture: Royal, Jangid, Jadish"),
                ("7", "Offices: Softraw IT, CA, Start Bit IT"),
                ("8", "Hotel Bars: Aza, Mercury Lounge, Ten 11 Lounge")
            ],
            "Manglam JTM Mall": [
                ("B", "Parking"),
                ("G", "Shopping: Reliance Trends, Zudio, Teamsprint"),
                ("1", "Gaming Zone: Rock Gaming, VR-Theme Park"),
                ("2", "Cafeteria: Sultanat Cafe, Cafe Quaint, Lazy Mojo"),
                ("3", "Offices: VRM Group, Girnar Software")
            ],
            "World Trade Park": [
                ("LB", "Parking"),
                ("UB", "Parking"),
                ("G", "Electronics: Croma, Havells, Philips"),
                ("1", "Shopping: Being Human, H&M, Peter England"),
                ("2", "Furniture: Lokpriya, Godrej, House Sutra"),
                ("3", "Cafeteria: Nibs, Anokhi Café, NBC"),
                ("4", "Cinema: Miraj, IMAX"),
                ("5", "Restaurants: Suvarna Mahal, Skyfall, Peacock")
            ]
        }

    def display_mall(self, mall_name):
        print(f"* {mall_name} *".center(50))
        table = PrettyTable(["Floor", "Details"])
        table.add_rows(self.floors[mall_name])
        print(table)
        self.choose_floor(mall_name)

    def choose_floor(self, mall_name):
        choice = input("Enter preferred floor (e.g., G, 1, 2, etc.): ").strip()
        floor_map = dict(self.floors[mall_name])
        print(floor_map.get(choice, "Invalid choice!"))
        if input("Return to Main Menu? (Y/N): ").lower() == 'y':
            main()


def main():
    mall = MallNavigator()
    table = PrettyTable(["ID", "Mall Name"])
    table.add_rows([(key, value) for key, value in mall.malls.items()])
    print(table)
    ch = int(input("Enter Mall ID to Visit: "))
    mall.display_mall(mall.malls.get(ch, "Invalid choice!"))


if __name__ == "__main__":
    main()
