from django.shortcuts import render
from django.http import HttpResponse
from.models import Product,Registation
from django.forms import ModelForm
# Create your views here.
class PostsForm(ModelForm):
    class Meta:
        model = Registation
        fields = ['Full_name','username','email','phone_number','password']
def home(request):
	return render(request, 'home.html')

def P_datails(request,id):
	a=Product.objects.get(id=id)
	print(a)
	return render(request, 'P_details.html',{'a':a})

def product_cart(request):
	products=Product.objects.all()
	return render(request, 'product_cart.html',{'products':products})		

def Registation(request,template_name ='Registation.html'):
	form = PostsForm(request.POST or None)
	if form.is_valid():
		form.save()
		# return redirect('contect')
	return render(request, template_name, {'form': form})	

def popup(request):
    return render(request, 'register.html')	  

# def P_datails(request):
#     products = Product.objects.order_by('-pk')[0]
#     return render(request, 'P_details.html', {'prodlist': products})    

