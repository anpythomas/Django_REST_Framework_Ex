import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):

    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # takes string of JSON data and converts to Python Dict
    except:
        pass
    print(data)
    # data['headers'] = request.headers
    # print(request.headers)
    print(request.GET) # to get url query params
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)