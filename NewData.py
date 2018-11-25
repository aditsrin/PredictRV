import random
import numpy as np
import math
import operator
from scipy.stats import *
import csv
import io


def getflag(direction,Gridcoords,GridSize):
	flag=0
	if(direction==1):
		if(Gridcoords[0]!=0):
			Gridcoords[0]-=1                 ### Moving North
		if(Gridcoords[1]==GridSize-1):
			flag=3
		elif(Gridcoords[1]==0):
			flag=2
		elif(Gridcoords[0]+1==GridSize-1):
			flag=4
	elif(direction==2):
		if(Gridcoords[1]!=0):
			Gridcoords[1]-=1                 ### Moving West
		if(Gridcoords[0]==0):
			flag=1
		elif(Gridcoords[1]+1==GridSize-1):
			flag==3
		elif(Gridcoords[0]==GridSize-1):
			flag=4

	elif(direction==3):
		if(Gridcoords[1]!=GridSize-1):
			Gridcoords[1]+=1                 ### Moving East
		if(Gridcoords[0]==GridSize-1):
			flag=4
		elif(Gridcoords[0]==0):
			flag=1
		elif(Gridcoords[1]-1==0):
			flag=2
	else:
		if(Gridcoords[0]!=GridSize-1):
			Gridcoords[0]+=1                 ### Moving South
		if(Gridcoords[0]-1==0):
			flag=1
		elif(Gridcoords[1]==GridSize-1):
			flag=3
		elif(Gridcoords[1]==0):
			flag=2
	return flag
	
#############################################################

def ReservationValuesnext(RV,Deadline,UpdateRate,GridSize,Gridcoords):
	Utilities=[0.75,0.57,0.321,0.12]
	# direction=random.randint(1,4)
	direction=random.choice([1,4])
	flag=getflag(direction,Gridcoords,GridSize)
	
	if(flag==0 ):
		return  Utilities[direction-1] 

	else:	
		return max (Utilities[flag-1], Utilities[direction-1] )

def ReservationValues(RV,Deadline,UpdateRate,GridSize,Gridcoords):
	ManPower=[12,10,7,4]
	Utilities=[0.75,0.57,0.321,0.12]

	RV=[]
	for roundnum in xrange(0,100):
		if(roundnum==0):
			direction=random.randint(1,4)
			# direction=random.choice([1,4])
			### Gridcoords Updation 
			flag=getflag(direction,Gridcoords,GridSize)
			
			if(flag==0 ):
				RV.append( Utilities[direction-1] )
				

			else:	
				print "This case: "+str(flag) + " "+ str(ManPower[direction-1] )
				RV.append( max (Utilities[flag-1], Utilities[direction-1] ) )

		elif(roundnum%UpdateRate==0):  
			direction=random.randint(1,4)
			# direction=random.choice([1,4])
			flag=getflag(direction,Gridcoords,GridSize)
			
			if(flag==0 ):
				RV.append( Utilities[direction-1] )

			else:	
				RV.append( max (Utilities[flag-1], Utilities[direction-1] ))

		else:
			RV.append( RV[len(RV)-1] )

	return RV

def boulwareUtilities (rv,Deadline,UpdateRate ,beta):
	ut = []

	# beta = float(1)/beta  # for boulware behaviour

	for i in range(1,Deadline+1):
		if((i-1)%UpdateRate==0):
			minm = min(i,Deadline)
			time = float(minm)/Deadline
			curr_ut = rv + (1-rv)*(math.pow(time,beta))
			# print "================"
			# print minm
			# print time
			# print beta
			# print "================"
			ut.append(float("{0:.4f}".format(curr_ut)))
		else:
			ut.append(ut[len(ut)-1])
	return ut

def TDTrv(Deadline,UpdateRate ):
	RV=[]
	wind=0
	for i in range(1,Deadline+1):
		if(i-1%UpdateRate==0):
			x=random.uniform(wind,wind+0.2)
			y=expon.cdf(x,0,1)
			RV.append(float("{0:.4f}".format(y)))
			wind=x
		else:
			RV.append(RV[len(RV)-1])
	return RV


def getdelay(delay_list,prevdelay):
	p=random.randint(1,10)
	if(p<=5):
		return prevdelay
	elif(p>5 and p<8):
		#increase
		l=[]
		ind=(prevdelay/5)-1
		end=min(ind+3,len(delay_list))
		# print str(ind) + " " + str(end)
		for i in xrange(ind,end):
			l.append(delay_list[i])
		return random.choice(l)
	else:
		#decrease
		l=[]
		ind=(prevdelay/5)-1
		end=max(ind-3,0)
		# print str(end) + " " + str(ind)
		for i in xrange(end,ind+1):
			l.append(delay_list[i])
		return random.choice(l)

#############################################################


def getmeetingrv(UpdateRate,delaylist,Deadline):

	delay_list=[45,40,35,30,25,20,15,10,5]
	delaylist=[]
	RV=[]
	for roundnum in xrange(1,Deadline+1):
		if(roundnum-1==0):
			delay=random.choice(delay_list)
			delaylist.append(delay)
			utility=getdelaycost(delay)
			# print str(utility) + " " + str(delay)
			RV.append( utility )

		elif( (roundnum-1)%UpdateRate==0):
			# print "in"
			delay=getdelay(delay_list,delaylist[len(delaylist)-1])
			delaylist.append(delay)
			# print delay
			utility=getdelaycost(delay)
			# print str(utility) + " "+ str(delay)
			RV.append( utility )

		else:
			RV.append( RV[len(RV)-1] )

	delay=getdelay(delay_list,delaylist[len(delaylist)-1])	
	utility=getdelaycost(delay)
	# print str(utility) + " "+ str(delay)
	RV.append( utility )
	return RV

def getdelaycost(delay):
	
	alpha=1.2
	Value=200
	cost=math.pow(delay,alpha)*2
	maxm=Value-math.pow(5,alpha)*2
	minm=Value-math.pow(45,alpha)*2
	# print str(maxm) + " " + str(minm)
	minm=Value-math.pow(45,alpha)*2
	if(float(Value-cost -minm)/(maxm-minm) ==0):
		return 0.01
	return float("{0:.4f}".format(float(Value-cost -minm)/(maxm-minm)))


#############################################################
def generatereservationvalue(Deadline):
	l=[0.9,0.1,0.36 ,0.75, 0.75 ,0.12 ,0.75,0.12 ,0.75,0.12]
	RV=[]
	for roundnum in xrange(1,Deadline+1):
		RV.append(l[(roundnum/2)%2])
		
	return RV




if __name__ == '__main__':



	# RV=generatereservationvalue(100)
	# print RV

	# beta=1.002
	updaterates = [2,5,10,20,50]
	for UpdateRate in updaterates:
		print UpdateRate
		for i in xrange(0,1000):
			RV=[]

			# UpdateRate = 2
			# GridSize=100
			
			# Gridcoords=[GridSize/2 ,GridSize/2]
			# Gridcoords=[GridSize/2 +random.choice([-4,0,4]),GridSize/2+random.choice([-4,0,4])]

			# RV=ReservationValues(RV,100,UpdateRate,GridSize,Gridcoords)
			# nextRV = float( "{0:.4f}".format( ReservationValuesnext(RV,100,UpdateRate,GridSize,Gridcoords) ) );
			# # print nextRV
			# RV.append( nextRV)

			
			RV = getmeetingrv(UpdateRate,[],100) 
			# nextRV =float("{0:.4f}".format( getmeetingrv(RV,100,UpdateRate,delaylist,100) ) ) 
			# RV.append(nextRV)

			# RV=boulwareUtilities(0,100,2,beta)
			# RV=TDTrv(100,2)
			# with open('exponential_2_0.2.csv', 'a') as csvfile:
			with open("meeting" + str(UpdateRate) + ".csv", 'a') as csvfile:
				spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
				spamwriter.writerow(RV)
			csvfile.close()
			# beta=beta+0.0005
			#print RV