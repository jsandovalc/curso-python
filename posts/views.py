from django.utils import timezone as tz
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, VehiculoForm
from django.contrib.auth.models import User


def post_list(request):
    return render(request, "posts/post_list.html",
                  {"posts": Post.objects.order_by("-created_date")})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.first()
            post.published_date = tz.now()
            post.save()

            return redirect("post_list")
    else:
        form = PostForm()

    return render(request, "posts/post_edit.html", {"form": form})


def vehiculo_new(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("post_list")
    else:
        form = VehiculoForm()

    return render(request, "posts/vehiculo_new.html", {"form": form})
