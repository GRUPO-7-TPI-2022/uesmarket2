from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .forms import *

from datetime import datetime

@login_required
def home(request):
    facultadFIA = Falcultad.objects.get(id_facultad = 1)
    usuario = Usuario.objects.filter(id_facultad = facultadFIA)
    publicaciones = []


    for u in usuario:
        for i in Publicacion.objects.filter(carnet = u):
            publicaciones.append({
                'id_publicacion':i.id_publicacion,
                'id_producto':i.id_producto,
                'carnet':i.carnet,
                'fecha_publicacion':i.fecha_publicacion,
                'estado_publicacion':i.estado_publicacion,
                'descripcion':i.descripcion,
                'path_foto':i.path_foto
            })


        
    # publicaciones = [] 

    # for i in Publicacion.objects.filter(carnet = request.user.username):
    #     publicaciones.append({
    #             'id_publicacion':i.id_publicacion,
    #             'id_producto':i.id_producto,
    #             'carnet':i.carnet,
    #             'fecha_publicacion':i.fecha_publicacion,
    #             'estado_publicacion':i.estado_publicacion,
    #             'descripcion':i.descripcion,
    #             'path_foto':i.path_foto
    #             })
    
    return render(request,"index.html",{'publicaciones':publicaciones})

def homeFacultad(request, id):
    facultadFIA = Falcultad.objects.get(id_facultad = int(id))
    usuario = Usuario.objects.filter(id_facultad = facultadFIA)
    publicaciones = []

    for u in usuario:
        for i in Publicacion.objects.filter(carnet = u):
            publicaciones.append({
                'id_publicacion':i.id_publicacion,
                'id_producto':i.id_producto,
                'carnet':i.carnet,
                'fecha_publicacion':i.fecha_publicacion,
                'estado_publicacion':i.estado_publicacion,
                'descripcion':i.descripcion,
                'path_foto':i.path_foto
            })
        
    # publicaciones = [] 

    # for i in Publicacion.objects.filter(carnet = request.user.username):
    #     publicaciones.append({
    #             'id_publicacion':i.id_publicacion,
    #             'id_producto':i.id_producto,
    #             'carnet':i.carnet,
    #             'fecha_publicacion':i.fecha_publicacion,
    #             'estado_publicacion':i.estado_publicacion,
    #             'descripcion':i.descripcion,
    #             'path_foto':i.path_foto
    #             })
    
    return render(request,"index.html",{'publicaciones':publicaciones})




#Gestion completa de las publicaciones
def publicacion(request, id):
    try:
        publicacion = Publicacion.objects.get(id_publicacion=id)
        verificar = 0 #Soporte para validar si es favorito
        usuario = Usuario.objects.get(carnet=request.user.username)
        comentarios = []
        for i in Comentario.objects.filter(id_publicacion = publicacion):
            comentarios.append({
                'id_comme':i.id_comme,
                'id_publicacion':i.id_publicacion,
                'carnet':i.carnet,
                'commet':i.commet
                })
        
        if Favoritos.objects.get(id_publicacion = publicacion, carnet=usuario):
            verificar = 1
    except Exception as e:
        messages.error(request,'No fue posible encontrar publicación')
        
    return render(request,"publicacion.html",{"publicacion":publicacion,"favorito":verificar, "comentarios":comentarios})

def crearPublicacion(request):
    #Atributos para la publicacion
    fecha_publicacion = datetime.today().strftime('%Y-%m-%d')
    descripcion = request.POST['txtDescripcion']
    path = request.FILES['imgUpload']
    username = request.POST['txtUsername']
    #estado_publicacion = request.POST['txtEstadoPublicacion']

    #Atributos para producto
    categoria = request.POST['idCategoria']
    nombre = request.POST['txtNombre']
    cantidad_disponible = request.POST['NumCantidadDisponible']
    precio_disponible = request.POST['NumPrecioDisponible']
    estado_producto = request.POST['txtEstadoProducto']
    
    producto = Producto.objects.create(
        #id_producto=,
        id_categoria =Categoria.objects.get(id_categoria=categoria),
        nombres = nombre,
        cantidad_disponible = int(cantidad_disponible),
        precio = float(precio_disponible),
        estado_producto = estado_producto
    )

    publicacion = Publicacion.objects.create(
        #id_foto=3,id_publicacion=Publicacion.objects.get(id_publicacion = 1),ruta="BLALBALBLABA",path=path)
        #id_publicacion
        id_producto = Producto.objects.get(id_producto = producto.id_producto),
        carnet = Usuario.objects.get(carnet = username),
        fecha_publicacion= fecha_publicacion,
        estado_publicacion="ACTIVO",
        descripcion=descripcion,
        path_foto=path
    )
    return redirect('/gestionarPublicacion/')

def gestionarPublicacion(request):
    categorias = Categoria.objects.all()
    publicaciones = []

    for i in Publicacion.objects.filter(carnet = request.user.username):
        publicaciones.append({
                'id_publicacion':i.id_publicacion,
                'id_producto':i.id_producto,
                'carnet':i.carnet,
                'fecha_publicacion':i.fecha_publicacion,
                'estado_publicacion':i.estado_publicacion,
                'descripcion':i.descripcion,
                'path_foto':i.path_foto
                })

    return render(request, 'crear_publicacion.html',{'categorias':categorias,'publicaciones':publicaciones})

def eliminarPublicacion(request, id):
    publicidad = Publicacion.objects.get(id_publicacion = id)
    for i in Favoritos.objects.filter(id_publicacion = publicidad):
        i.delete()
    for i in Comentario.objects.filter(id_publicacion = publicidad):
        i.delete()
    publicidad.delete()
    return redirect('/gestionarPublicacion/')

def edicionPublicacion(request,id):
    categorias = Categoria.objects.all()
    publicacion = Publicacion.objects.get(id_publicacion =id)
    return render(request, 'editar_publicacion.html',{'publicacion':publicacion,'categorias':categorias})

def editarPublicacion(request):
    #Atributos para la publicacion
    id_publicacion = request.POST['numPublicacion']
    fecha_publicacion = datetime.today().strftime('%Y-%m-%d')
    descripcion = request.POST['txtDescripcion']
    path = request.FILES['imgUpload']
    username = request.POST['txtUsername']
    #estado_publicacion = request.POST['txtEstadoPublicacion']

    #Atributos para producto
    categoria = request.POST['idCategoria']
    nombre = request.POST['txtNombre']
    cantidad_disponible = request.POST['NumCantidadDisponible']
    precio_disponible = request.POST['NumPrecioDisponible']
    estado_producto = request.POST['txtEstadoProducto']
    
    publicacion = Publicacion.objects.get(id_publicacion = id_publicacion)
    producto = Producto.objects.get(id_producto = publicacion.id_producto.id_producto)

    producto.id_categoria = Categoria.objects.get(id_categoria=categoria)
    producto.nombres = nombre
    producto.cantidad_disponible = int(cantidad_disponible)
    producto.precio = float(precio_disponible)
    producto.estado_producto = estado_producto
    producto.save()

    publicacion.fecha_publicacion = fecha_publicacion
    publicacion.descripcion = descripcion
    publicacion.path_foto = path
    publicacion.save()

    return redirect('/gestionarPublicacion/')

def favoritos(request):
    
    listaDeseos = []
    
    for i in Favoritos.objects.filter(carnet = request.user.username):
        listaDeseos.append({
                'publicacion':i.id_publicacion
                })
    numPublicaciones = len(listaDeseos)

    return render(request,"lista_de_deseos.html",{'publicacion':listaDeseos,'numPublicaciones':numPublicaciones})

def listas(request):
    return render(request,"lista_favoritos.html")

# Es parte de la programacion del liston que se muestra en cada publicacion
# asi puede seleccionar como favorito o eliminar el favorito
def publicacionFavorita(request):
    #El carnet del usuario lo tomamos a través del request
    
    #print(request.POST)
    usuario = Usuario.objects.get(carnet = request.user.username)
    publicacion = Publicacion.objects.get(id_publicacion = request.POST['id_publicacion'])
    
    Favoritos.objects.create(
        carnet = usuario,
        id_publicacion = publicacion
    )

    return redirect('/')

def eliminarFavorita(request):
    usuario = Usuario.objects.get(carnet = request.user.username)
    publicacion = Publicacion.objects.get(id_publicacion = request.POST['id_publicacion'])
    objetoDeleteFavorito(usuario,publicacion)

    return redirect('/')

def objetoDeleteFavorito(usuario,publicacion):
    favorito = Favoritos.objects.get(
        carnet = usuario,
        id_publicacion = publicacion
    )

    favorito.delete()
# Aqui finaliza lo mencionado con anterioridad

#Se creara una función para elimiar favoritos a partir de una lista de favoritos
def deleteFavoritoList(request, id):
    usuario = Usuario.objects.get(carnet = request.user.username)
    publicacion = Publicacion.objects.get(id_publicacion =id)
    objetoDeleteFavorito(usuario,publicacion)
    return redirect('favoritos')

#function para registrar usuario

def registrarCuenta(request):

    form = RegistrarCuenta()
    form2 = RegistrarUsuario()
    facultad = Falcultad.objects.all()
    
    if request.method == 'POST':
        form = RegistrarCuenta(request.POST)
        form2 = RegistrarUsuario(request.POST)
        if form.is_valid and form2.is_valid():
            form.save()
            form2.save()
            return redirect('login')

    context = {'form':form,'form2':form2,'facultad':facultad}
    

    return render(request,'registration/createAccount.html',context)

#Funcion para guardar comentarios de la publicacion
def comentarPublicacion(request):
    usuario = Usuario.objects.get(carnet = request.user.username)
    publicacion = Publicacion.objects.get(id_publicacion = request.POST['id_publicacion_comment'])
    comentario = request.POST['txtComment']
    Comentario.objects.create(
        id_publicacion = publicacion,
        carnet = usuario,
        commet = comentario
    )
    #comentarios = list(Comentario.objects.all().values())
    comentarios = list(Comentario.objects.filter(id_publicacion = publicacion).values())
    '''
    for i in Comentario.objects.filter(id_publicacion = publicacion):
        comentarios.append({
            'id_comme':i.id_comme,
            'id_publicacion':i.id_publicacion,
            'carnet':i.carnet,
            'commet':i.commet
            })
    comentarios = list(comentarios)
    '''

    #Pintaremos de nuevo la caja de comentarios
    return JsonResponse({'comentarios':comentarios})