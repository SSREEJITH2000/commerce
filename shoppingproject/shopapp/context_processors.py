from .models import category
def cate_links(request):
    links=category.objects.all()
    return dict(links=links)