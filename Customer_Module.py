def OpenTextFileRead(): # use this for a returning customer
    global custfile
    global old_cust
    try:
        acnt = 1
        custfile = open('CustomerList.txt','r+') #this opens the customer file and stores the contents in the
                                                 # variable custfile
        old_cust = list(custfile)                # This loads custfile into a list called old_cust
        #print (old_cust)
        return old_cust
    except:
        print ("CustomerList.txt does not exist.")

def OpenTextFileAppend(): # use this to add a new customer
    global custfile
    global old_cust
    global fileindex
    try:
        acnt = 1
        custfile = open('CustomerList.txt','a+') #this opens the customer file and stores the contents in the
                                                 # variable custfile
        old_cust = list(custfile)                # This loads custfile into a list called old_cust
        fileindex = len(old_cust)
     #   print (fileindex)
        return old_cust, fileindex
        # close(custfile)
    except:
        print ("CustomerList.txt does not exist.")

def GetCustNum():
    global custnum
    custnum = input('Please enter your customer number')
    str_custnum =str(custnum)
    custlen = len(str_custnum)
    custindex = str_custnum[0:custlen-4]
    custnum = int(custindex)
    custnum = custnum - 1
    #print (custlen, custindex, custnum)
    return custnum
    #    except ValueError, e:
    #        print ("'%s' Kiosk error." % e.args[0].split(": ")[1])


def FindCustNum(custnum):
    global old_cust
    global first_name
    #print (custnum)
    try:
        #print (old_cust)
        n = len(old_cust)
        #print (n)
        found_Cust = old_cust[custnum]
        #print (found_Cust[0:7])
        index = found_Cust.find(',') #find the first comma
        cust_number = found_Cust[0:index]
        #print (cust_number)
        size = len(found_Cust)
        for i in range(7): # there are 6 remaining commas
            index_old = index
            index = found_Cust.find(',',index_old+1)
            #print (index)
            #print (index_old)
            #print (i)
            if i == 0 :
               first_name = found_Cust[index_old+1:index]
               #print ('First Name: ',first_name)
            elif i == 1:
                last_name = found_Cust[index_old+1:index]
                #print ('Last Name: ',last_name)
            elif i == 2:
                address = found_Cust[index_old+1:index]
                #print ('Address: ',address)
            elif i == 3:
                city = found_Cust[index_old+1:index]
                #print ('City: ',city)
            elif i == 4:
                state = found_Cust[index_old+1:index]
                #print ('State: ',state)
            elif i == 5:
                zip = found_Cust[index_old+1:index]
                #print ('Zipcode',zip)
            elif i == 6:
                phone = found_Cust[index_old+1:index]
                #print ('Phone: ',phone)


        print (cust_number)
        print (first_name)
        print (last_name)
        print (address)
        print (city)
        print (state)
        print (zip)
        print (phone)
        return first_name
    except:
        print ("Customer does not exist.")

def Get_New_Cust_Data(): #This creates a new customer record
    global new_cust
    global first_name
    print ("We need to ask a few questions.")
    print ("We use the last four digits of your phone number to create a customer number.")
    print (24*"=")
    cust_first = raw_input("First Name: ") #use raw_input to capture strings
    cust_last = raw_input("Last Name: ")
    cust_street = raw_input("Street Address: ")
    cust_city = raw_input("City: ")
    cust_city = raw_input("State: ")
    cust_zip = raw_input("Zip Code: ")
    cust_phone = raw_input("Last four digits only: ")
    str_phone = str(fileindex+1)+cust_phone
    print (24*"=")
    print ("Thank you for your information.")
    # The following creates the string that will write to the file.
    new_cust = str_phone+","+cust_first+","+cust_last+","+cust_street+","+cust_city+","+cust_zip+","+cust_phone+","
    print (new_cust)
    custfile.write(new_cust)
    custfile.close()
    return first_name

global custfile
global first_name
global old_cust
global end_of_day
global new_cust
end_of_day = 0
while not end_of_day:
    try:
       print (20*"=")
       print ("1. Returning Customer")
       print ("2. New Customer")
       print ("3. Guest")
       print (20*"=")
       cust_type = int(input("Please select your customer type."))
       if cust_type == 1:
           OpenTextFileRead()
           #print (old_cust)
           GetCustNum()
           FindCustNum(custnum)
           print (first_name)
       elif cust_type == 2:
           OpenTextFileAppend()
           Get_New_Cust_Data()
           print (first_name)
       elif cust_type == 3:
           print ("Welcome to the Kiosk Service Center")
           first_name = "Guest"
       elif cust_type == 99:
           end_of_day = 1
    except ValueError, e:
        print("'%s' Kiosk error." % e.args[0].split(": ")[1])

