import random
import numpy as np
import math
import operator
from scipy.stats import *
import csv


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
				RV.append( Utilities[direction-1] )

		else:
			RV.append( RV[len(RV)-1] )

	return RV

def boulwareUtilities (rv,Deadline ,beta):
	ut = []

	# beta = float(1)/beta  # for boulware behaviour

	for i in range(0,Deadline+1):
		minm = min(i,Deadline)
		time = float(minm)/Deadline
		curr_ut = rv + (1-rv)*(math.pow(time,beta))
		# print "================"
		# print minm
		# print time
		# print beta
		# print "================"
		ut.append(float("{0:.4f}".format(curr_ut)))
	return ut

def TDTrv(Deadline):
	RV=[]
	wind=0
	for i in range(0,Deadline+1):
		x=random.uniform(wind,wind+0.2)
		y=expon.cdf(x,0,1)
		RV.append(float("{0:.4f}".format(y)))
		wind=x
	return RV

if __name__ == '__main__':

	beta=1.002
	for i in xrange(0,1000):
		RV=[]

		GridSize=100
		Gridcoords=[GridSize/2 ,GridSize/2]
		RV=ReservationValues(RV,100,1,GridSize,Gridcoords) 
		#RV=boulwareUtilities(0,100,beta)
		# RV=TDTrv(100)
		with open('fire1.csv', 'a') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(RV)
		beta=beta+0.002
		#print RV