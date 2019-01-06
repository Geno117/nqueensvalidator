#!/usr/bin/python

qcheck(arrls):
	#for each el generate a lists of conflicting positions for each column

singlecheck(qcol,qrow):
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
6  . . Q . . .
5  . . . . . Q
4  . Q . . . .
3  . . . . Q .
2  Q . . . . .
1  . . . Q . .
   a b c d e f
   '''
