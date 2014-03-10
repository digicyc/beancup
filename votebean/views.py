from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import VoteBean
from bean.models import Bean


def home(request):
    user = request.user

    return render(request, 'votebean/main.html', {
        'bean_id': '1',
        'user': user,
    })


@login_required
def add_vote(request):
    if request.method == 'GET':
        bean_id = request.GET['bean_id']

        if bean_id:
            bean = Bean.objects.get(id=bean_id)
            vote_bean = VoteBean(voter=request.user, bean_type=bean, vote_count=1)
            vote_bean.save()

    return render(request, 'votebean/main.html')


