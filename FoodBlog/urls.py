"""
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.forms import AuthenticationForm


print("URLS . PY TRIGGERES")

urlpatterns = [
    
    path("", include("recipes.urls")),
    path("recipes/", include("recipes.urls")),
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("base/", include("recipes.urls")),
    path("accounts/", include("recipes.urls")),

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#  django.contrib.auth.urls include

#  accounts/login/ [name='login']
#  accounts/logout/ [name='logout']
#  counts/password_change/done/ [name='password_change_done']
#  accounts/password_reset/ [name='password_reset']
#  accounts/password_reset/done/ [name='password_reset_done']
#  accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
#  accounts/reset/done/ [name='password_reset_complete']