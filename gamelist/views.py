from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Game, GameCategories
from django.http import Http404


# Create your views here.
class GameListView(TemplateView):
    template_name = "game_list.html"
    def get_context_data(self, **kwargs):
        # context = super(GameListView, self).get_context_data(**kwargs)
        products = Game.objects.all().order_by('id')
        cat = kwargs.get("category", None)
        if cat:
            try:
                cat = cat.upper()
            except:
                raise Http404("No such category")
            if cat not in GameCategories.categoriesList:
                raise Http404("No such category")
            else:
                products = products.filter(category = cat)

        paginator = Paginator(products, 1)
        page = self.request.GET.get("page")
        currentPageSet = paginator.get_page(page)
        return {"gameQSet": currentPageSet}
