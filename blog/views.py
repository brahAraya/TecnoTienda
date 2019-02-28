from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
def index(request):
    producto = Producto.objects.all()
    return render(request, 'blog/index.html', {'productos':producto})


#class SignUpView(CreateView):
#    model = Perfil
#    form_class = SignUpForm
#
#    def form_valid(self, form):
#        '''
#        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
#        '''
#        form.save()
#        usuario = form.cleaned_data.get('username')
#        password = form.cleaned_data.get('password1')
#        usuario = authenticate(username=usuario, password=password)
#        login(self.request, usuario)
#        return redirect('/')

#class SignInView(LoginView):
#    template_name = 'blog/iniciar_sesion.html'


#class SignOutView(LogoutView):
#    template_name = 'blog/index.html'
#    pass

