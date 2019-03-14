from flask import session, render_template, redirect, url_for, Response
from controller.modules.home import home_blu
from controller.utils.camera import VideoCamera

video_camera = None
global_frame = None


# 主页
@home_blu.route('/')
def index():
    # 模板渲染
    username = session.get("username")
    if not username:
        return redirect(url_for("user.login"))
    return render_template("index.html")


# 获取视频流
def video_stream():
    global video_camera
    global global_frame

    if video_camera is None:
        video_camera = VideoCamera()

    while True:
        frame = video_camera.get_frame()

        if frame is not None:
            global_frame = frame
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + global_frame + b'\r\n\r\n')


# 视频流
@home_blu.route('/video_viewer')
def video_viewer():
    # 模板渲染
    username = session.get("username")
    if not username:
        return redirect(url_for("user.login"))
    return Response(video_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
