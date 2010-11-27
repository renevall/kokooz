from django.template import Context, loader
from recordlist.models import Table, Element
from django.http import Http404
from django.http import HttpResponse

# Create your views here.
def index(request,table_id):
        try:
		elements=Element.objects.filter(table=table_id)
	 	t = loader.get_template('recordlist/index.html')
	 	c = Context({'elements':elements,})
		return HttpResponse(t.render(c))
	except Element.DoesNotExist:
		raise Http404
		return HttpResponse('Direccion incorrecta')
