from rest_framework import serializers
from postcomment.models import Post,Comment,UserPost

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = ('user_name','full_name','user_email','website','company')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','subject','email','body')

class PostSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many = True, read_only=True)
    userpost = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id','title','content','userpost','comments')
