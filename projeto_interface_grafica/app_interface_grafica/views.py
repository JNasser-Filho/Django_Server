'''from django.shortcuts import render

def home(request):
    return render(request,'usuarios/home.html')'''
   
import cv2
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.conf import settings
import os

def obter_frames_camera():
    video = cv2.VideoCapture()
    ip_camera = "https://192.168.101.2:8080/video"
    video.open(ip_camera)

    while True:
        check, frame = video.read()
        _, buffer = cv2.imencode('.jpg', frame)
        jpg_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n\r\n')

def exibir_pagina_inicial(request):
        return render(request, os.path.join(settings.BASE_DIR, 'app_interface_grafica', 'templates', 'home.html'))

def obter_video(request):
    return StreamingHttpResponse(obter_frames_camera(), content_type="multipart/x-mixed-replace;boundary=frame")
