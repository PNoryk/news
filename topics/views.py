from django.shortcuts import render


def test_cookies(request):
    request.COOKIES['hello'] = 1
    response = render(request, 'topics/test_cookies.html')
    response.set_cookie('hello', 'world')

    return response
