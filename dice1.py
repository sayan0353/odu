import random

x=y=1
print "\n----START----"
print (x,y)
i=1
while ((x<=8) and (y<=8)):
     
    dice=random.randint(1,6)
    print "Dice Value %d =%d"%(i,dice)
    i=i+1
    if (x%2 != 0) :    
        if ((y+dice)<=8):
            y=y+dice
        else:
            s_left=8-y
            y=y+s_left
            d_left=dice-s_left-1
            x=x+1
            y=y-d_left
    
    elif(x==8):
        if ((y-dice)>0):
            y=y-dice
            break
        if(y==1):
            print x,y
            break
        else:
            s_left=y-1
            if((y-dice)>s_left-1):
                continue
            else:
                y=y-s_left
                d_left=dice-s_left-1
                y=y+d_left
        
            
    else:
        if ((y-dice)>0):
            y=y-dice
        else:
            s_left=y-1
            y=y-s_left
            d_left=dice-s_left-1
            x=x+1
            y=y+d_left
    
        
    print x,y
    

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
    
                
                
                
                
                
                
                
                