from __future__ import print_function
#IP转数字
def ip2int(ip):
    try:
        hexn=''.join(["%02X" %int(i) for i in ip.split('.')])
    except Exception:
        hexn=''.join(["%02X" %int(i) for i in '0.0.0.0'.split('.')])
    return int(hexn,16)

with open('ipdata.csv','rb') as f:
    info=f.readlines()
    c=[]
    for line in info:
        line=line.decode(encoding='utf-8')
        sinfo=line.strip().split(',',4)
        c1,c2,c3,c4,c5=sinfo[0],ip2int(sinfo[1]),ip2int(sinfo[2]),sinfo[3],sinfo[4]
        cl1=(c2,c3,c4,c5)
        c.append(cl1)
# print(c[:10])
import pymysql
con=pymysql.connect(host="localhost",user="root",passwd="root",db="contact",charset='utf8')
cur=con.cursor()
#
# # for i in c[0]:
# #     print(c[0])
# #     ret=cur.execute("insert into ipdata values (%s,%s,%s,%s,%s)",i)
# cur.execute("insert into ipdata values (null,%s,%s,%s,%s)",c[0])
# for i in range(len(c)//1000+1):
#     tempc=c[i*1000:(i+1)*1000]   #每次插入1000条 防止数据库崩溃
#     ret=cur.executemany("insert into ipdata values(null,%s,%s,%s,%s)",tempc)
# cur.execute("commit")
# con.commit()
# for i in range(10):
#     tempc=c[i]
#     ret=cur.executemany("insert into ipdata values(NULL ,%s,%s,%s,%s)",tempc)
# cur.execute("commit")
#数字转IP
def int2ip(n):
    d = 256 * 256 * 256
    q = []
    while d > 0:
        m,n = divmod(n,d)
        q.append(str(m))
        d = d//256
    return '.'.join(q)

#数据库查询优化
import  random,time
ip_list=map(lambda x:x[1],random.sample(c,100))
t1=time.time()
# for i in ip_list:
#     cur.execute("select *from ipdata where %s BETWEEN startip and endip",i)
# t2=time.time()
# print(t2-t1)
#优化
'''
1.数据库中添加索引 startip endip
2.SELECT *from ipdata where %s>=startip order by startip Desc LIMIT 1,i 试用于ip数据库连续
'''
# for i in ip_list:
#     ret=cur.execute("SELECT *from ipdata where %s>=startip order by startip Desc LIMIT 1",i)

'''
3.100条语句一起执行

'''
sql_tmp="SELECT {0}. *from (select *from ipdata where %s>=startip order by startip Desc LIMIT 1){0}"
l=list(ip_list)
sql_list=[]
for i in range(len(l)):
    sql_list.append(sql_tmp.format("t"+str(i))%l[i])
sql=' union all '.join(sql_list)
cur.execute(sql)
for i in cur.fetchall():
    print(i)