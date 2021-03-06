from apps import app
from modules.web.index import index_blue
from modules.web.user import user_blue
from modules.admin.admin import admin_blue
from flask_wtf import CSRFProtect

#首页，新闻展示
app.register_blueprint(index_blue,url_prefix='/')
#用户信息相关
app.register_blueprint(user_blue,url_prefix='/user')
#管理员模块
app.register_blueprint(admin_blue,url_prefix='/admin')

CSRFProtect(app)

if __name__ == '__main__':
    app.run(port=2456)