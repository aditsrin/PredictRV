import random
import numpy as np
import numpy.polynomial.polynomial as poly
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def GenerateUtility( rv,rounds):
	l=[]
	l.append(rv);
	for i in range(1,rounds+1):
		l.append(float((l[i-1]+1)*(l[i-1]+1))/4)
	return l



############# Generating random reservation values #########
def generaterandomRV(random_rv,intervals,dif):
	temp1=0
	for i in xrange(0,intervals+1):
		#print (i*float(rv_high-rv_low)/intervals);
		if(i!=0):
			#rv = random.uniform(temp1,(i*float(dif)/intervals))
			rv=temp1+((i*float(dif)/intervals)-temp1)/2
			#print rv
			random_rv.append(float("{0:.4f}".format(rv)))
			temp1=i*float(dif)/intervals;
		#random_rv.append((i*float(rv_high-rv_low)/intervals));

	#print random_rv
#############################################################

def generatereservationvalue(flag,roundnum,RV,inc):
	if(flag==1):
		if(roundnum==2):
			return 0.2
		elif((roundnum-1)%20==0):
			#l=[0.0,0.25,0.5,0.75]
			l= [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
			lower=[]
			higher=[]
			#print RV[roundnum-2]
			for i in l:
				if(i<RV[roundnum-2] or (RV[roundnum-2]==0 and i==0)):
					lower.append(i)
				else:
					higher.append(i)
			# print higher
			# print lower
			if(inc==1):
				if(random.uniform(0,10)>7):
					return random.choice(higher)
				else:
					return random.choice(lower)
			else:
				if(random.uniform(0,10)>3):
					return random.choice(higher)
				else:
					return random.choice(lower)
		else:
			return RV[roundnum-2]

	elif(flag==2):
		if(roundnum==1):
		 	return random.choice([0.2,0.4,0.6,0.8])
		elif((roundnum)%(Deadline/5)==0):
			return random.choice([0.2,0.4,0.6,0.8])
		else:
			return RV[len(RV)-1]
	elif(flag==3):
		#l=[0.2,0,0.5,0.25,0.75]
		l=[0.51,0.52,0.54,0.55,0.75]
		#l=[0,1]
		#l=[0,1,0,1,0]
		#l=[0,1,0,1,0,1,0,1,0,1]
		#l=[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
		#l=[0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.75,0.25,0.75]
		return l[(roundnum-1)/20]
	elif(flag==4):
		#l=[0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.76, 0.76, 0.76, 0.76, 0.76, 0.76, 0.76, 0.76, 0.76, 0.76, 0.76, 0.76, 0.76, 0.76, 0.76, 0.76, 0.76, 0.76, 0.76, 0.76, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9]
		#l=[0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.4831, 0.4831, 0.4831, 0.4831, 0.4831, 0.4831, 0.4831, 0.4831, 0.4831, 0.4831, 0.4831, 0.4831, 0.4831, 0.4831, 0.4831, 0.4831, 0.4831, 0.4831, 0.4831, 0.4831, 0.5298, 0.5298, 0.5298, 0.5298, 0.5298, 0.5298, 0.5298, 0.5298, 0.5298, 0.5298, 0.5298, 0.5298, 0.5298, 0.5298, 0.5298, 0.5298, 0.5298, 0.5298, 0.5298, 0.5298, 0.925, 0.925, 0.925, 0.925, 0.925, 0.925, 0.925, 0.925, 0.925, 0.925, 0.925, 0.925, 0.925, 0.925, 0.925, 0.925, 0.925, 0.925, 0.925, 0.925, 0.2056, 0.2056, 0.2056, 0.2056, 0.2056, 0.2056, 0.2056, 0.2056, 0.2056, 0.2056, 0.2056, 0.2056, 0.2056, 0.2056, 0.2056, 0.2056, 0.2056, 0.2056, 0.2056, 0.2056]
		l= [0.0, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.49, 0.49, 0.49, 0.49, 0.49, 0.49, 0.49, 0.49, 0.49, 0.49, 0.49, 0.49, 0.49, 0.49, 0.49, 0.49, 0.49, 0.49, 0.49, 0.49, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]

		return l[roundnum-1]
#############################################################


if __name__ == '__main__':
	#RV=[0.0, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.4]
	RV=[]
	weights = []
	random_rv=[]
	intervals=2
	Deadline = 100
	belief_plots = []
	counter = []
	probabilities = []
	weighted_utility=[]
	actual_utility=[]
	Utilities=[]
	x=[]
	for i in xrange(0,intervals):
		belief_plots.append([0])
		weights.append(0)
		counter.append(0)
		probabilities.append(0.5)

	total=0	
	generaterandomRV(random_rv,intervals,1)
	inc=1
	#print random_rv
	for rv in random_rv:
		Utilities.append(GenerateUtility(rv,Deadline))

	for roundnum in xrange(1,Deadline+1):
		if(roundnum==1):
			RV.append(0.0)
		else:
			RV.append(float("{0:.4f}".format(generatereservationvalue(2,roundnum,RV,inc)) ))
			if(RV[roundnum-1]<RV[roundnum-2]):
				inc=-1

		utility_RV=GenerateUtility(RV[roundnum-1],Deadline)	
		if(roundnum>1):
			if(RV[roundnum-1] < 0.5 ):
				ind=0
			else:
				ind=1
			counter[ind]+=1
			
			
			total+=1
			for i in xrange(0,len(counter)):
				weights[i]=float(counter[i])/total
				belief_plots[i].append(weights[i])
				probabilities[i]=weights[i]
			# summation=0
			# for i in xrange(0,len(weights)):
			# 	weights[i]=math.pow(2,counter[i])
			# 	summation+=weights[i]

			# for i in xrange(0,len(weights)):
			# 	weights[i]=float(weights[i])/summation
			# 	belief_plots[i].append(weights[i])
			# 	probabilities[i]=weights[i]
		else:
			belief_plots[i].append(0)
				
		combined_utility=0	
		for i in xrange(0,len(probabilities)):	
			combined_utility+=probabilities[i]*Utilities[i][len(Utilities[i])-roundnum-1]

		weighted_utility.append(float("{0:.4f}".format(combined_utility)) )
		actual_utility.append(float("{0:.4f}".format(utility_RV[len(utility_RV)-roundnum-1])))
		x.append(roundnum)
		
	################# Belief Plots #################
	plt.figure(3)	
	plt.plot(RV,'ro')
	for i in xrange(0,len(belief_plots)):
		if(i==0):
			plt.plot(belief_plots[i],'g--')
		elif(i==1):
			plt.plot(belief_plots[i],'b--')
	#print x
	################################################

	############## Comparing the 2 residual errors ##############
	Actual_error=0
	Weights_error=0
	for i in xrange(2,6):
		Actual_fit=np.polyfit(x,actual_utility,i,full=True)
		Generated_fit=np.polyfit(x,weighted_utility,i,full=True)
		if(i==2):
			Actual_error=Actual_fit[1]
			Weights_error=Generated_fit[1]	
			Actual_index=i
			Weights_index=i
		else:
			if(Actual_fit[1]<Actual_error):
				Actual_error=Actual_fit[1]
				Actual_index=i
			if(Generated_fit[1]<Weights_error):
				Weights_error=Generated_fit[1]	
				Weights_index=i
	plt.figure(1)
	y=actual_utility
	coefs = poly.polyfit(x, actual_utility, Actual_index)
	ffit = poly.polyval(x,coefs)

	# print coefs
	# print Actual_fit[0]
	#plt.ylim(0,1)
	plt.plot(ffit,'g--')
	plt.plot(actual_utility,'r--')
	plt.xlabel('Tims Algorithm')

	print RV
	print "last bid of Tims utilities: " + str(actual_utility[len(actual_utility)-1]) + " avg of Tims Utility: "+ str(np.mean(actual_utility))
	print "last bid of learnt utilities: " + str(weighted_utility[len(weighted_utility)-1]) +" avg of learnt Utility: "+ str(np.mean(weighted_utility))
	print Actual_error
	print Weights_error
	print "Actual's degree: " + str(Actual_index) + " Learning's degree:  " + str(Weights_index)

	plt.figure(2)
	y=weighted_utility
	coefs = poly.polyfit(x, weighted_utility, Weights_index)
	ffit = poly.polyval(x,coefs)
	#plt.ylim(0,1)
	plt.plot(x,ffit,'g--')
	plt.plot(x,weighted_utility,'r--')
	plt.xlabel('Learning Algorithm')

	plt.show()

	##################################################################



