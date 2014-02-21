from django.shortcuts import render_to_response

def home(request):
    user = request.user

    return render_to_response('votebean/main.html', {
        'test': 'test',
        'user': user,
    })
