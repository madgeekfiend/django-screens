from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from website.forms.comment import CommentForm
from website.forms.screens import ScreenUploadForm
from website.models import Screen, Comment


@login_required
def upload(request):
    if request.method == 'GET':
        form = ScreenUploadForm()
        return render(request, 'upload.html', {'form': form})
    elif request.method == 'POST':
        # Store this stuff into the databse and redirect
        form = ScreenUploadForm(request.POST, request.FILES)
        if form.is_valid():
            #screen = Screen(caption=form.cleaned_data['caption'], image=form.cleaned_data['image'],
             #               team=form.cleaned_data['team'])
            #screen.save()
            form.save()
            return redirect('screens:upload')
        else:
            return HttpResponseNotFound('Oops')


@login_required
def view_screen(request, screen_id):
    screen = get_object_or_404(Screen, pk=screen_id)
    comments = Comment.objects.filter(screen=screen)
    form = CommentForm()
    form.helper.form_action = reverse('screens:comment', kwargs={'screen_id': screen.id})
    return render(request, 'view_screen.html', {'screen': screen, 'comments': comments, 'comment_form': form})


@login_required
def review(request):
    """
    View screen shots
    :param request:
    :return:
    """
    screens_list = Screen.objects.all()
    paginator = Paginator(screens_list, 1)
    page = request.GET.get('page')

    try:
        screens = paginator.page(page)
    except PageNotAnInteger:
        screens = paginator.page(1)
    except EmptyPage:
        screens = paginator.page(paginator.num_pages)
    current_screen = screens.object_list.all()[0]
    form = CommentForm()
    form.helper.form_action = reverse('screens:comment', kwargs={'screen_id': current_screen.id})
    comments = Comment.objects.filter(screen=current_screen)
    user = request.user

    return render(request, 'review.html',
                  {'screens': screens, 'comments': comments, 'comment_form': form, 'current_user': user})


def comment(request, screen_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            screen = Screen.objects.get(id=screen_id)
            new_comment = Comment(screen=screen, comment=form.cleaned_data['comment'], created_by_user=request.user)
            new_comment.save()
            return redirect(request.META['HTTP_REFERER'])
    elif request.method == 'GET':
        raise Http404