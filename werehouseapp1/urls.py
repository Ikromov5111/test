from django.urls import path
from .views import *
urlpatterns = [
    
    path("werehouse-list/", WerehouseListApiView.as_view()),
    path("product-list/", ProductListAPiView.as_view()),
    
    path("werehouse-create/", WerecouseCreateApiView.as_view()),
    path("product-create/", ProductCreateApiView.as_view()),
    
    path("werehouse-update/<int:pk>/", WerehouseUpdateAPIView.as_view()),
    path("product-update/<int:pk>/", ProductUpdateAPIView.as_view()),
    # path("product-list-create/", ProductListCreate.as_view()),
    
    path("werehouse-delete/<int:pk>/",WerehouseDeleteAPIView.as_view()),
    path("product_delete/<int:pk>/", ProductDeleteAPIView.as_view()),
    
    path("werehouse-super/<int:pk>", WerehouseSuperApiview.as_view()),
    
    
]

