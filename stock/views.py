from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, FormView, TemplateView


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'form.html'
    form_class = ProductForm
    success_url = '/products/'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'form.html'
    form_class = ProductForm
    success_url = '/products/'


def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('product')


def main(request):
    return render(request, 'main.html', {})


class SupplierListView(ListView):
    model = Supplier
    template_name = 'supplier/supplier_list.html'
    context_object_name = 'suppliers'


class SupplierCreateView(CreateView):
    model = Supplier
    template_name = 'form.html'
    form_class = SupplierForm
    success_url = '/suppliers/'


class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = 'form.html'
    form_class = SupplierForm
    success_url = '/suppliers/'


def delete_supplier(request, pk):
    supplier = Supplier.objects.get(pk=pk)
    supplier.delete()
    return redirect('supplier')


class ManagerListView(ListView):
    model = Manager
    template_name = 'manager/manager_list.html'
    context_object_name = 'managers'


class ManagerCreateView(CreateView):
    model = Manager
    template_name = 'form.html'
    form_class = ManagerForm
    success_url = '/manager/'


class ManagerUpdateView(UpdateView):
    model = Manager
    template_name = 'form.html'
    form_class = ManagerForm
    success_url = '/manager/'


def delete_manager(request, pk):
    manager = Manager.objects.get(pk=pk)
    manager.delete()
    return redirect('manager_list')


class StockListView(ListView):
    model = StockProduct
    template_name = 'stock/stock_list.html'
    context_object_name = 'stocks'


class StockCreateView(CreateView):
    model = StockProduct
    template_name = 'form.html'
    form_class = StockForm
    success_url = '/stock/'


class StockUpdateView(UpdateView):
    model = StockProduct
    template_name = 'form.html'
    form_class = StockForm
    success_url = '/stock/'


def delete_stock(request, pk):
    stock = StockProduct.objects.get(pk=pk)
    stock.delete()
    return redirect('stock')


class CookerListView(ListView):
    model = Cooker
    template_name = 'cooker/cooker_list.html'
    context_object_name = 'cookers'


class CookerCreateView(CreateView):
    model = Cooker
    template_name = 'form.html'
    form_class = CookerForm
    success_url = '/cookers/'


class CookerUpdateView(UpdateView):
    model = Cooker
    template_name = 'form.html'
    form_class = CookerForm
    success_url = '/cookers/'


def delete_cooker(request, pk):
    cooker = Cooker.objects.get(pk=pk)
    cooker.delete()
    return redirect('cooker')


class SuppliesListView(ListView):
    model = Supplies
    template_name = 'supplies/supplies_list.html'
    context_object_name = 'supplies'


class SuppliesCreateView(CreateView):
    model = Supplies
    template_name = 'form.html'
    form_class = SuppliesForm
    success_url = '/supplies/'


def supplies_create_view(request):
    context = {}
    if "added_products" not in request.session.keys():
        request.session["added_products"] = []
    form = SuppliesForm()

    if request.method == "POST" and (form := SuppliesForm(request.POST)).is_valid():
        pass

    context["form"] = form
    context["added_products"] = request.session.get("added_products")
    return render(request, 'add_products_form.html', context)

def supplies_product_create_view(request):
    context = {}



    return render(request, "form.html", context)

class SuppliesUpdateView(UpdateView):
    model = Supplies
    template_name = 'form.html'
    form_class = SuppliesForm
    success_url = '/supplies/'


def delete_supplies(request, pk):
    supplies = Supplies.objects.get(pk=pk)
    supplies.delete()
    return redirect('supplies')


class CookerSelectView(FormView):
    template_name = 'cooker/cooker_select.html'
    form_class = CookerSelectionForm
    success_url = '/cooker/product/'
    cooker = None

    def form_valid(self, form):
        self.cooker = form.cleaned_data['cooker']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cookers'] = Cooker.objects.all()
        context['selected_cooker'] = self.cooker
        return context


class CookerProductView(FormView):
    template_name = 'cooker/cooker_product.html'
    form_class = CookerProductForm
    success_url = '/cooker/'

    def form_valid(self, form):
        stock_model = form.cleaned_data['stock']
        amount = form.cleaned_data['amount']
        initial_amount = stock_model.amount
        stock_model.amount -= amount
        stock_model.save()
        StockHistory.objects.create(stock=stock_model, amount=amount, initial_amount=initial_amount, final_amount=stock_model.amount)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stocks'] = StockProduct.objects.all()
        return context



class CookerProductHistoryView(TemplateView):
    template_name = 'cooker/cooker_product_history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        history = StockHistory.objects.all()
        for i, item in enumerate(history):
            if i == 0:
                item.initial_amount = item.stock.amount
            else:
                item.initial_amount = history[i - 1].final_amount + item.amount
            item.final_amount = item.initial_amount - item.amount
        context['history'] = history
        return context

