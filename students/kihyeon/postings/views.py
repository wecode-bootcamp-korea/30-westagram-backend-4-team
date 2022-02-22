import json, jwt

from django.views import View
from django.http  import JsonResponse

from users.models     import User
from .models          import Post, Comment, Like
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

class CommentView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            comment = data['comment']
            post_id = data['post_id']
            payload = jwt.decode(data["token"], SECRET_KEY, ALGORITHM)
            user_id = payload['user_id']


            if not User.objects.filter(id = user_id).exists():
                return JsonResponse({'MESSAGE': "User Does Not Exist"}, status=404)

            if not Post.objects.filter(id = post_id).exists(): 
                return JsonResponse({'MESSAGE': "Posting Does Not Exist"}, status=404)
            
            Comment.objects.create(
                comment = comment,
                user_id = payload['user_id'],
                post_id = post_id,
            )

            return JsonResponse({"MESSAGE": "Post created!"}, status=201)
   
        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)
        
    def get(self, request):
        comments = Comment.objects.all()
        results = []

        for comment in comments:
            results.append(
                {
                "comment" : comment.comment,
                "post_id" : comment.post_id,
                "user_id" : comment.user_id,
                "post" : {
                    "post_title" : comment.post.post_title,
                    "post_content" : comment.post.post_content,
                    }   
                }
            )
        return JsonResponse({"postings" : results}, status = 200)
    
class LikeView(View):
    def post(self, request):
        try:        
            data = json.loads(request.body)
            post_id    = data['post_id'] 
            payload = jwt.decode(data["token"], SECRET_KEY, ALGORITHM)
            user_id    = payload['user_id']

            if not User.objects.filter(id = user_id).exists():
                return JsonResponse({'MESSAGE': "User Does Not Exist"}, status=404)    
            
            if not User.objects.filter(id = post_id).exists():
                return JsonResponse({'MESSAGE': "Post Does Not Exist"}, status=404)    
            
            if Like.objects.filter(user = user_id, post=post_id).exists():
                return JsonResponse({'MESSAGE': "Already Liked Post"}, status=404)    
            
            Comment.objects.create(
                user_id = payload['user_id'],
                post_id = post_id,
            )
            return JsonResponse({'messasge':'SUCCESS'}, status=201) 

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)
        