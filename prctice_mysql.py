import pymysql

e=pymysql.connect(
	host="localhost",
	user="root",
	passwd="",
	db="2020-06-30",
	charset="utf8"
)

c=e.cursor()

#c.execute(
# "DELETE FROM 'news' WHERE `id` = %s"

# "INSERT INTO `news`(`title`, `source`, `create_time`,`description`)"+
# "VALUES(%(a)s, %(b)s, %(c)s, %(d)s)"
# , {
# 	"a":input("title:"),
# 	"b":input("source:"),
# 	"c":input("create time:"),
# 	"d":input("description:")
# })
c.execute("SELECT * FROM `news`")
# r = c.fetchall()
# for d in r :
# 	print(d[0], d[1], d[2])


# d = c.fetchone()
# print(d[0], d[1], d[2])

# d = c.fetchone()
# print(d[0], d[1], d[2])

# d = c.fetchone()
# print(d[0], d[1], d[2])
# d = c.fetchone()
# print(d[0], d[1], d[3])

co = c.rowcount
print(co)





# e.commit()


e.close()

