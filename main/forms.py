from django import forms


class CreatePost(forms.Form):
    title = forms.CharField(label="post_title", max_length=50)
    text = forms.CharField(label="post_text", max_length=200)
    image = forms.CharField(label="post_image", max_length=500)
    link = forms.CharField(label="post_link", max_length=500)    # link is optional
    category = forms.CharField(label="post_category", max_length=50)
