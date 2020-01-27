from django.views.generic import ListView ,DetailView
from django.http import Http404    
from .models import Product

from django.shortcuts import render ,get_object_or_404


class ProductListView(ListView):
    queryset=Product.objects.all()
    
    # model = Product
    # def get_context_data(self,*args,**kwargs):
    #     context = super(ProductListView,self).get_context_data(*args,**kwargs)
    #     print(context) 
    #     return context
    
    template_name = "products/list.html"

def product_list_view(request):
    queryset=Product.objects.all()
    context={
        'object_list':queryset
    }
    return render(request,"products/list.html",context)


class ProductDetailView(DetailView):
    queryset=Product.objects.all()
    
    # model = Product
    def get_context_data(self,*args,**kwargs):
        context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
        print(context) 
        return context
    
    template_name = "products/detail.html"

def product_detail_view(request,pk=None,*args,**kwargs):
    # queryset=Product.objects.all()
    # instance=Product.objects.get(pk=pk)
    #instance=get_object_or_404(Product,pk=pk)
    # try:
    #     instance=Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     raise Http404('product not exist')

    qs = Product.objects.all()
    if qs.exists() and qs.count()==1:
        instance=qs.first()
    else:
        raise Http404('product not exist')
    context={
        'obj':instance
    }
    return render(request,"products/detail.html",context)    