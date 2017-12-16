#conway'sGameOfLifeMK2
import os
import time
import random
def generation(field):
	newField = field
	for row in range(0,40):
		for col in range(0,40):
			nCount = 0
			if field[row][col] == '#':
				if field[(row+1)%40][col] == '#':
					nCount+=1
				if field[(row+1)%40][(col+1)%40] == '#':
					nCount+=1
				if field[(row+1)%40][(col-1)%40] == '#':
					nCount+=1
				if field[(row-1)%40][col] == '#':
					nCount+=1
				if field[(row-1)%40][(col-1)%40] == '#':
					nCount+=1
				if field[(row-1)%40][(col+1)%40] == '#':
					nCount+=1
				if field[row][(col+1)%40] == '#':
					nCount+=1
				if field[row][(col-1)%40] == '#':
					nCount+=1
				if nCount>3:
					newField[row][col]=' '
			else:
				if field[(row+1)%40][col] == '#':
					nCount+=1
				if field[(row+1)%40][(col+1)%40] == '#':
					nCount+=1
				if field[(row+1)%40][(col-1)%40] == '#':
					nCount+=1
				if field[(row-1)%40][col] == '#':
					nCount+=1
				if field[(row-1)%40][(col-1)%40] == '#':
					nCount+=1
				if field[(row-1)%40][(col+1)%40] == '#':
					nCount+=1
				if field[row][(col+1)%40] == '#':
					nCount+=1
				if field[row][(col-1)%40] == '#':
					nCount+=1
				if nCount == 2:
					newField[row][col]='#'
	return newField
def clear():
	os.system('cls')
def pause():
	os.system('pause >nul')
field = [[]]
for row in range(0,40):
	field.append([])
for row in field:
	for cell in range(0,40):
		if random.randint(1,10) >= 9:
			field[cell].append('#')
		else:
			field[cell].append(' ')
for row in field:
	rowString = ""
	for cell in row:
		rowString = rowString + cell
	print rowString
while(True):
	primeField = generation(field)
	for row in primeField:
		rowString = ""
		for cell in row:
			rowString = rowString + cell
		print rowString
	field = primeField
	print '\n==============================================================\n'
	time.sleep(2)