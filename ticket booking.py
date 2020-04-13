import sys
from pathlib import Path
class Ticket:
        def menu(self):
                s=int(input("what you want? 1:Book tickets  2:Cancel tickets  3:View tickets"))
                if s==1:
                        self.book_ticket()
                elif s==2:
                        self.cancel_ticket()
                elif s==3:
                        self.view_ticket()
                else:
                        print("try again")
                
        def __init__(self):
                
                self.total=60
                datapath=Path()
                detailspath=datapath / "detail.txt"
                detail=open(detailspath,"r")
                f=detail.readlines()
                l=len(f)
                print(f,l)
                try:
                        ar=(f[0].rstrip()).split(" ")
                        self.lis=ar
                        self.id=int(ar[-4])
                        print(self.lis,self.id,ar,f)
                except:
                        self.id=0
                        self.lis=[]
                try:
                        for i in range(l):
                                if i==l-1:
                                        self.total=int(f[i].rstrip())
                                        
                       
                except:
                        self.total=60   
                                        
                detail.close()
                self.menu()

        def final(self):
                s=input("Shall we do anything more (y/n)")
                if s=="y":
                        self.menu()  
        

        def book_ticket(self):
                if self.total==0:
                        print("No tickets available")
                        self.final()
                
                else:
                        print("the total available tickets are "+ str (self.total))
                        self.name=input("name")
                        self.source=input("source")
                        self.destination=input("destination")
                        self.date=input("date as ddmmyy")
                        self.total=self.total-1
                        self.id=self.id+1
                        self.lis.append(str(self.id))
                        self.lis.append(str(self.name))
                        self.lis.append(str(self.source))
                        self.lis.append(str(self.date))
                        detailspath=Path() / "detail.txt"
                        detail=open(detailspath,"w")
                        string=" ".join(self.lis)
                        
                        detail.write(string+"\n")
                        detail.write(str(self.total)+"\n")
                        detail.close()
                        print("Booking succesful:Your booking id is {}".format(str(self.id)))
                        print("pay fare")
                        self.final()

        def cancel_ticket(self):
                self.id=input("id")
                detailspath=Path() / "detail.txt"
                detail=open(detailspath,"w+")
                line=detail.readline()
                line=line.rstrip()
                a=line.split(" ")
                l=len(a)
                for i in range(l):
                        if a[i]==self.id:
                                print(self.id)
                                for j in range(4):
                                        s=a[i+j]
                                        a.remove(s)
                                break
                        else:
                                continue
                detail.write(" ".join(a))
                self.total=self.total+1
                detail.write(str(self.total))
                detail.close()
                self.final()

        def view_ticket(self):
                self.id=input("id")
                detailspath=Path() / "detail.txt"
                detail=open(detailspath)
                line=detail.readline()
                line=line.rstrip()
                a=line.split(" ")
               
                for i in range(len(a)):
                       
                        if a[i]==self.id:
                                for j in range(4):
                                        s=a[i+j]
                                        print(s)
                        else:
                                continue
                detail.close()
                self.final()
      
my=Ticket()
