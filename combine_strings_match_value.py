season = "Winter"

match season:
    case "Winter":
        print("December January Febrary")
    case "Spring":
        print(" March April May")
    case "Autumn":
        print("September October November")
    case "Summer":
        print("June July August")
    case _:
        print("Invalid Season")