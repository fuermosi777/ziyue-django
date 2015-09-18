# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import subprocess
import uuid
from api.decorators import domain_verify
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
#@domain_verify
def main(request):
    if request.method != 'POST':
        return HttpResponse(status=400)
    body = request.POST.get('body', None)
    if not body:
        return HttpResponse(status=503)
    body = ''.join(set(body)) # rm duplicate
    body = body.encode('utf8') # encode
    font_id = uuid.uuid4()
    subprocess.call(['java', '-jar', 'font/dist/tools/sfnttool/sfnttool.jar', '-e', '-s', '%s'%body, 'font/fonts/PingFangRegular.ttf', 'font/serve/%s.eot'%font_id])
    subprocess.call(['java', '-jar', 'font/dist/tools/sfnttool/sfnttool.jar', '-w', '-s', '%s'%body, 'font/fonts/PingFangRegular.ttf', 'font/serve/%s.woff'%font_id])
    content = '@font-face {font-family: "ziyuepf"; font-style: normal; font-weight: normal; src: url(/fonts/%s.eot) format("eot"); url(/fonts/%s.woff) format("woff"); }'%(font_id, font_id)
    return HttpResponse(content, content_type='text/css')