from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
#from apps.soporte.forms import NuevoForm
#from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.urls import reverse 
from soporte import views

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView
)

from soporte.models import Juego

#<----  JuegosList  ---->
class JuegoList(ListView):
	model = Juego

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs) 
		
		
		self.request.session['UltimaPagina'] = 'Lista de juegos'
		self.request.session_modified = True
		return context
#<----  JuegosList  ---->



#<----  JuegoDetail  ---->
class JuegoDetail(DetailView):
	model = Juego

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs) 
		
		
		self.request.session['UltimaPagina'] = 'Ver detalle'
		self.request.session_modified = True
		return context
#<----  JuegoDetail  ---->	



#<----  JuegoCreation  ---->
class JuegoCreation(CreateView):
	model = Juego
	success_url = reverse_lazy('soporte:list')
	fields = ['tituloJuego', 'generoJuego', 'idiomaJuego', 'numeroJugador', 'fechaLanzamiento', 'companiaJuego', 'plataformaJuego', 'editorJuego', 'imagen']

	def get (self, *args, **kwargs):
		user = self.request.user
		print("Entro")
		if(user.has_perm('soporte.add_juego')):

			return super(JuegoCreation, self).get(*args, **kwargs)
		else:

			return render(self.request,'soporte/403.html')

	def form_valid(self, form):
		usuario = self.request.user
		if(usuario.has_perm('juego.add_juego')):
			juego = self.model()
			juego.tituloJuego = form.cleaned_data['tituloJuego']
			juego.generoJuego = form.cleaned_data['generoJuego']
			juego.idiomaJuego = form.cleaned_data['idiomaJuego']
			juego.numeroJugador = form.cleaned_data['numeroJugador']
			juego.fechaLanzamiento = form.cleaned_data['fechaLanzamiento']
			juego.companiaJuego = form.cleaned_data['companiaJuego']
			juego.plataformaJuego = form.cleaned_data['plataformaJuego']
			juego.editorJuego = form.cleaned_data['editorJuego']

			if 'imagen' in self.request.FILES:
				juego.imagen = self.request.FILES['imagen']
			juego.save()

			return HttpResponseRedirect(reverse("soporte:list"))
		else:
 
 			return render(self.request,'soporte/403.html')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs) 
		
		self.request.session['UltimaPagina'] = 'Agregar juego'
		self.request.session_modified = True
		return context
#<----  JuegoCreation  ---->




#<----  JuegoUpdate  ---->
class JuegoUpdate(UpdateView):
	model = Juego
	success_url = reverse_lazy('soporte:list')
	fields = ['tituloJuego', 'generoJuego', 'idiomaJuego', 'numeroJugador', 'fechaLanzamiento', 'companiaJuego', 'plataformaJuego', 'editorJuego', 'imagen']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs) 
		
		
		self.request.session['UltimaPagina'] = 'Actualizar juego'
		self.request.session_modified = True
		return context
#<----  JuegoUpdate  ---->




#<----  JuegoDelete  ---->
class JuegoDelete(DeleteView):
	model = Juego
	success_url = reverse_lazy('soporte:list')

	def get (self, *args, **kwargs):
		usuario = self.request.user
		if(usuario.has_perm('soporte.delete_juego')):
			return super(JuegoDelete, self).get(*args, **kwargs)
		else:
			return render(self.request,'soporte/403.html')

	def form_valid(self, form):
		usuario = self.request.user
		if(usuario.has_perm('juego.delete_juego')):
			juego = self.model()
			juego.tituloJuego = form.cleaned_data['tituloJuego']
			juego.generoJuego = form.cleaned_data['generoJuego']
			juego.idiomaJuego = form.cleaned_data['idiomaJuego']
			juego.numeroJugador = form.cleaned_data['numeroJugador']
			juego.fechaLanzamiento = form.cleaned_data['fechaLanzamiento']
			juego.companiaJuego = form.cleaned_data['companiaJuego']
			juego.plataformaJuego = form.cleaned_data['plataformaJuego']
			juego.editorJuego = form.cleaned_data['editorJuego']

			if 'imagen' in self.request.FILES:
				juego.imagen = self.request.FILES['imagen']
			juego.save()

			return HttpResponseRedirect(reverse('soporte:list'))
		else:
			print("sin perm")

			return render(self.request,'soporte/403.html')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs) 
		
		self.request.session['UltimaPagina'] = 'Borrar juego'
		self.request.session_modified = True
		return context
#<----  JuegoDelete  ---->




#<----  search  ---->
def search(request):
	template_name = 'soporte/buscador.html' 
	success_url =  'soporte/juego_list.html'
	
	if(request.method == 'POST'):
		campo=request.POST.get('busqueda','')
		print(campo)
		if(campo == ''):
			return(render(request,template_name))
		else:

			resultado=Juego.objects.filter(
				tituloJuego__icontains=campo
			)
			for res in resultado:
				print(res.tituloJuego)
			contexto = {'busqueda': campo, 'object_list': resultado}
			return(render(request, success_url,contexto))
	return(render(request,template_name))

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs) 
			
		self.request.session['UltimaPagina'] = 'Buscador'
		self.request.session_modified = True
		return context


		
#<----  search  ---->
	



# Create your views here.

def index(request):
	#print('Base dir:' + settings.BASE_DIR)
	#print(settings.STATIC_URL)
	#print('Staticfiles dir: ' + settings.STATICFILES_DIR)
	#print('Static root: ' + settings.STATIC_ROOT)
	return render(request, 'plantillas/index.html')

#def nuevo_view(request):
#	if request.method == 'POST':
#		form = NuevoForm(request.POST)
#		if forms.is_valid():
#			form.save()
#		return HttpResponseRedirect('soporte:index')
#	else:
#		form = NuevoForm()
#		print(form)
#		print(request)
#		return render(request, 'plantillas/nuevo_form.html', {'form':form})

#def juego_list(request):
#	juego = Juego.objects.all()
#	contexto = {'juegos': juego }
#	return render(request, 'plantillas/juego_list.html', contexto)