from django.shortcuts import render
from matplotlib.style import context

# Create your views here.
def search_view(request):
    query = request.GET.get('q')

    context = {
        "query":query
    }
    template = "search/results.html"
    if request.htmx:
        template = "search/partials/results.html"
    return render(request, template, context)