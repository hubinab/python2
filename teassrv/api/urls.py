from django.urls  import path
from .views import get_brands, create_brand, brand_detail, tea_detail, get_post_Teas, create_tea


urlpatterns = [
    path('brands/', get_brands, name='get_brands'),
    path('brands/', create_brand, name='create_brand'),
    path('brands/<int:pk>', brand_detail, name='brand_detail'),
    path('teas/', get_post_Teas, name='get_post_teas'),
    path('teas/create/', create_tea, name='create_tea'),
    path('teas/<int:pk>', tea_detail, name='tea_detail'),
]