debt_int = int(input("Enter the debt value:"))
bill_val_int = int(input("Enter a denomination of currency:"))

#height = debt/billval * 0.0043in/1 bill * 1ft/12in * 1mile/5280ft
height_flt = (debt_int / bill_val_int)*(0.0043)*(1/12)*(1/5280)
mult_moon_dist_flt = height_flt/ 238857

print()
print("The debt", debt_int, "as a height in miles of", bill_val_int, "'s:", height_flt)
print("That is", mult_moon_dist_flt, "times the average distance from the eart to the moon.")
