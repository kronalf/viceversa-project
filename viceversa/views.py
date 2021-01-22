from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def reverse(request):
    user_text = request.GET['usertext']
    number_words = user_text.split(' ')
    count = len(number_words)
    if count > 1:
        s = 's'
    else:
        s = ''
    reverse_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext':user_text, 'reversetext':reverse_text, 'count':count, 's':s})
