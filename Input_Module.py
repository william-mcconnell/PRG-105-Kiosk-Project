# this is the module where the customer makes their orders

def discount(ord_total): #this function computes discounts
    global disc_amt_total
    disc_amt = .1
    disc_amt_total = disc_amt * ord_total
    print (disc_amt_total)
    return disc_amt_total

def county_tax(ord_total): #this function receives the order total from the input module.
                          #the function returns the calculated county tax
    cty_tax = .03
    cty_tax_total = cty_tax * ord_total
    return cty_tax_total

def state_tax(ord_total): #this function receives the order total from the input module.
                         #the function returns the calculated state tax

    state_tax = .07
    state_tax_total = state_tax * ord_total
    return state_tax_total

def complete_order(ordtot): #this module will total the order, add taxes, and print out the receipt
    global disc_amt_total
    order_total = ordtot
    disc_amt_total = 0
    disc_code = raw_input("Do you have a discount code? (Y/N)\n")
    if disc_code == "Y":
        disc_number = input("Please enter your code.\n")
        if disc_number == 99751:
            discount(ordtot)
            ordtot = order_total - disc_amt_total

    tax_total = 0
    if order_total > 0:
        tax_total_cty = county_tax(ordtot)
        tax_total_state = state_tax(ordtot)

    orderline = "Order total: $ %3.2f"% order_total
    orderdisc = "Discount:    $ %-3.2f"% disc_amt_total
    ordercity = "City Tax:    $ %3.2f"% tax_total_cty
    orderstate = "State Tax:   $ %3.2f"% tax_total_state
    order_total = ordtot+tax_total_cty+tax_total_state
    ordertot = "Total :      $ %3.2f"% order_total

    print(orderline)
    print (orderdisc)
    print(ordercity)
    print(orderstate)
    print(20*"=")
    print(ordertot)

def load_menus(): #using a dictionary
     global cboSweeteners
     global cboCreamers
     global cboBrewTypes
     global cboCoffeeType
     global cboCoffeeSize
     global cboPrice

     cboSweeteners = {1:"None",2:"Raw",3:"Cane",4:"Coconut",5:"Granulated",6:"Sweet & Low",
                     7:"Equal",8:"Stevia",9:"Splenda"}

     cboCreamers = {1:"None",2:"French Vanilla",3:"Fat-Free French Vanilla",4:"Sugar-Free French Vanilla",
                    5:"Hazelnut",6:"Sugar-Free Hazelnut",7:"Salted Caramel Mocha",8:"Southern Butter Pecan",
                    9:"White Chocolate Macadamia",10:"White Chocolate Raspberry",11:"Caramel Macchiato",
                    12:"Fat-Free Caramel Macchiatto",13:"Sugar-Free Caramel Macchiatto",14:"Hazelnut Macchiato",
                    15:"Vanilla Macchiato",16:"Amaretto Cafe",17:"Irish Creme Cafe",18:"Vanilla Caramel Creme"}

     cboBrewTypes = {1:"Drip",2:"Steep",3:"Espresso",4:"Turkish" }

     cboCoffeeType = {1:"Black",2:"With Cream",3:"With Sweetener",4:"Both Cream and Sweetener",5:"Complete Order"}

     cboPrice = {1:1.25,2:2.50,3:3.75,4:5.00}

     cboCoffeeSize = {1:"12 oz",2:"16 oz",3:"20 oz",4:"24 oz"}

def coffeetype_menu():
    for i in cboCoffeeType.iteritems():
        print (i)

def brew_menu():
    for i in cboBrewTypes.iteritems():
        print (i)

def coffeesize_menu():
    for i in cboCoffeeSize.iteritems():
        print (i)

def creamer_menu():
    for i in cboCreamers.iteritems():
        print (i)

def sweetener_menu():
    for i in cboSweeteners.iteritems():
        print (i)

load_menus() #loading all of the items for each menu.
order_complete = 0
order_cnt = 0
order_subtotal = 0
order_total = 0
global ordtot
global disc_amt_total
global orderprice
global orderbrew
global ordercream
global ordersweet
global ordersize
global ordertype
global ordertransaction
while not order_complete:
    global orderline
    if order_cnt > 0:
         orderline = orderline+orderprice
         if order_cnt == 1: #this initializes the ordertransaction dictionary
            ordertransaction= {order_cnt:orderline}
         else: #this adds to the dictionary
            ordertransaction.update({order_cnt:orderline})
    try:
       print (20*"=")
       coffeetype_menu()
       print (20*"=")
       coffee_type = int(input("Please make your coffee selection.\n"))
       print (20*"=")
       if coffee_type <= 5 and coffee_type > 0:
           if coffee_type == 5:
              order_complete = 1
              print ("Thank you for your order!")
              print (40*"=")
              for i in ordertransaction.iteritems():
                  print (i)
           else:
              brew_menu()
              print (20*"=")
              coffee_brew = int(input("Please make your brew type selection.\n"))
              orderbrew = cboBrewTypes[coffee_brew]
              coffeesize_menu()
              print (20*"=")
              coffee_size = int(input("Please make your coffee cup selection.\n"))
              order_cnt = order_cnt + 1
              orderline = ""
              ordersize = cboCoffeeSize[coffee_size]
              order_subtotal = cboPrice[coffee_size]+order_subtotal
              tempprice = cboPrice[coffee_size]
              temp = "$ %3.2f"% tempprice #format the price correctly for a string
              orderprice = temp
              ordertype = cboCoffeeType [coffee_type]
              orderline = ordersize+" - "+ordertype+" - "+orderbrew+" - "
              if coffee_type == 1:
                  orderline = orderline #nothing happening, just a place holder
              elif coffee_type == 2:
                  creamer_menu()
                  print (20*"=")
                  coffee_cream = int(input("Please make your creamer selection.\n"))
                  ordercream = cboCreamers[coffee_cream]
                  orderline = orderline+ordercream+" - "
              elif coffee_type == 3:
                  sweetener_menu()
                  print (20*"=")
                  coffee_sweet = int(input("Please make your sweetner selection.\n"))
                  ordersweet = cboSweeteners[coffee_sweet]
                  orderline = orderline+ordersweet+" - " #list entry in order line
              elif coffee_type == 4:
                  creamer_menu()
                  print (20*"=")
                  coffee_cream = int(input("Please make your creamer selection.\n"))
                  sweetener_menu()
                  coffee_sweet = int(input("Please make your sweetner selection.\n"))
                  ordercream = cboCreamers[coffee_cream]
                  orderline = orderline+ordercream+" - "
                  ordersweet = cboSweeteners[coffee_sweet]
                  orderline = orderline+ordersweet+" - " #last entry in order line

    except ValueError, e:
        print("'%s' Kiosk error." % e.args[0].split(": ")[1])

print (40*"=")
complete_order(order_subtotal) #this calls the routine to calcualte totals and taxes
