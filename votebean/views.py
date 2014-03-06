from django.shortcuts import render

def home(request):
    user = request.user

    return render(request, 'votebean/main.html', {
        'test': 'test',
        'user': user,
    })
