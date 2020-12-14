from django.urls import path

from app.views import (load_data)

urlpatterns = [
    path('add-movies/', add_movie_view, name='add_movie'),
    path('get-movies/', get_movies_view, name='get_movie'),
    path('give-feedback/', give_feedback_view, name='give_feedback'),
    path('view-feedback/', view_feedback_view, name='view_feedback'),
]