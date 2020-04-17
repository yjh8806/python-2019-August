from django.shortcuts import render

# Create your views here.

from .models import Board

def board(request):
    qs = Board.objects.all()
    context = {
        'board' : qs,
    }

    return render(request, 'board/board.html', context)