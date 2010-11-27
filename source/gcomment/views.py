from django.template import Context, loader
from table.models import Table
from gcomment.models import Comment, CommentForm
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render_to_response
from datetime import datetime
from django.http import HttpResponseRedirect

# Create your views here.
def index(request,table_id):
	try:
                comments=Comment.objects.filter(table=table_id)
                t = loader.get_template('gcomment/index.html')
                c = Context({'comments':comments,'table_id':table_id,})
                return HttpResponse(t.render(c))
        except Element.DoesNotExist:
                raise Http404
                return HttpResponse('Direccion incorrecta')

def create(request,table_id):
	m = 'add'
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			c=Comment(comment=form.cleaned_data['comment'],table_id=form.cleaned_data['table_id'],created=datetime.now())
			c.save()
			m = 'added'
			return HttpResponseRedirect('/gcomment/'+form.cleaned_data['table_id']+'/')
	else:
		form = CommentForm()

	return render_to_response('gcomment/create.html',{'form':form,'table_id':table_id,'action':m,})
