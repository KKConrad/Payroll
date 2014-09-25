largest=None
smallest=None

while True:
    inp=raw_input("Enter a number please!: ")
    try:
        num=int(inp)
        
        if largest is None:
            largest=num
        elif num>largest:
            largest=num
        if smallest is None:
            smallest=num
        elif num<smallest:
            smallest=num
    
    except:
            if inp == "done" : break
            else:
                print "This was an invalid input, no!"

print "The largest number you had picked was:", largest
print "The smallest number you had picked was:", smallest
