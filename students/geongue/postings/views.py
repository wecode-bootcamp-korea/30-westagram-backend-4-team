import json

from django.views       import View
from django.http        import JsonResponse
from .models            import Post, Comment, Like
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
                posted_title   = posted_title,
                posted_content = posted_content,
                posted_image   = posted_image,
                user           = user
            )

            return JsonResponse({"message" : "SUCCESS"}, status = 201)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)
    
    @login_decorator
    def get(self, request):
        posts   = Post.objects.all()
        results = []

        for post in posts:
            fix_created_at = post.created_at.strftime("%Y-%m-%d %H")+"시"
            likes = post.like_set.all()
            like_count = 0
            like_user = []
           
            for like in likes:
                if like.like_status == 1:
                    like_count += 1
                    like_user.append(like.user.email)

            results.append(
                {
                    "poster"     : post.user.first_name,
                    "title"      : post.posted_title,
                    "content"    : post.posted_content,
                    "image_url"  : post.posted_image.url,   
                    "created_at" : fix_created_at,
                    "like_count" : like_count,
                    "like_user"  : like_user
                }
            )

        return JsonResponse({"posts" : results}, status = 200)       


class CommentView(View):

    @login_decorator
    def post(self, request):
        try:
            data    = json.loads(request.body)
            content = data['comment']
            post_id = data['post']
            user    = request.user
            post = Post.objects.get(id=post_id)

            Comment.objects.create(
                content = content,
                post    = post,
                user    = user
            )

            return JsonResponse({"message" : "SUCCESS"}, status = 201)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)

    @login_decorator
    def get(self, request):
        comments = Comment.objects.filter(post = 1)
        results  = []

        for comment in comments:
            fix_created_at = comment.created_at.strftime("%Y-%m-%d %H")+"시"
            results.append(
                {
                    "posted_title" : comment.post.posted_title,
                    "commenter"    : comment.user.email,
                    "content"      : comment.content,
                    "created_at"   : fix_created_at
                }
            )
        
        return JsonResponse({"comments" : results}, status = 200)


class LikeView(View):

    @login_decorator
    def post(self, request):
        try:
            data        = json.loads(request.body)
            like_status = data['like_status']
            post_id     = data['post']
            user        = request.user
            post        = Post.objects.get(id = post_id)

            if like_status == 1 :               
                if not Like.objects.filter(post = post, user = user).exists():
                    Like.objects.create(
                        like_status = like_status,
                        post        = post,
                        user        = user
                    )
                
                else:
                    like             = Like.objects.filter(post = post, user= user)[0]
                    like.like_status = 1
                    like.save()
            
            if like_status == 0 :
                if Like.objects.filter(post = post, user = user).exists():
                    like             = Like.objects.filter(post = post, user= user)[0]
                    like.like_status = 0
                    like.save()
                
                else:
                    return JsonResponse({"message" : "INVALID_LIKE"}, status = 400)

            return JsonResponse({"message" : "SUCCESS"}, status = 201)

        except Post.DoesNotExist:
            return JsonResponse({"message" : "INVALID_POST"}, status = 400)

        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)

    