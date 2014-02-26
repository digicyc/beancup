from django.shortcuts import render

def home(request):
    user = request.user

    return render(request, 'votebean/main.html', {
        'request': request,
        'test': 'test',
        'user': user,
    })
