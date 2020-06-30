import os
import codecs
path = os.getcwd()
x = ""
while x!="0":
	os.system("cls")
	data=os.listdir("./")
	fileList=[]
	dirList=[]
	for d in data:
		if os.path.isdir(d)!=True:
			fileList+=[d]  
		else:
			dirList+=[d]
	if x=="1":
		for a in range(0,len(fileList),1):
			print(a,fileList[a])
		print("")
		# data = os.listdir()
		# for file in data:
		# 	if True == os.path.isfile(file):
		# 		print(file)

	elif x=="2":
		for i in range(0,len(dirList),1):
			print(i,dirList[i])
		print("") 

		# file = []
		# for file in os.listdir():
		# 	if os.path.isdir(file) == True:
		# 		print(file)
	elif x=="3":
		for i in range(0,len(fileList),1):
			print(i,fileList[i])
		print("")
		p=input("請輸入檔案索引:")
		os.system("cls")
		print("================檔案開始================")
		with codecs.open(fileList[int(p)],"r","utf8") as f:
			print(f.read())
		print("================檔案結束================")
		print("")





		# file = []
		# for file in os.listdir():
		# 	if os.path.isfile(file) == True:
		# 		print("- ", file)

	elif x=="4":
		for i in range(0,len(fileList),1):
			print(i,fileList[i])
		print("")	
		q=input("請輸入檔案索引:")
		os.system("cls")
		os.remove(fileList[int(q)])
		
	elif x=="5":
		for i in range(0,len(fileList),1):
			print(i,fileList[i])
		print("")	
		q=input("請輸入檔案索引:")	
		os.system("cls")
		os.system(fileList[int(q)])

	elif x=="6":

		for i in range(0,len(dirList),1):
			print(i,dirList[i])
		print("") 

		q=input("請輸入檔案索引:")
		# os.chdir()的指令是針對目前的路徑去變更，是屬於動作指令
		# os.getcwd() 才能重新取得目前的路徑
		# os.chdir()不會回傳新的路徑，直接讓path 去接，並不會回傳任何結果
		# 80或81行兩種指令都可以
		os.chdir("./"+dirList[int(q)])
		# path=os.chdir(path+"/"+dirList[int(q)])
		path=os.getcwd()
		os.system("cls")

		
	elif x=="7":
		for i in range(0,len(dirList),1):
			print(i,dirList[i])
		print("")	
		q=input("請輸入檔案索引:")
		os.system("cls")
		os.rmdir(dirList[int(q)])
		
	elif x=="8":
		os.chdir("../")
		path=os.getcwd()
		os.system("cls")


	print("工作路徑:",path)
	print("(0) 離開程式")
	print("(1) 列出檔案")
	print("(2) 列出資料夾")
	print("(3) 顯示檔案內容")
	print("(4) 刪除檔案")
	print("(5) 執行檔案式")
	print("(6) 進入資料夾")
	print("(7) 刪除資料夾")
	print("(8) 回上層資料夾")
	x=input("操作")
os.system("cls")