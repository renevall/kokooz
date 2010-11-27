from django.template import Context, loader
#Add as many models as you need
from recordlist.models import Table, Element
from mainmodel.models import Klocal, Kcategory
from django.http import Http404
from django.http import HttpResponse

# Create your views here.
def index(request):
  # read(table,template,context name,filter)
  #results = read(Klocal,'locales.html','locals',filter)
  results = read(Kcategory,'category.html','categories',filter)
  return HttpResponse(results[0].categoryname)

def read(table,template,context_name,filter):
  elements = table.objects.all()
  return elements


























#		elements=Element.objects.filter(tab le=table_id)
#	 	t = loader.get_template('recordlist/index.html')
#	 	c = Context({'elements':elements,})
#		return HttpResponse(t.render(c))
#	except Element.DoesNotExist:
#		raise Http404
#		return HttpResponse('Direccion incorrecta')
#
#
#
#def read(table,params,filter):


#tabla1,table2,tabla3

#tabla='tabla1'
#read(tabla)

#def read(table,template,contextnamei,error)
#    elemnt = $table.objects.....\
#    loader...'ruta/$template'
#    context... (contextname:element)


