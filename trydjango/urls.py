"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from pages.views import home_view, contact_view, about_view, social_view, chapter_view, seznam_view, ntice_view, mnozina_view, cyklus_view, slovnik_view, funkce_view, generatory_view, dekoratory_view, vyjimky_view, soubory_view, tridy_view, zaklady_view, sablony_view, pohledy_view, bootstrap_view, prvniprojekt_view, komponenty_view, instalace_view, nasazeni_view, knihovny_view
from products.views import product_detail_view, product_create_view

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('about/', about_view),
    path('social/', social_view),
    path('admin/', admin.site.urls),
    path('product/', product_detail_view),
    path('create/', product_create_view),
    path('prvni/', chapter_view),
    path('seznam/', seznam_view),
    path('ntice/', ntice_view),
    path('mnozina/', mnozina_view),
    path('cyklus/', cyklus_view),
    path('slovnik/', slovnik_view),
    path('funkce/', funkce_view),
    path('generatory/', generatory_view),
    path('dekoratory/', dekoratory_view),
    path('vyjimky/', vyjimky_view),
    path('soubory/', soubory_view),
    path('tridy/', tridy_view),
    path('zaklady/', zaklady_view),
    path('sablony/', sablony_view),
    path('pohledy/', pohledy_view),
    path('bootstrap/', bootstrap_view),
    path('prvniprojekt/', prvniprojekt_view),
    path('komponenty/', komponenty_view),
    path('instalace/', instalace_view),
    path('nasazeni/', nasazeni_view),
    path('knihovny/', knihovny_view)




]




