from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


app_name = "products"

urlpatterns = [
    path("categories/", login_required(views.CategoryList.as_view()), name="category_list"),
    path("new/category/", login_required(views.CategoryForm.as_view()), name="new_category"),
    path("view/category/<str:pk>/", login_required(views.CategoryDetail.as_view()), name="view_category"),
    path("update/category/<str:pk>/", login_required(views.CategoryUpdate.as_view()), name="update_category"),
    path("delete/category/<str:pk>/", login_required(views.CategoryDelete.as_view()), name="delete_category"),
    path("products/", login_required(views.ProductList.as_view()), name="product_list"),
    path("new/product/", login_required(views.ProductForm.as_view()), name="new_product"),
    path("view/product/<str:pk>/", login_required(views.ProductDetail.as_view()), name="view_product"),
    path("update/product/<str:pk>/", login_required(views.ProductUpdate.as_view()), name="update_product"),
    path("delete/product/<str:pk>/", login_required(views.ProductDelete.as_view()), name="delete_product"),
    path("offer_products/", login_required(views.OfferProductList.as_view()), name="offer_product_list"),
    path("new/offer_product/", login_required(views.OfferProductForm.as_view()), name="new_offer_product"),
    path("view/offer_product/<str:pk>/", login_required(views.OfferProductDetail.as_view()), name="view_offer_product"),
    path(
        "update/offer_product/<str:pk>/",
        login_required(views.OfferProductUpdate.as_view()),
        name="update_offer_product",
    ),
    path(
        "delete/offer_product/<str:pk>/",
        login_required(views.OfferProductDelete.as_view()),
        name="delete_offer_product",
    ),
    path("product_enquiries/", login_required(views.ProductEnquiryList.as_view()), name="product_enquiry_list"),
    path("new/product_enquiry/", login_required(views.ProductEnquiryForm.as_view()), name="new_product_enquiry"),
    path(
        "view/product_enquiry/<str:pk>/",
        login_required(views.ProductEnquiryDetail.as_view()),
        name="view_product_enquiry",
    ),
    path(
        "update/product_enquiry/<str:pk>/",
        login_required(views.ProductEnquiryUpdate.as_view()),
        name="update_product_enquiry",
    ),
    path(
        "delete/product_enquiry/<str:pk>/",
        login_required(views.ProductEnquiryDelete.as_view()),
        name="delete_product_enquiry",
    ),
]
