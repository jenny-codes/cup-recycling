from interaction.views import render
from IPython import embed

def index(request):
    if request.session.has_key('animation'):
        request.session['animation'] = True
    else:
        request.session['animation'] = False
    return render(request, 'index.html', context={})
