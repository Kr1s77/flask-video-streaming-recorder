from flask import Flask, render_template, Response, request, redirect, url_for, session

from serve.camera import VideoCamera

app = Flask(__name__)

# session 加密秘钥
app.secret_key = "fM3PEZwSRcbLkk2Ew82yZFffdAYsNgOddWoANdQo/U3VLZ/qNsOKLsQPYXDPon2t"


# 主页
@app.route('/')
def index():
    # 模板渲染
    username = session.get("username")
    if username:
        return render_template('index.html')
    return redirect(url_for("login"))


# 登录
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    # 获取参数
    username = request.form.get("username")
    password = request.form.get("password")

    # 校验参数
    if not all([username, password]):
        return render_template("login.html", errmsg="参数不足")

    # 校验对应的管理员用户数据
    if not username == "admin" and password == "admin":
        return render_template("login.html", errmsg="用户名或密码错误")

    # 验证通过
    session["username"] = username
    return redirect(url_for("index"))


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=7000)
