# from flask_script import Manager
from controller import create_app

# 创建APP对象
app = create_app('dev')
# # 创建脚本管理
# mgr = Manager(app)


if __name__ == '__main__':
    # mgr.run()
    app.run(threaded=True, host="0.0.0.0")

