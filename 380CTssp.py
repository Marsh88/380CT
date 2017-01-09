from random import randint, sample
from itertools import chain, combinations
from time import time

class SSP():
    def __init__(self, S=[], t=0):
        self.S = S
        self.t = t
        self.n = len(S)
        self.count= 0
        self.decision = False
        self.total    = 0
        self.selected = []

    def __repr__(self):
        return "SSP instance: S="+str(self.S)+"\tt="+str(self.t)
    
    def random_instance(self, n, bitlength=10): #creates a random isntance 
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        
        self.t = randint(0,n*max_n_bit_number)
        self.n = len( self.S )

    def random_yes_instance(self, n, bitlength=10):#creates a random isntance that can be found
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        self.t = sum( sample(self.S, randint(0,n)) )
        self.n = len( self.S )


    def try_at_random(self): #generates randomly until it finds it or it does it 50 times, this was put in as the program would just loop however it still doesnt properlyl check because it may take mroe then 50 tries for random
        candidate = []
        total = 0
        self.count=0
        while total != self.t and self.count <51:
            self.count+=1
            candidate = sample(self.S, randint(0,self.n))
            total     = sum(candidate)
            print( "Trying: ", candidate, ", sum:", total )
        print ("found",candidate)
        print ("ran",self.count,"times")




    def try_Exaust_search(self):
        candidate=self.S
        self.count=0
        Poly=self.polynominal_time()
        if Poly == True: #this checks if a polynomial tiem situation exists
            print ("found")
            return 1
        elif Poly == False:
            print ("not found")
            return 0
        if (self.Exhaust_imp(candidate,len(candidate),self.t)==True):#runs the actual class that checks for a subset sum
            print ("found")
            print ("ran" ,self.count,"times")
            return 1
        else:
            print ("not found")
            print ("ran" ,self.count,"times")
            return 0
                        
    def Exhaust_imp(self,list2,n,sum1):#takes a list, size of list and sum of list as input
        self.count+=1
        print ("old total",sum1)
        if sum1 == 0: #if it hits 0 it is true 
            return True
        if sum1!=0 and n==0: #it the lsit empties then it is not true
            return False
        if (list2[n-1]>sum1): #if the top of the list is bigger then the target, ignore it
            return self.Exhaust_imp(list2,n-1,sum1)
        print ("new total ",sum1-list2[n-1])
        return (self.Exhaust_imp(list2,n-1,sum1) or self.Exhaust_imp(list2,n-1,sum1-list2[n-1]))#forks into two classes, one where the current element is added and one where it isnt
            
            



    def try_Dynamic_search(self):
        candidate=self.S
        self.count=0
        Poly=self.polynominal_time()
        if Poly == True:
            print ("found")
            return 1
        elif Poly == False:
            print ("not found")
            return 0    
        if (self.Dynamic_imp(candidate,self.n-1,self.t))==True :
            print ("found")
            print ("ran" ,self.count,"times")
            return 1
        else:
            print ("not found")
            print ("ran" ,self.count,"times")
            return 0


    def Dynamic_imp(self,list1,n2,sum1):
        self.count+=1
        list4=[]

        gen2 = {z for z in range(len(list1)) if list1[z]==sum1} #if an element = total return True
        for z in gen2:
            self.count+=1
            print ("found in",list1)
            return True
        if sum1!=0 and len(list1)<1:#if the length of list 1 is empty, it must be false for this fork
            return False
        if n2<1:# if the length of list 3 is empty, it msut be false for this fork
            return False
        add=self.S[n2]
        list3=[x+add for x in list1] #add the bottom element to all the values

        del list3[n2]
        gen = {y for y in range(len(list3)) if list3[y]<=sum1}
        for y in gen: #this bit creates a new list without elements greater then t
            self.count+=1
            list4.append(list3[y])
        list3=list4
        print ("fork 1 with set",list3)
        print ("fork 2 with set",list1)
        return self.Dynamic_imp(list3,n2-1,sum1) or self.Dynamic_imp(list1,n2-1,sum1)#forks the code with one side doing the added list and the other the orginal
    
            
    


        
        

    def try_greedy_search(self):
        total = 0
        count=0
        while count<self.n and total!=self.t:#if it is in the range of the list and the current total != t
            if self.S[count]+total<=self.t: # if adding doesnt taking it over t
                total+=self.S[count] #add it
                print ("old total =",total-self.S[count],", add", self.S[count],"New total =",total)
            count+=1

        print (total)



    def polynominal_time(self):
        S1 = []

        if sum(self.S)<self.t: #if t is greater then the total sum it must be false
            print ("t",self.t,"is greater then total sum",sum(self.S))
            return False

        if self.S[self.n-1]>self.t and self.t!=0:#if t is less then the smallest element it must be false
            print ("t",self.t,"is less then smallest element",self.S[self.n-1])
            return False

        for i in range(self.n):#if t is equal to an element it must be true (this runs O(n) times)
            if self.S[i] == self.t:
                print ("t",self.t," is equal to element", self.S[i])
                return True

        if self.t == 0: #if t is empty it msut be true as an empty set makes 0
            print ("t is 0 so can be made from empty set {}")
            return True

        if sum(self.S)==self.t: #if the sum == t then it must be true
            print ("t",self.t,"is equal to total sum",sum(self.S))
            return True

        for y in range(self.n): #removes all elements greater than t
            if self.S[y]<=self.t:
                S1.append(self.S[y])
        self.S=S1
        self.n=len(S1)



#tries both a yes and a any instance    
instance = SSP()
instance.random_yes_instance(8, bitlength=4)
print( instance )

instance.try_at_random()
instance.try_Exaust_search()
instance.try_Dynamic_search()
instance.try_greedy_search()



instance.random_instance(8, bitlength=4)
print( instance )
instance.count=0

    
instance.try_at_random()
instance.try_Exaust_search()
instance.try_Dynamic_search()
instance.try_greedy_search()

