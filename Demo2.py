from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy import create_engine #数据库类型
meta=MetaData()
#创建表users
users = Table('users', meta,
Column('id', Integer, primary_key=True),
Column('name', String(10)),
Column('fullname', String(10)),)
#创建表addresses
addresses = Table('addresses', meta,
Column('id', Integer, primary_key=True),
Column('user_id', None, ForeignKey('users.id')),
Column('email_address', String(20), nullable=False)
)
#连接数据库
engine=create_engine("mysql+pymysql://root:root@localhost/contact?charset=utf8",echo=True) #mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
#表加入数据库中
meta.create_all(engine)

#插入
# ins = users.insert().values(name='jack', fullname='Jack Jones')
con=engine.connect() #创建数据库连接
# con.execute(ins) #执行操作

# ins1=users.insert()
# con.execute(ins1, id=3, name='wendy', fullname='Wendy')
#批量插入
# con.execute(addresses.insert(),[
# {'user_id': 1, 'email_address' : 'jack@yahoo'},
# {'user_id': 1, 'email_address' : 'jack@msn'},
# {'user_id': 2, 'email_address' : 'www@www'},
# {'user_id': 2, 'email_address' : 'wendy@aol'},
#  ])

#选择
from sqlalchemy import select
s=select([users])
result=con.execute(s)
# for i in result:
#
# result.close()

s1=select([users,addresses]).where(users.c.id==addresses.c.user_id)
s2=select([users]).where(users.c.id==1)
result=con.execute(s2)
for i in result:
    print(i)

#删除
# con.execute(addresses.delete())
# con.execute(users.delete().where(users.c.name > 'm'))
#更新
stmt = users.update().\
        values(name='hahahhah').\
        where(users.c.id == 1)
con.execute(stmt)



