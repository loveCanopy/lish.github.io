import sqlalchemy
from Tools.demo.ss1 import center
from sqlalchemy import create_engine #数据库类型
from sqlalchemy.ext.declarative import declarative_base #类工厂函数
from sqlalchemy import Column,Integer,String #字段及类型数据
from sqlalchemy.orm import sessionmaker #使用事务
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import backref
import pymysql
engine=create_engine("mysql+pymysql://root:root@localhost/admin?charset=utf8",echo=True) #mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
base=declarative_base() #数据库的表的基类
class User(base):
    __tablename__='users' #表名
    id=Column(Integer,primary_key=True)
    name=Column(String(10))
    fullname=Column(String(10))
    password=Column(String(10))
    address= relationship("Address", order_by="Address.id", backref="user")
    #对象User上的Address对象集是通过User.address属性引用
    def __repr__(self):
        '''
        类实例化打印的格式
        '''
        return "<User(name='%s',fullname='%s',password='%s'>"%(self.name,self.fullname,self.password)
#创建另一张表
class Address(base):
    __tablename__="address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(32), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id')) #外键 指向 users表的id
    # user = relationship("User", backref=backref('address', order_by=id))
    #Address.user和User.address的关系来说总是双向的。
    #新出现的就是relationship()函数，这个将会告知ORM通过Address.userAddress类自身必须链接到User类。relationship()使用两个表的外键约束来判定这种链接的性质，比如说判定Address.user将会是多对一(many-to-one)关系
    #relationship()内还有另外一个函数称为backref()，它将提供一种用于反向查询的细节，比如说在对象User上的Address对象集是通过User.addresses属性引用，那么多对一的关系(many-to-one)反向总会是一对多关系(one-to-many)。还有对于Address.user和User.addresses的关系来说总是双向的
    def __repr__(self):
        return "<Address(email_address='%s')>"%self.email_address
base.metadata.create_all(engine)
# base.metadata.create_all(engine) 建表
Session=sessionmaker(bind=engine) #工厂函数创建类
session=Session() #类的实例化
#建立User表
# ed_user=User(name="yujie",fullname="yujie",password="123456")
# ed_user1=User(name="yujie1",fullname="yujie1",password="1234567")
#建立Address表
# ed_user.address=[Address(email_address="1039431593@qq.com"),Address(email_address="993026523@qq.com")]
# session.add(ed_user)
# session.add(ed_user1)
# session.commit() #提交
#连表查询
print(session.query(User.name, Address.email_address).filter(User.id==Address.user_id).filter(Address.email_address=='993026523@qq.com').all())
# session.query(User).join(Address).filter(Address.email_address=='1039431583@qq.com').first()
# our_user=session.query(User).filter_by(name="yujie").first()
# #select *from users where name="yujie" limit
# # session.commit() #提交
# print(session.query(User).all()) #select *from users
# print(session.query(User).order_by(User.id)) #select *from users order by id desc
# for i in session.query(User).filter(User.name.in_(['yu','yujie','yujie1'])):
#     print(i)   # select *from users where name in
# for i in session.query(User).filter(~User.name.in_(['yu','yujie','yujie1'])):
#     print(i)    # select *from users where name not in
# print(session.query(User).filter(User.name=="yujie").count())  # SELECT COUNT(*) FROM users
# print("======")
# #and操作和or操作
# from sqlalchemy import and_,or_
#
# for i in session.query(User).filter(and_(User.name=="yujie",User.fullname=="yujie")):
#     print(i)
# print("===")
# for i in session.query(User).filter(or_(User.name=="yujie",User.fullname=="yujie")):
#     print(i)



