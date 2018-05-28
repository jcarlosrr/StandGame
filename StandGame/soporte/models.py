from django.db import models

# Create your models here.

class Juego(models.Model):
    tituloJuego = models.CharField(max_length=30)
    generoJuego = models.CharField(max_length=30)
    idiomaJuego = models.CharField(max_length=20)
    numeroJugador = models.CharField(max_length=20)
    fechaLanzamiento = models.DateTimeField()
    companiasJuegos = (('Nintendo', 'Nintendo'), ('Sony', 'Sony'), ('Microsoft', 'Microsoft'), ('Ubisoft', 'Ubisoft'), ('Bethesda', 'Bethesda'), ('SquareEnix', 'SquareEnix'), ('SEGA', 'SEGA'))
    companiaJuego = models.CharField(max_length=20, choices=companiasJuegos, default='MICROSOFT')
    plataformaJuegos = (('Ps4', 'Ps4'), ('Xbox One', 'Xbox One'), ('Nintendo Switch', 'Nintendo Switch'), ('Pc', 'Pc'))
    plataformaJuego = models.CharField(max_length=20, choices=plataformaJuegos, default='PS4')
    editorJuegos = (('Bethesda', 'Bethesda'), ('Nintendo', 'Nintendo'), ('SEGA', 'SEGA'), ('Ubisoft', 'Ubisoft'), ('Sony', 'Sony'), ('SquareEnix', 'SquareEnix'), ('Microsoft', 'Microsoft'))
    editorJuego = models.CharField(max_length=20, choices=editorJuegos, default='BETHESDA')
    imagen = models.ImageField(upload_to='', verbose_name='Imagen')






#class Juego(models.Model):
#    tituloJuego = models.CharField(max_length=30)
#    idGenero = models.CharField(max_length=11)
#    idiomaJuego = models.CharField(max_length=20)
#    numeroJugador = models.CharField(max_length=20)
#    fechaLanzamiento = models.DateTimeField()
    #imagen = models.ImageField(upload_to='media/soporte/pictures')
    
    
#class JuegoPlataforma(models.Model):
#    idJuego = models.ForeignKey(Juego, on_delete=models.CASCADE)
#    companiasJuegos = (('Nintendo', 'Nintendo'), ('Sony', 'Sony'), ('Microsoft', 'Microsoft'))
#    companiaJuego = models.CharField(max_length=20, choices=companiasJuegos, default='MICROSOFT')
#    plataformaJuegos = (('Ps4', 'Ps4'), ('Xbox One', 'Xbox One'), ('Nintendo Switch', 'Nintendo Switch'), ('Pc', 'Pc'))
#    plataformaJuego = models.CharField(max_length=20, choices=plataformaJuegos, default='PS4')
#    editorJuegos = (('Bethesda', 'Bethesda'), ('SEGA', 'SEGA'), ('Ubisoft', 'Ubisoft'), ('Sony', 'Sony'), ('SquareEnix', 'SquareEnix'))
#    editorJuego = models.CharField(max_length=20, choices=editorJuegos, default='BETHESDA')


#class JuegoGenero(models.Model):
#    idGenero = models.ForeignKey(Juego, on_delete=models.CASCADE)
#    generoJuego = models.CharField(max_length=30)



#class Juego(models.Model):
#    IdJuego = models.CharField(max_length=11, primary_key=True)
#    TituloJuego = models.CharField(max_length=30)
#    GeneroJuego = models.CharField(max_length=30)
#    IdiomaJuego = models.CharField(max_length=20)
#    NumeroJugador = models.CharField(max_length=20)
#    FechaLanzamiento = models.DateTimeField()
#    CompaniasJuegos = (('Nintendo', 'Nintendo'), ('Sony', 'Sony'), ('Microsoft', 'Microsoft'))
#    CompaniaJuego = models.CharField(max_length=20, choices=CompaniasJuegos, default='MICROSOFT')
#    PlataformaJuegos = (('Ps4', 'Ps4'), ('Xbox One', 'Xbox One'), ('Nintendo Switch', 'Nintendo Switch'), ('Pc', 'Pc'))
#    PlataformaJuego = models.CharField(max_length=20, choices=PlataformaJuegos, default='PS4')
#    EditorJuegos = (('Bethesda', 'Bethesda'), ('SEGA', 'SEGA'), ('Ubisoft', 'Ubisoft'), ('Sony', 'Sony'), ('SquareEnix', 'SquareEnix'))
#    EditorJuego = models.CharField(max_length=20, choices=EditorJuegos, default='BETHESDA')



# Create your models here.
#class Juego(models.Model):
#    TituloJuego = models.CharField(max_length=30)
#    GeneroJuego = models.CharField(max_length=30)
#    FechaLanzamiento = models.DateTimeField()
#    CompaniasJuegos = (('Nintendo', 'Nintendo'), ('Sony', 'Sony'), ('Microsoft', 'Microsoft'))
#    CompaniaJuego = models.CharField(max_length=20, choices=CompaniasJuegos, default='MICROSOFT')
    
#    Imagen = models.FileField(upload_to='imagenes/', blank=True, null=True)
    
#    def __str__(self):
#        return self.TituloJuego





#   def __str__(self):
#        return '{}'. format(self.TituloJuego)
      