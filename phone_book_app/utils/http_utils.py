import json

def getPayload(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    return body