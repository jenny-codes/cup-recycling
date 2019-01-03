from interaction.views import render
from IPython import embed
def index(request):

    context = {}
    embed()
    return render(request, 'index.html', context=context)
