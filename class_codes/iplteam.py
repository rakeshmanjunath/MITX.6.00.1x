#!/usr/bin/env python

import copy
import operator

# IPL team object
class iplteam(object):
	"""Object IPL team"""
	
	def __init__(self,teamID,played,win,NRR):
		"""Init IPL team variables"""
		self.teamID=teamID
		self.played=played
		self.win=win
		self.NRR=NRR
		
	def playGame(self,result,NRR_diff):
		self.played+=1
		self.NRR+=NRR_diff
		if result=="won":
			self.win+=1
	
	def __lt__(self,other):
		if(self.win==other.win):
			return self.NRR<other.NRR
		return self.win<other.win
	
	def __str__(self):
		return self.teamID+"\t"+str(self.played)+"\t"+str(self.win)+"\t"+str(self.NRR)
		
SRH = iplteam('SRH' ,10, 7,+0.558)
GL  = iplteam('GL'  ,11, 7,-0.138)
KKR = iplteam('KKR' ,10, 6,+0.206)
DD  = iplteam('DD'  , 9, 5,+0.309)
MI  = iplteam('MI'  ,10, 5,-0.447)
RCB = iplteam('RCB' , 9, 4,+0.032)
RSP = iplteam('RSP' ,11, 3,+0.087)
KXIP= iplteam('KXIP',10, 3,-0.567)

# After RCB vs MI
MI  = iplteam('MI'  ,11, 6,-0.346)
RCB = iplteam('RCB' ,10, 4,-0.041)

# After DD vs SRH
DD  = iplteam('DD'  ,10, 6,+0.376)
SRH = iplteam('SRH' ,11, 7,+0.417)

# After MI vs KXIP
MI  = iplteam('MI'  ,12, 6,-0.435)
KXIP= iplteam('KXIP',11, 4,-0.384)

# After RCB vs GL
RCB = iplteam('RCB' ,11, 5,+0.627)
GL  = iplteam('GL'  ,12, 7,-0.747)

# After KKR vs RPS
RSP = iplteam('RSP' ,12, 3,-0.078)
KKR = iplteam('KKR' ,11, 7,+0.373)

# After KXIP vs SRH
KXIP= iplteam('KXIP',12, 4,-0.371)
SRH = iplteam('SRH' ,12, 8,+0.400)

# After MI vs DD
MI  = iplteam('MI'  ,13, 7,-0.082)
DD  = iplteam('DD'  ,11, 6,-0.038)

# After RCB vs KKR
RCB = iplteam('RCB' ,12, 6,+0.640)
KKR = iplteam('KKR' ,12, 7,+0.280)

# After RSP vs DD
RSP = iplteam('RSP' ,13, 4,+0.013)
DD  = iplteam('DD'  ,12, 6,-0.125)

# After RCB vs KXIP
RCB = iplteam('RCB' ,13, 7,+0.930)
KXIP= iplteam('KXIP',13, 4,-0.693)

# After GL vs KKR
GL  = iplteam('GL'  ,13, 8,-0.479)
KKR = iplteam('KKR' ,13, 7,+0.022)

# After DD vs SRH
DD  = iplteam('DD'  ,13, 7,-0.102)
SRH = iplteam('SRH' ,13, 8,+0.355)

# After KXIP vs RSP
KXIP= iplteam('KXIP',14, 4,-0.646)
RSP = iplteam('RSP' ,14, 5,+0.015)

# After MI vs GL
MI  = iplteam('MI'  ,14, 7,-0.146)
GL  = iplteam('GL'  ,14, 9,-0.374)

# After KKR vs SRH
# KKR = iplteam('KKR' ,14, 8,+0.022)
# SRH = iplteam('SRH' ,14, 8,+0.355)

# After RCB vs DD

# Points Table
class pointsTable(object):
	"""Maintains points table and updates based on results"""
	
	def __init__(self):
		self.table=[
			copy.deepcopy(SRH),
			copy.deepcopy(KKR),
			copy.deepcopy(RCB),
			copy.deepcopy(KXIP),
			copy.deepcopy(RSP),
			copy.deepcopy(MI),
			copy.deepcopy(GL),
			copy.deepcopy(DD)]
		self.Sorted=False
	
	def matchDay(self,team_win,team_lose,NRR_diff):
		self.Sorted=False
		for i in self.table:
			if i.teamID==team_win:
				i.playGame('won',NRR_diff)
			elif i.teamID==team_lose:
				i.playGame('lose',-1*NRR_diff)
	
	def getTable(self):
		if self.Sorted==False:
			self.table.sort()
			self.table.reverse()
			self.Sorted=True
		
		return self.table[:]

# Remaining Games
Mth_rem = [
('RCB' ,'MI'),
('SRH' ,'DD'),
('MI'  ,'KXIP'),
('RCB' ,'GL'),
('KKR' ,'RSP'),
('KXIP','SRH'),
('MI'  ,'DD'),
('KKR' ,'RCB'),
('RSP' ,'DD'),
('RCB' ,'KXIP'),
('GL'  ,'KKR'),
('DD'  ,'SRH'),
('RSP' ,'KXIP'),
('GL'  ,'MI'),
('KKR' ,'SRH'),
('DD'  ,'RCB')]

# Update for each Match done - KXIP vs RSP
Mth_rem = Mth_rem[14:16]
print 'Matches remaining: \n',Mth_rem,'\n'

def predict_league(Mth_rem,pointsTable,cmpr_ID):
	"""Using remaning matches predict which team can get 
	   through to playoffs"""
	   
	len_mth = len(Mth_rem)
#	NRR_diff = 0.05
	NRR_diff = 0.5
	predict = {'SRH':0,'RCB':0,'MI':0,'RSP':0,'GL':0,'DD':0,'KKR':0,'KXIP':0}
	
	# Loop Number of possibilities - 2**n iterations
	for itr in range(2**len_mth):
		newTable=pointsTable()
		itr_bin =bin(itr)[2:].zfill(len_mth)
		Mth_seq=[]
		
		# A single unique possibility
		for mth in range(len_mth):
			w = int(itr_bin[-1-mth])
			l = w^1
			newTable.matchDay(Mth_rem[mth][w],Mth_rem[mth][l],NRR_diff)
			Mth_seq.append((Mth_rem[mth][w],Mth_rem[mth][l]))
		
		currTable = newTable.getTable()
		
		for tbl_top in range(4):
			tt_teamID=currTable[tbl_top].__str__().split('\t')[0]

			predict[tt_teamID]+=1
			
			if(tt_teamID==cmpr_ID):
				print Mth_seq
				for entry in currTable:
					print entry
			
	for i in predict:
		predict[i]=(predict[i]*100.0)/(2**len_mth)
			
	predict = sorted(predict.items(),key=operator.itemgetter(1),reverse=True)
		
	print 'Predictions:\n',predict
	
predict_league(Mth_rem,pointsTable,'NIL')

# Updates needed
# 1. NRR calcs - as of now kept +win -lose, needs to be changed
# 2. Algorithm is 2**n costly, time needs to be reduces.
# Update with exceptions?