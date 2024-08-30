from django.urls import path
from . import views # 같은 폴더 내의 views.py를 import

app_name = 'main'

urlpatterns = [
    # 127.0.0.1:8000/predict_sentiment/bert_input/
    path('bert_input/', views.bert_input, name='bert_input'),
    path('bert_predict/', views.bert_predict, name='bert_predict'),
]
