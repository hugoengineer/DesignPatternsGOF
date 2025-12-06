async def adapter_function(request, user):
    body = None

    try:
        body = await request.json()
    except Exception:
        body = {}

    headers = dict(request.headers)
    query_params = request.args
    path_params = {'user':user}

    return {
        'body': body,
        'headers': headers, 
        'query_params': query_params,
        'path_params': path_params
    }