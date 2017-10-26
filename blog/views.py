from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm, ContactForm
from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def sobre(request):
    return render(request, 'blog/sobre.html')


def contact(request):

    voidContactForm = ContactForm()
    if request.method == "POST":

        name=request.POST.get('nameSurnames', '')
        problem = request.POST.get('problem', '')
        from_email = request.POST.get('email', '')
        message="Contact Name: "+name+"\nEmail: "+from_email+"\nProblem:\n"+problem
        if message and from_email:
            try:
                email = EmailMessage("Auto Message", message, to=['ttasnadi.olivera@gmail.com'])
                email.send()
            except BadHeaderError:
                return HttpResponse('Algo ha sortit malament, prova mes tard')
        else:
            return HttpResponse('Et falta per omplir coses')

    return render(request, 'blog/contacta.html',{'contactForm':voidContactForm})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
