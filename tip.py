def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    dollars_without_dollarsign = d.replace("$", "")
    return float(dollars_without_dollarsign)


def percent_to_float(p):
    # TODO
    percent_withoutpercentage = p.replace("%","")
    p_conversion = float(percent_withoutpercentage) / 100
    return p_conversion


main()

