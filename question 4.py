x = int(input("Enter x-coordinate : "))
y = int(input("Enter y-coordinate : "))
point = [x,y]
if x > 0 :
    if y > 0 :
        print("(" , x , "," , y , ")" , "is in 1st quadrant")
    else :
        print("(" , x , "," , y , ")" , "is in 4th quadrant")

if x < 0 :
    if y > 0 :
        print("(" , x , "," , y , ")" , "is in 2nd quadrant")
    elif point[1] == 0 :
       print("(" , x , "," , y , ")" , "is in on X-axis")
    else :
        print("(" , x , "," , y , ")" , "is in 3rd quadrant")
elif (point[0] == 0 and point[1] == 0) :
    print("(" , x , "," , y , ")" , "is Origin")
elif point[0] == 0 :
    print("(" , x , "," , y , ")" , "is on Y-axis")
    
    
         
    
    

