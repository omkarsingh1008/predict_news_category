from django.http import HttpResponse


def index(request):
    page = """
    <!Doctype html>
    <html>
    <head> <title>HOME</title></head>
    <body><div>
    <a href="app/">app</a>
    </div>
    </body>
    </html>
    """
    return HttpResponse(page)
