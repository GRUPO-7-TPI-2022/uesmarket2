from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='ID_CATEGORIA', primary_key=True)  # Field name made lowercase.
    nombre_categoria = models.TextField(db_column='NOMBRE_CATEGORIA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categoria'


class Comentario(models.Model):
    id_comme = models.AutoField(db_column='ID_COMME', primary_key=True)  # Field name made lowercase.
    id_publicacion = models.ForeignKey('Publicacion', models.DO_NOTHING, db_column='ID_PUBLICACION', blank=True, null=True)  # Field name made lowercase.
    carnet = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='CARNET', blank=True, null=True)  # Field name made lowercase.
    commet = models.TextField(db_column='COMMET', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comentario'


class Falcultad(models.Model):
    id_facultad = models.AutoField(db_column='ID_FACULTAD', primary_key=True)  # Field name made lowercase.
    nombre_facultad = models.TextField(db_column='NOMBRE_FACULTAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'falcultad'


class Favoritos(models.Model):
    id_favorito = models.AutoField(db_column='ID_FAVORITO', primary_key=True)  # Field name made lowercase.
    carnet = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='CARNET', blank=True, null=True)  # Field name made lowercase.
    id_publicacion = models.ForeignKey('Publicacion', models.DO_NOTHING, db_column='ID_PUBLICACION', blank=True, null=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='TITULO', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'favoritos'


class Producto(models.Model):
    id_producto = models.AutoField(db_column='ID_PRODUCTO', primary_key=True)  # Field name made lowercase.
    id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='ID_CATEGORIA', blank=True, null=True)  # Field name made lowercase.
    nombres = models.TextField(db_column='NOMBRES', blank=True, null=True)  # Field name made lowercase.
    cantidad_disponible = models.IntegerField(db_column='CANTIDAD_DISPONIBLE', blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='PRECIO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.     
    estado_producto = models.TextField(db_column='ESTADO_PRODUCTO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto'


class Publicacion(models.Model):
    id_publicacion = models.AutoField(db_column='ID_PUBLICACION', primary_key=True)  # Field name made lowercase.
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='ID_PRODUCTO', blank=True, null=True)  # Field name made lowercase. 
    carnet = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='CARNET', blank=True, null=True)  # Field name made lowercase.
    fecha_publicacion = models.DateField(db_column='FECHA_PUBLICACION', blank=True, null=True)  # Field name made lowercase.
    estado_publicacion = models.TextField(db_column='ESTADO_PUBLICACION', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)  # Field name made lowercase.
    path_foto = models.ImageField(null=True,blank=True,upload_to="images/")   # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publicacion'


class Usuario(models.Model):
    carnet = models.CharField(db_column='CARNET', primary_key=True, max_length=7)  # Field name made lowercase.
    id_facultad = models.ForeignKey(Falcultad, models.DO_NOTHING, db_column='ID_FACULTAD', blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='NOMBRES', blank=True, null=True,max_length=50)  # Field name made lowercase.
    correo_institucional = models.EmailField(db_column='CORREO_INSTITUCIONAL', blank=True, null=True)  # Field name made lowercase.
    apellidos = models.CharField(db_column='APELLIDOS', blank=True, null=True,max_length=50)  # Field name made lowercase.
    estado = models.TextField(db_column='ESTADO', blank=True, null=True)  # Field name made lowercase.
    contrasena = models.TextField(db_column='CONTRASENA', blank=True, null=True)  # Field name made lowercase.
    numero_contacto = models.CharField(db_column='NUMERO_CONTACTO', blank=True, null=True,max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'