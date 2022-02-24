import json
import datetime

from django.views       import View
from django.http        import JsonResponse
from .models            import Post
from users.utils        import login_decorator


class PostingView(View):
   
    @login_decorator
    def post(self, request):
        try:
            data           = json.loads(request.body)
            posted_title   = data['posted_title']
            posted_content = data['posted_content']
            posted_image   = data['posted_image']
            user           = request.user
            
            Post.objects.create(
                posted_title = posted_title,
                posted_content = posted_content,
                posted_image = posted_image,
                user = user
            )

            return JsonResponse({"message" : "SUCCESS"}, status = 201)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)
    
    @login_decorator
    def get(self):
        posts = Post.objects.all()
        results = []

        for post in posts:
            poster_id = post.user
            results.append(
                {
                    "poster"     : post.user_set.get(id=poster_id).first_name,
                    "title"      : post.posted_title,
                    "content"    : post.posted_content,
                    "image_url"  : post.posted_image,   
                    "created_at" : post.created_at
                }
            )

        return JsonResponse({"postings" : results}, status = 200)       
