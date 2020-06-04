class Hall:
    def __init__(self):
        self.Name=[]
        self.ph_no=[]
        self.Adress=[]
        self.bookingDate=[]
        self.Cost=[]
        self.Owner=[]
        print("Enter the number of Entries")
        n=int(input())
        for i in range(0,n):
            print("Enter details of Hall",i+1)
            
            na=input("Enter Hall name\n")
            self.Name.append(na)
            
            pn=int(input("Enter Phone\n"))
            self.ph_no.append(pn)
            
            a=input("Enter Address\n")
            self.Adress.append(a)
            
            bd=input("Enter Date of booking\n")
            self.bookingDate.append(bd)
            
            c=float(input("Enter cost\n"))
            self.Cost.append(c)
          
            o=input("Enter owner name\n")
            self.Owner.append(o)
        
    def equals(self):
        
        q=0
        print("")
        print("Enter the Hall details for booking")
        
        ena=input("Enter Hall name\n")
        
        epn=int(input("Enter Phone\n"))
     
        ea=input("Enter Address\n")
    
        ebd=input("Enter Date of booking\n")
        
        ec=float(input("Enter cost\n"))
        
        eo=input("Enter owner name\n")
        while ena in self.Name:
            while epn in self.ph_no:
                while ebd in self.bookingDate:
                    q=1
                    break
                break
            break
        if q>=1:
            print("")
            print("Already Registered")
            print("")
            Hall.Display(self)
            
        else:
            print("")
            print("Registration available")
            Hall.Display(self)
            print("Hall name :",end="")
            print(ena)
            print("Phone No :",end=" ")
            print(epn)
                    
            print("Address :",end="")
            print(ea)
            print("Cost :",end="") 
            print("%.2f"%ec)
            print("Owner name :",end="") 
            print(eo)
            
    def Display(self):
        print("")
        print("Display the Booked Hall details")
        for i in range(0,len(self.Name)):
            print("Hall name :",end="")
            print(self.Name[i])
            print("Phone No :",end=" ")
            print(self.ph_no[i])
            print("Address :",end="")
            print(self.Adress[i])
            print("Cost :",end="")
            print("%.2f" %self.Cost[i])
            print("Owner name :",end="")
            print(self.Owner[i])
                        
            
       
                       

        

ob=Hall()
ob.equals()
