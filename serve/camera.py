import time

import cv2


class VideoCamera(object):
    def __init__(self):
        # 参数0是表示视频设备，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
        self.video = cv2.VideoCapture(0)
        # 如果您决定播放video.mp4，则必须在该文件夹中包含此文件
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        # 当类对象被删除时自动调用del方法,关闭摄像头
        self.video.release()

    def get_frame(self):
        # 调用read方法，获得两个返回值，如果读取帧是正确的则success=True
        # 如果文件读取到结尾，它的返回值就为False
        # img就是每一帧的图像，是个三维矩阵。
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.

        # '.jpg'表示把当前图片img按照jpg格式编码，按照不同格式编码的结果不一样 
        # 获得两个返回值，jpeg为视频流
        ret, jpeg = cv2.imencode('.jpg', image)
        # 对于 python2.7 或者低版本的 numpy 请使用 jpeg.tostring()
        # 转为二进制
        time.sleep(0.15)
        return jpeg.tobytes()
