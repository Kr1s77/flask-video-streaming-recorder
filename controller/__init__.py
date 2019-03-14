import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from config import config_dict


# 设置日志(目的是将flask默认的日志和自定义的日志保存到文件中)
def setup_log(log_level):
    # 设置日志的记录等级
    logging.basicConfig(level=log_level)  # 根据配置类型设置日志等级

    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(pathname)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


# 工厂函数: 由外界提供物料, 在函数内部封装对象的创建过程
def create_app(config_type):  # 封装web应用的创建过程
    # 根据类型取出对应的配置子类
    config_class = config_dict[config_type]
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 注册蓝图对象  如果内容只在文件中使用一次, 最好在使用前才导入, 可以有效避免导入错误
    from controller.modules.home import home_blu
    app.register_blueprint(home_blu)
    from controller.modules.user import user_blu
    app.register_blueprint(user_blu)

    # 设置日志
    setup_log(config_class.LOG_LEVEL)

    return app
