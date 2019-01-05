from interaction.views import render

def index(request):
    return render(request, 'index.html', context={})
