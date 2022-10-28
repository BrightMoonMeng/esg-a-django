from pdb import post_mortem
from django.shortcuts import render, redirect
from blog.models import Post, Restaurant
from django.views.generic import CreateView
from blog.forms import PostForm, ResForm

def index(request):
    # 전체 포스팅을 가져올 준비. 아직 가져오지는 않음.
    post_qs = Post.objects.all().order_by("-id")
    return render(request, "blog/index.html", {
        "post_list":post_qs,
    })
    
def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "blog/single_post_page.html",{
        "post":post,
    })


def restaurant_page(request, pk):
    post_res2 = Restaurant.objects.get(pk=pk)
    return render(request, "blog/restaurant_page.html",{
        "post_page":post_res2,
    })


def restaurant(request):
    post_res = Restaurant.objects.all().order_by("-id")
    return render(request, "blog/restaurant.html",{
        "post_rs":post_res,
    }
                  )
# post_new = CreateView.as_view(
#     form_class = PostForm,
#     model=Post,
#     success_url="/blog/",
#     )
    
    
def post_new(request):
    # print("request.method =", request.method)
    # print("request.Post =", request.Post)
    if request.method =="GET":
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            # 유효성 검사에 통과한 값들이 저장된 dict
            # form.cleaned_data
            post = form.save() # ModelForm에서 지원
            # return redirect("/blog/")
            # return redirect(f"/blog/{post.get_absolute_url}")
            return redirect(post)
        
    return render(request, "blog/post_form.html", {
        "form":form,
    })
    
    
def restaurant_new(request):
    # print("request.method =", request.method)
    # print("request.Post =", request.Post)
    if request.method =="GET":
        form_rs = ResForm()
    else:
        form_rs = ResForm(request.POST)
        if form_rs.is_valid():
            # 유효성 검사에 통과한 값들이 저장된 dict
            # form.cleaned_data
            post_res2 = form_rs.save() # ModelForm에서 지원
            # return redirect("/blog/")
            # return redirect(f"/blog/{post.get_absolute_url}")
            return redirect(post_res2)
        
    return render(request, "blog/restaurant/new.html", {
        "form_res":form_rs,
    })
#     from django.shortcuts import render

# def index(request):
#     """포스팅 목록 페이지 HTML을 반환"""
#     return HttpResponse
    
# def post_detail(request,pk):
#  """특정 pk 포스팅 페이지 HTML을 반환"""