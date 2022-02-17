#products/views.py

import json

from django.http import JsonResponse
from django.views import View

from users.models import User

class ProductsView(View):
    def post(self, request):
        data     = json.loads(request.body)
        menu     = Menu.objects.create(name=data['menu'])
        category = Category.objects.create(
            name = data['category'],
            menu = menu
        )
        Product.objects.create(
            name     = data['product'],
            category = category
        )
    return JsonResponse({'messasge':'created'}, status=201)