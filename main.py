linoleum_price = float(input("Ieraksti linoleja cenu (EUR/m2): "))
roll_width = float(input("Ieraksti linoleja platumu (m): "))
room_width = float(input("ieraksti istabas platumu (m): "))
room_length = float(input("ieraksti istabas garumu (m): "))


linoleum_area = roll_width * (room_width + 0.1) * (room_length + 0.1)  
total_cost = linoleum_area * linoleum_price


print("Pilna cena linolejam sajai izstabai ir {:.2f} EUR.".format(total_cost))