

# print("請輸入：",end="")
# r=input("")
# if r.find("a")!=-1:
# 	print("你好")
# elif r.find("b")!=-1:
# 	print("哈囉")
# else:
# 	print("哈哈哈")
# print("剛剛你輸入了：",r)

# x="a,b,c,d,e,f"
# z=x.split(",")
# for i in z:
# 	print(i)

# x=input("請輸入生日：")
# z=x.split("-")
# print(z[0],"年")
# print(z[1],"月")
# print(z[2],"日")

# x=["A","B","C"]
# z="-".join(x)
# print(z)

# x=[input("國家："),input("城市："),input("地址：")]
# z="".join(x)
# print(z)

# import sys
# print(sys.argv)

# import sys as s
# print(s.argv)

# from sys import argv
# print(argv)

# import os
# os.system("dir")
# os.system("notepad.exe")
# os.system("tasklist")

# p=os.popen("tasklist")
# x=p.read()
# x=x.split("\n")
# y=False
# for a in x:
# 	if a.find("notepad.exe")!=-1:
# 		y=True

# if y==True:
# 	print("記事本已開啟")
# else:
# 	os.system("notepad.exe")
import codecs
# f=codecs.open("1.txt", "r", "utf8")
# # f.write("ABC")
# x=f.read()
# f.close()

# print(x)

# f=codecs.open("1.jfif", "rb")
# x=f.read()
# f.close()

# f=codecs.open("2.jfif", "wb")
# f.write(x)
# f.close()


# with codecs.open("1.jfif", "rb") as f:
# 	x=f.read()

# with codecs.open("2.jfif", "wb") as f:
# 	f.write(x)

import os
# os.remove("2.jfif")
# os.mkdir("xxx")
# os.rmdir("xxx")

# r=os.listdir("../googlemap_extension/")
# for d in r:
# 	print(d)

# print("=====================")
# print("工作路徑：",os.getcwd())
# print(os.listdir("./"))

# print("=====================")
# os.chdir("../googlemap_extension/")
# print("工作路徑：",os.getcwd())
# print(os.listdir("./"))

# print(os.path.isdir("../googlemap_extension/"))
# print(os.path.exists("../googlemap_extension/"))

# print(os.path.basename("D:/python/2020-06-20.py"))
# print(os.path.dirname("D:/python/2020-06-20.py"))
# print(os.path.getsize("D:/python/2020-06-20.py"))

# def read_dir(r,t):
# 	z=os.listdir(r)
# 	for d in z:
# 		if os.path.isdir(r+"/"+d)==True:
# 			read_dir(r+"/"+d,t)
# 		if d.find(t)!=-1:
# 			print(r+"/"+d)

# read_dir("D:/googlemap_extension","css")

x=""
while x!="0":
	os.system("cls")
	fileList=[]
	dirList=[]
	for d in os.listdir("./"):
		if os.path.isdir(d)!=True:
			fileList+=[d]
		else:
			dirList+=[d]
	if x=="1":
		for i in range(0,len(fileList),1):
			print(i,fileList[i])
		print("")
	elif x=="2":
		for i in range(0,len(dirList),1):
			print(i,dirList[i])
		print("")
	elif x=="3":
		for i in range(0,len(fileList),1):
			print(i,fileList[i])
		print("")

		p=input("請輸入檔案索引：")
		os.system("cls")
		print("================檔案開始================")
		with codecs.open(fileList[int(p)],"r","utf8") as f:
			print(f.read())
		print("================檔案結束================")
		print("")
		
	elif x=="4":
		print("xxxx")

	print("工作路徑：",os.getcwd())
	print("(0) 離開程式")
	print("(1) 列出檔案")
	print("(2) 列出資料夾")
	print("(3) 顯示檔案內容")
	print("(4) 刪除檔案")
	print("(5) 執行檔案")
	x=input("操作：")