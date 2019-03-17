'''尽人事，听天命'''
from datetime import datetime
from apps import db,app


#父类
class Base(object):
    creare_time = db.Column(db.DateTime , default=datetime.now())
    update_time = db.Column(db.DateTime , default=datetime.now())

#管理员表
class Admin(Base,db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable = False)
    pass_hash = db .Column(db.String(200),nullable=False)

table_user_news = db.Table('user_collection',
                           db.Column('id',db.Integer,primary_key=True),
                           db.Column('user_id',db.Integer,db.ForeignKey('user.id')),
                           db.Column('news_id',db.Integer,db.ForeignKey('news.id')))





class User(Base,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    nick_name = db.Column(db.String(20),index=True)
    password_has = db .Column(db.String(200),nullable=False)
    mobile = db .Column(db.String(11),nullable=False)
    avatar_url = db.Column(db.String(256))
    last_login = db.Column(db.DateTime)
    signature = db.Column(db.String(512))
    gender = db.Column(db.String(10),default='Man',nullable=False)
    new = db.relationship('News',backref = 'author',lazy = 'dynamic')
    news_collection = db . relationship('News' , secondary = table_user_news
                                        ,backref = 'users' , lazy = 'dynamic')

#新闻分类表
class Category(Base,db.Model) :
    __tablename__ = 'category'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30))
    relate_news = db.relationship('News',backref = 'relate_category' , lazy = 'dynamic')


class News(Base,db.Model) :
    __tablename__ = 'news'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(30))
    source = db.Column(db.String(30))
    index_image_u = db.Column(db.String(100))
    digest = db.Column(db.String(255))
    clicks = db.Column(db.Integer)
    content = db.Column(db.Text)
    category_id = db.Column(db.Integer , db.ForeignKey('category.id'))
    user_id = db.Column(db.Integer , db.ForeignKey('user.id'))
    status = db.Column(db.Integer)
    reason = db.Column(db.String(100))

    def to_dict(self):
        new_dict = \
            {
                'id':self.id,
                'title':self.title,
                'source':self.source,
                'index_image_u':self.index_image_u,
                'digest':self.digest,
                'clicks':self.clicks,
                'content':self.content,
                'category_id':self.category_id,
                'user_id':self.user_id,
                'status':self.status,
                'reason':self.reason,
                'creare_time':self.creare_time.strftime('%Y-%m-%D %H:%M:%S')
            }


@app.route('/')
def qwe():
    return '少年郎ojbk了'


#