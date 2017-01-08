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
    
    def random_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        
        self.t = randint(0,n*max_n_bit_number)
        self.n = len( self.S )

    def random_yes_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        self.t = sum( sample(self.S, randint(0,n)) )
        self.n = len( self.S )


    def try_at_random(self):
        candidate = []
        total = 0
        while total != self.t:
            self.count+=1
            print (self.count)
            candidate = sample(self.S, randint(0,self.n))
            total     = sum(candidate)
            print( "Trying: ", candidate, ", sum:", total )

    def try_Exaust_search(self):
        candidate=[]
        total     = sum(candidate)
        print( "Trying: ", candidate, ", sum:", total )
        if total == self.t:
            return 0
        for j in range (self.n):
            for i in range(j,self.n):
                
                for count in range(i,self.n):
                    candidate.append(self.S[count])
                    total     = sum(candidate)
                    print( "Trying: ", candidate, ", sum:", total )
                    if total == self.t:
                        return 0
                candidate=[]
                candidate.append(self.S[j])



    def try_Exaust_search2(self):
        candidate=self.S
        Poly=self.polynominal_time()
        if Poly == True:
            print ("found")
            print (self.count)
            return 1
        elif Poly == False:
            print ("not found")
            print (self.count)
            return 0
        if (self.Exhaust_imp(candidate,len(candidate),self.t)==True):
            print ("found")
            print (self.count)
            return 1
        else:
            print ("not found")
            return 0
                        
    def Exhaust_imp(self,list2,n,sum1):
        self.count+=1
        print("--",sum1)
        if sum1 == 0:
            return True
        if sum1!=0 and n==0:
            return False
        if (list2[n-1]>sum1):
            return self.Exhaust_imp(list2,n-1,sum1)
        print (list2)
        print (sum1)
        return (self.Exhaust_imp(list2,n-1,sum1) or self.Exhaust_imp(list2,n-1,sum1-list2[n-1]))
            
            



    def try_Dynamic_search(self):
        candidate=self.S
        self.count=0
        Poly=self.polynominal_time()
        if Poly == True:
            print ("found")
            print (self.count)
            return 1
        elif Poly == False:
            print ("not found")
            print (self.count)
            return 0
            
        if (self.Dynamic_imp(candidate,self.n-1,self.t))==True:
            print ("found")
            print (self.count)
            return 1
        else:
            print ("not found")
            print (self.count)
            return 0


    def Dynamic_imp(self,list1,n2,sum1):
        self.count+=1
        list4=[]

        gen2 = {z for z in range(len(list1)) if list1[z]==sum1}
        for z in gen2:
            #self.count+=1
            return True
        if sum1 == 0:
            return True
        if sum1!=0 and len(list1)<1:
            return False
        if n2<1:
            return False
        print ("count" , n2)
        add=self.S[n2]
        list3=[x+add for x in list1]

        list3.pop()
        gen = {y for y in range(len(list3)) if list3[y]<=sum1}
        for y in gen:
            #self.count+=1
            list4.append(list3[y])
        list3=list4
        return self.Dynamic_imp(list3,n2-1,sum1) or self.Dynamic_imp(list1,n2-1,sum1)
    
            
    


        
        

    def try_greedy_search(self):
        total = 0
        count=0
        while count<self.n and total!=self.t:
            if self.S[count]+total<=self.t:
                total+=self.S[count]
                print ("old total =",total-self.S[count],", add", self.S[count],"New total =",total)
            count+=1

        print (total)



    #def GRASP(self):
     #   for i in range(self.n):
      #      solution = GRASP_construct()
       #     solution = local_search(solution)

    #def GRASP_construct(self):
        #solution = 0



    def polynominal_time(self):
        S1 = []

        if sum(self.S)<self.t:
            return False

        if self.S[self.n-1]>self.t and self.t!=0:
            return False

        for i in range(self.n):
            if self.S[i] == self.t:
                return True

        if self.t == 0:
            return True

        if sum(self.S)==self.t:
            return True

        for y in range(self.n):
            if self.S[y]<=self.t:
                S1.append(self.S[y])
        self.S=S1
        self.n=len(S1)

    
instance = SSP()
instance.random_yes_instance(4, bitlength=8)
print( instance )

#instance.try_at_random()
#instance.try_Exaust_search()
#instance.try_Exaust_search2()
instance.try_Dynamic_search()
#instance.try_greedy_search()


instance.random_instance(4, bitlength=8)
print( instance )
instance.count=0

    
#instance.try_at_random()
#instance.try_Exaust_search()
#instance.try_Exaust_search2()
instance.try_Dynamic_search()
#instance.try_greedy_search()


