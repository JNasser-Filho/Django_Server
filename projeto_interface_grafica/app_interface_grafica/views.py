import cv2
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.conf import settings
import os
from django.http import JsonResponse

def obter_frames_camera():
    video = cv2.VideoCapture()
    ip_camera = "https://192.168.0.179:8080/video"
    video.open(ip_camera)

    while True:
        check, frame = video.read()
        _, buffer = cv2.imencode('.jpg', frame)
        jpg_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n\r\n')

def exibir_pagina_inicial(request):
    return render(request, 'home.html')  # ajuste o caminho do arquivo HTML conforme a estrutura do seu projeto

def obter_video(request):
    return StreamingHttpResponse(obter_frames_camera(), content_type="multipart/x-mixed-replace;boundary=frame")

def receber_teclas(request):
    if request.method == 'POST':
        dados = request.POST.get('teclas')
        # Faça o que quiser com os dados, como salvá-los no banco de dados
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})
