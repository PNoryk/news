from django.shortcuts import render


def test_cookies(request):
    request.COOKIES['hello'] = 1
    response = render(request, 'topics/test_cookies.html')
    response.set_cookie('hello', 'world')

    return response


def bbb():
    return '    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Culpa cupiditate ea eius est et ex harum, impedit ipsa ipsam laborum laudantium magni nesciunt nihil quam quidem quod reiciendis sequi ullam!'
