from django.utils import timezone as tz
from django.shortcuts import render, redirect
from .models import Post, Vehiculo
from .forms import PostForm, VehiculoForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


class VehiculoCreate(CreateView):
    model = Vehiculo
    fields = ["placa", "referencia", "nota", "estaeliminado", "marca"]

    success_url = reverse_lazy("info")


class VehiculoDelete(DeleteView):
    model = Vehiculo

    success_url = reverse_lazy("info")


def post_list(request):
    return render(
        request,
        "posts/post_list.html",
        {"posts": Post.objects.order_by("-created_date")},
    )


class PostCreate(CreateView):
    model = Post
    fields = ["title", "text"]

    success_url = reverse_lazy("info")

    def form_valid(self, form):
        form.instance.author = User.objects.first()
        form.instance.published_date = tz.now()

        return super().form_valid(form)


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


class Info(TemplateView):
    template_name = "posts/info.html"
