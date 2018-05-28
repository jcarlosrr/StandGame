from django import forms
from apps.soporte.models import Juego
from django.forms import ModelForm

class NuevoForm(ModelForm):


	class Meta:

		model = Juego

		fields = '__all__'

		''' [

			'IdJuego',
	    	'TituloJuego', 
	    	'IdGenero',
	    	'IdiomaJuego', 
	    	'NumeroJugador',
	    	'FechaLanzamiento',
		]
		labels = {
			'IdJuego': 'Id del juego',
	    	'TituloJuego': 'Titulo del juego', 
	    	'IdGenero': 'Id del genero',
	    	'IdiomaJuego': 'Idioma del juego', 
	    	'NumeroJugador': 'Numero de jugadores',
	    	'FechaLanzamiento': 'Fecha de lanzamiento', 
		}
		widgets = {
			'IdJuego': forms.TextInput(attrs={'class':'form-control'}),
	    	'TituloJuego': forms.TextInput(attrs={'class':'form-control'}),
	    	'IdGenero': forms.TextInput(attrs={'class':'form-control'}),
	    	'IdiomaJuego': forms.TextInput(attrs={'class':'form-control'}),
	    	'NumeroJugador': forms.TextInput(attrs={'class':'form-control'}),
	    	'FechaLanzamiento': forms.TextInput(attrs={'class':'form-control'}),
		}'''
