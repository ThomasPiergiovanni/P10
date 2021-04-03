from django.shortcuts import get_object_or_404, render

from .models import Product



# Create your views here.
def index(request):
    return render(request, 'supersub/index.html')

# def account(request):
#     return render(request, 'supersub/account.html')

def aliment(request):
    return render(request, 'supersub/aliment.html')


def registered_aliments(request):
    return render(request, 'supersub/registered_aliments.html')

def results(request):
    return render(request, 'supersub/results.html', context)

def test_results(request):
    
    # product = pRODUCTget_object_or_404(Product, name__contains=request.POST['product'])
    try:
        product = Product.objects.get(name__contains=request.POST['product'])
        products_in_catgeories = Product.objects.filter(category_id=product.category_id).exclude(id__exact=product.id).order_by('nutriscore_grade')[:6]
        context = {
            'name': product.name,
            'image': product.image,
            'products_in_categories': products_in_catgeories
        }
        return render(request, 'supersub/test_results.html', context)
    except:
        context = {
            'error_message': "No such product in DB"
        }
        return render(request, 'supersub/test_results.html', context)
