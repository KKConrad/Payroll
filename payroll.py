def calculatepay(h,r):
    if h<=40:
        p=r*h
    else:
        p=r*40+(r*1.5*(h-40))
    return p
  
try: 
    inp=raw_input("Enter Hours!!!11: ")
    hours=float(inp)
    inp=raw_input("Enter the rate amg!: ")
    rate=float(inp)

except:
    print "Error, you didn't enter a numeric input =(")
    quit()
  
pay=calculatepay(hours, rate)
print pay
