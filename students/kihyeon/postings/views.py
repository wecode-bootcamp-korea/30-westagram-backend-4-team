import json, jwt

from django.views import View
from django.http  import JsonResponse

from .models          import Post
from secret           import ALGORITHM
from config.settings  import SECRET_KEY

class PostingView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            post_title   = data["post_title"]
            post_content = data["post_content"]
            payload = jwt.decode(data["token"], SECRET_KEY, ALGORITHM)

            Post.objects.create(
                post_title   = post_title,
                post_content = post_content,
                image_url    = data["image_url"],
                user_id      = payload['user_id'],
            )

            return JsonResponse({"MESSAGE": "Post created!"}, status=201)
        
        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)

    def get(self, request):
        posts = Post.objects.all()
        results = []
        
        for post in posts:
            results.append(
                {
                "id" : post.id,
                "post_title" : post.post_title,
                "post_content" : post.post_content,
                "image" : post.image_url,
                "user_id" : post.user_id,
                "user" : {
                    "id" : post.user.id,
                    "first_name" : post.user.first_name,
                    "last_name" : post.user.last_name,
                    "email" : post.user.email,
                    "phone_number" : post.user.phone_number,   
                    }
                }
            )
        return JsonResponse({"postings" : results}, status = 200)
