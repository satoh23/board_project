from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from .models import Posts, CustomUser, Thread
from .forms import PostsForm, UesrCreateForm, ThreadCreateForm, ResponseForm
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
def rule(request):
    return render(request, 'login_app/rule.html', {})

def after_create_user(request):
    return render(request, 'login_app/after_create_user.html', {})

#スレッド作成view。ログイン中のみ可
@login_required
def create_thread(request):
    names = CustomUser.objects.filter(username=request.user).values_list('nickname')
    for name in names:
        author_name = name[0]

    params = {'message': '', 'form': None, 'author_name': author_name}
    if request.method == 'POST':
        form = ThreadCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_list')
        else:
            params['message'] = '再入力してください'
            params['form'] = form
    else:
        params['form'] = ThreadCreateForm(initial={'author': author_name})

    return render(request, 'login_app/create_thread.html', params)

#スレッドの表示、書き込みのview。pk=Threadの主キー
def board(request, pk):
    thread = Thread.objects.filter(id = pk)
    writing_inf = Posts.objects.filter(thread_id__id = pk, response_id__isnull=True)
    params = {'message': '', 'form': None, 'thread': thread, 'writing_inf': writing_inf,}
    url = request.build_absolute_uri()
    author_names = thread.values_list('author')

    for author_name in author_names:
        author_name = author_name[0]

    if request.user.is_authenticated:
        names = CustomUser.objects.filter(username=request.user).values_list('nickname')
        for name in names:
            name = name[0]
    else:
        name = '名無しさん'

    if 'writing_btn' in request.POST:
        form = PostsForm(request.POST)
        if form.is_valid():
            posts = form.save(commit = False)
            posts.save()
            return redirect(url)
        else:
            params['message'] = '再入力してください'
            params['form'] = form
    else:
        params['form'] = PostsForm(initial={'thread_id': pk, 'nickname': name})

    params.update(author_name=author_name, name=name)
    return render(request, 'login_app/board.html', params)

#書き込みへの返信。iframeを使ってスレッドに表示する。res_id=Postsの主キー。
@xframe_options_exempt
def response(request,res_id):
    res_inf = Posts.objects.filter(response_id=res_id)
    params = {'message': '', 'res_form': None, 'res_inf': res_inf,}
    url = request.build_absolute_uri()

    if request.user.is_authenticated:
        names = CustomUser.objects.filter(username=request.user).values_list('nickname')
        for name in names:
            name = name[0]
    else:
        name = '名無しさん'

    if 'response_btn' in request.POST:
        res_form = ResponseForm(request.POST)
        if res_form.is_valid():
            posts = res_form.save(commit = False)
            posts.save()
            return redirect(url)
        else:
            params['message'] = '再入力してください'
            params['res_form'] = res_form
    else:
        params['res_form'] = ResponseForm(initial={'response_id': res_id, 'nickname': name})

    params['name']=name
    return render(request, 'login_app/response.html', params)

#掲示板の一覧表示。
def board_list(request):
    params = {'message': '', 'form': None}
    all_item = Thread.objects.all
    params['all_item'] = all_item

    return render(request, 'login_app/board_list.html', params)

#ユーザー作成。
class Create_user(CreateView):
    def post(self, request, *args, **kwargs):
        form = UesrCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            nickname = form.cleaned_data.get('nickname')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, nickname=nickname, password=password)
            return redirect('after_create_user')
        return render(request, 'login_app/create_user.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = UesrCreateForm(request.POST)
        return render(request, 'login_app/create_user.html', {'form': form,})

Create_user = Create_user.as_view()