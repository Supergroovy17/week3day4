

#Your task is to update this menu based on given instructions. This exercise tests your ability to manipulate nested dictionaries and manage data effectively.





restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main_Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}


restaurant_menu['Beverages']={"Man-hatten" : 10.00, "Oldfashiond"  :  9.00}

restaurant_menu["Main_Course"]["Steak"]=17.99 

restaurant_menu["Starters"].pop("Soup") 
print(restaurant_menu)
restaurant_menu["Starters"].pop("Bruschetta")


#Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
#Implement functions to:
#Open a new service ticket.
#Update the status of an existing ticket.
#Display all tickets or filter by status.


service_tickets = {}
    
service_tickets["Ticket002"]={"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
service_tickets["Ticket001"]={"Customer": "Alice", "Issue": "Login problem", "Status": "open"}

service_tickets["Ticket002"].update({"Status":"open"})

print(service_tickets["Ticket001"]["Status"])

