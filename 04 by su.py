import time
import colorama
import os

while True:
	colorama.init(True)
	for a in range(1,11):
		os.system("cls")
		if a >= 1 and a <= 5 :
			print(colorama.Back.RED+"  ")
			print(a)
		elif a == 6 :
			print("   "+colorama.Back.YELLOW+"  ")
			print(a)
		elif a >= 7 and a <= 9 :
			print("   "+"   "+colorama.Back.GREEN+"  ")
			print(a)
		else :
			print("   "+"   "+colorama.Back.GREEN+"  ")
			print(0)
		time.sleep(1)

