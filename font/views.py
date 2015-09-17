# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import subprocess
import uuid
from api.decorators import domain_verify
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@domain_verify
def main(request):
    if request.method != 'POST':
        return HttpResponse(status=404)
    body = request.POST.get('body', None)
    if not body:
        return HttpResponse(status=404)

    font_id = uuid.uuid4()
    subprocess.call(['java', '-jar', 'font/dist/tools/sfnttool/sfnttool.jar', '-w', '-s', body, 'font/fonts/PingFangRegular.ttf', 'font/serve/%s.woff'%font_id])
    content = '@font-face {font-family: "Ping-Fang"; font-style: normal; font-weight: 100; src: local("PingFang"), url(/font/%s.woff) format("woff"); }'%font_id
    return HttpResponse(content, content_type='text/css')