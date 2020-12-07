from django.shortcuts import render


def homepage(request):
    """
    Рендеринг домашней страницы
    """
    return render(request=request, template_name='home.html')


def infopage(request):
    """
    Рендеринг страницы информации о разработчике
    """
    return render(request=request, template_name='info.html')
