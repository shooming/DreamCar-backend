from django.urls    import path

from .views         import UserView

urlpatterns = [
    path('/testdrive', UserView.as_view()),
]
