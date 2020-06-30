import webbrowser
from sys import argv


if len(argv) < 2 :
	print("請輸入網址")
else:
	url = argv[1]
	webbrowser.open(url, new=0, autoraise=True)
	print(argv[1])


