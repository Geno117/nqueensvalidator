#!/usr/bin/python
samarrls = [4, 2, 7, 3, 6, 8, 5, 1]
def qcheck(arrls):
	print("arrls")
	#for each el generate a lists of conflicting positions for each column
	i=0
	n=len(samarrls)
	for i in range(n):
		print(i)
		invls=invmvgen(i,samarrls[i],n) #{{},{},{}}
		for o in range(i+1,n):
			if samarrls[o] in invls[o-i]:
				print("invalid")
				return False
	return True

def invmvgen(qcol,qrow,n): #return ls of invalid positions {{},{},{}}
	ls=[]
	for x in range(qcol+1,n):
		nls=[]
		nls.append(qrow)
		#check if diagonal is above the bounds
		if(qrow+(x-qcol)<(n)):
			nls.append(qrow+(x-qcol))
		if(qrow-(x-qcol)>=(0)):
			nls.append(qrow-(x-qcol))
		ls.append(nls)
		print(ls)
	return ls


invmvgen(0,4,8)

qcheck([4, 2, 7, 3, 6, 8, 5, 1])
'''


singlecheck(qcol,qrow): #return ls of invalid positions v
	ls={}
	#columns are from 0-7
	num_cols_2_check = 8-qcol -1 # unnecessary
	for x in range(qcol+1,7):
		colls={}
		colls.append(qrow)
		if (qrow-(x-qcol)>=0):
			colls.append(qrow-(x-qcol))
		if (qrow+(x-qcol))<7
'''



'''
6  . . Q . . .
5  . . . . . Q
4  . Q . . . .
3  . . . . Q .
2  Q . . . . .
1  . . . Q . .
   a b c d e f
   '''

'''
process
starting from the right most,
generate opposing positions
check with the rest of the positions if they invalidate this
if invalid return false
print the invalid positions
else continue evaluation

{4, 2, 7, 3, 6, 8, 5, 1} sample arrls
'''