from random import randint, sample
from itertools import chain, combinations
from time import time

class SSP():
    def __init__(self, S=[], t=0):
        self.S = S
        self.t = t
        self.n = len(S)
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
            candidate = sample(self.S, randint(0,self.n))
            total     = sum(candidate)
            print( "Trying: ", candidate, ", sum:", total )

    def try_Exaust_search(self):
        candidate=[]
        total     = sum(candidate)
        print( "Trying: ", candidate, ", sum:", total )
        v=0
        if total == self.t:
            return 0
        for j in range ((self.n)):
            v+=1
            print (j)
            for i in range (self.n-j):
                v+=1
                if j==0:
                    candidate.append(self.S[i])
                    total     = sum(candidate)
                    print( "Trying: ", candidate, ", sum:", total )
                    if total == self.t:
                        return 0
                    candidate =[]
                else:
                    for l in range (self.n-j):
                        v+=1
                        candidate.append(self.S[i])
                        for n in range(j):
                            v+=1
                            if 1+i+l+n<self.n:
                                candidate.append(self.S[1+i+l+n])
                        if len(candidate)==j+1:
                            total     = sum(candidate)
                            print( "Trying: ", candidate, ", sum:", total )
                            if total == self.t:
                                return 0
                        candidate =[]
        print ("candidate not found")

    def try_Dynamic_search(self):
        candidate=[]
        for i in range(self.n):
            if self.S[i]<=self.t:
                candidate.append(self.S[i])
                print( "Trying: ", candidate, ", sum:", candidate[len(candidate)-1] )
                for j in range (len(candidate)):
                    if candidate[j]==self.t:
                        print ("found")
                        return 0
                    else:
                        for m in range(len(candidate)):
                            if candidate[m]+self.S[i+1]<=self.t and i+1<self.n:
                                candidate[m]+=self.S[i+1]
                    print( "Trying: ", candidate, ", sum:", candidate[len(candidate)-1])
                    for k in range (len(candidate)):
                        if candidate[k]==self.t:
                            print ("found")
                            return 0

    def try_greedy_search(self):
        total = 0
        count=0
        while count<self.n and total!=self.t:
            if self.S[count]+total<=self.t:
                total+=self.S[count]
                print ("old total =",total-self.S[count],", add", self.S[count],"New total =",total)
            count+=1

        print (total)

    def try_grasp_search(self):
        total = 0
        while 
              greedy_candidate =try_random_greedy_search()
              grasp_candidate = local_search(greedy_candidate)
              if f(grasp_candidate) < self.t-total:
                  total = grasp_candidate
        return total

  def try_random_greedy_search(self):
        total = 0
        count=0
        while count<self.n and total!=self.t:
            if self.S[count]+total<=self.t:
                total+=self.S[count]
                print ("old total =",total-self.S[count],", add", self.S[count],"New total =",total)
            count+=1

        print (total)

    
instance = SSP()
instance.random_yes_instance(5, bitlength=8)
print( instance )
#{x for x in s if x<5}
#instance.try_at_random()
#instance.try_Exaust_search()
#instance.try_Dynamic_search()
instance.try_greedy_search()
