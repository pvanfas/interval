from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from products.models import Category
from products.models import OfferProduct
from products.models import Product
from products.models import ProductEnquiry


class CategoryList(ListView):
    queryset = Category.objects.all()


class CategoryDetail(DetailView):
    model = Category
    template_name = "common/object_detail.html"


class CategoryForm(CreateView):
    model = Category
    fields = "__all__"
    template_name = "common/object_form.html"

    def get_success_url(self):
        return reverse_lazy("products:category_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Category"
        return context


class CategoryUpdate(UpdateView):
    model = Category
    fields = "__all__"
    template_name = "common/object_form.html"
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Category - "
        return context


class CategoryDelete(DeleteView):
    model = Category
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("products:category_list")


class OfferProductList(ListView):
    queryset = OfferProduct.objects.all()


class OfferProductDetail(DetailView):
    model = OfferProduct
    template_name = "common/object_detail.html"


class OfferProductForm(CreateView):
    model = OfferProduct
    fields = "__all__"
    template_name = "common/object_form.html"

    def get_success_url(self):
        return reverse_lazy("products:offer_product_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New OfferProduct"
        return context


class OfferProductUpdate(UpdateView):
    model = OfferProduct
    fields = "__all__"
    template_name = "common/object_form.html"
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit OfferProduct -"
        return context


class OfferProductDelete(DeleteView):
    model = OfferProduct
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("products:offer_product_list")


class ProductList(ListView):
    queryset = Product.objects.all()


class ProductDetail(DetailView):
    model = Product
    template_name = "common/object_detail.html"


class ProductForm(CreateView):
    model = Product
    fields = "__all__"
    template_name = "common/object_form.html"

    def get_success_url(self):
        return reverse_lazy("products:product_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Product"
        return context


class ProductUpdate(UpdateView):
    model = Product
    fields = "__all__"
    template_name = "common/object_form.html"
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Product - "
        return context


class ProductDelete(DeleteView):
    model = Product
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("products:product_list")


class ProductEnquiryList(ListView):
    queryset = ProductEnquiry.objects.all()


class ProductEnquiryDetail(DetailView):
    model = ProductEnquiry
    template_name = "common/object_detail.html"


class ProductEnquiryForm(CreateView):
    model = ProductEnquiry
    fields = "__all__"
    template_name = "common/object_form.html"

    def get_success_url(self):
        return reverse_lazy("products:product_enquiry_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New ProductEnquiry"
        return context


class ProductEnquiryUpdate(UpdateView):
    model = ProductEnquiry
    fields = "__all__"
    template_name = "common/object_form.html"
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit ProductEnquiry - "
        return context


class ProductEnquiryDelete(DeleteView):
    model = ProductEnquiry
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("products:product_enquiry_list")
