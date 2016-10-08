print (100*"=")
print ("Welcome to the Coffee Kiosk Service Center")
print (100*"=")
print (2*"\n")
end_of_service = 0
while not end_of_service:
    try:
       import Customer_Module
       end_of_service = 1
    except ValueError, e:
        print("'%s' Kiosk error." % e.args[0].split(": ")[1])
