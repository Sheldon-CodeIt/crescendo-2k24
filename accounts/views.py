from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib import auth
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate


# class CustomLoginView(LoginView):
#     template_name = 'accounts/login.html'
#     fields = '__all__'
#     redirect_authenticated_user = True

#     def get_success_url(self):
#         if 'next' in self.request.POST:
#             # If 'next' parameter exists in POST data, redirect to it
#             return self.request.POST.get('next')
#         else:
#             # If 'next' parameter doesn't exist, redirect to the product details page
#             # You need to modify this logic based on how your URLs are structured
#             # For demonstration purposes, I'm assuming there's a 'product' URL pattern
#             return reverse_lazy('product', kwargs={'pk': self.request.user.id})

    

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'foodsafety/login.html')

    
def registerView(request):
    return render(request, 'foodsafety/register.html')
    


class RegisterPage(FormView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)
    


class CustomLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('login')

    

def logout(request):
    auth.logout(request)
    return redirect('home')
    

# class TaskList(LoginRequiredMixin, ListView):
#     model = Task
#     context_object_name = 'tasks' 

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['tasks'] = context['tasks'].filter(user=self.request.user)
#         context['count'] = context['tasks'].filter(complete=False).count()

#         search_input = self.request.GET.get('search-area') or ''
#         if search_input:
#             context['tasks'] = context['tasks'].filter(title__startswith = search_input)
#             # context['tasks'] = context['tasks'].filter(title__icontains = search_input)

#         context['search_input'] = search_input   
#         return context
    

# class TaskDetail(LoginRequiredMixin, DetailView):
#     model = Task
#     context_object_name = 'task'
#     template_name = 'base/task.html'


# class TaskCreate(LoginRequiredMixin, CreateView):
#     model = Task
#     fields = ['title', 'description', 'complete']
#     success_url = reverse_lazy('tasks')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(TaskCreate, self).form_valid(form)

    
# class TaskUpdate(LoginRequiredMixin, UpdateView):
#     model = Task
#     fields = ['title', 'description', 'complete']
#     success_url = reverse_lazy('tasks')

# class TaskDelete(LoginRequiredMixin, DeleteView):
#     model = Task
#     context_object_name = 'task' 
#     success_url = reverse_lazy('tasks')