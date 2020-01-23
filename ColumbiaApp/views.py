from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from ColumbiaApp.models import Restaurant

# Create your views here.

def home(request):
    data = dict()
    import datetime
    data['date'] = datetime.date.today()
   
    template_name = 'home.html'
    extended_template = 'base_nologin.html'

    if request.user.is_authenticated:
        extended_template = 'base_login.html'
    
    data['extended_template'] = extended_template
    user = request.user
    if user.is_superuser:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.save()
            data['message'] = "Successfully processed. Press register again to add another user. "
            return render(request,"admin_ops.html", context=data)
        else:
            form = UserCreationForm()
            data['form'] = form
            return render(request,"admin_ops.html",context=data)
    return render(request, template_name, context=data)

def register(request):
    #TODO
    pass

def restaurant_map(request):
    #TODO
    pass

def fav_list(request):
    fav_rest_list = Restaurant.objects.filter(user=request.user)
    data_list = []
    context = {}
    for ele in fav_rest_list:
        temp_dict = {}
        temp_dict['name'] = ele.name
        temp_dict['cusine'] = ele.cusine
        temp_dict['url'] = ele.url
        data_list.append(temp_dict)
    context['fav_restaurants'] = data_list
    return render(request,'fav_list.html',context)

def add_to_fav(request):
    #TODO
    #Upon adding restaurant from map.
    # Update database here
    pass

def remove_from_fav(request):
    #Restaurant.objects.filter(user=request.user,name=).delete()
    #return fav_list(request)
    print(request.name)
    print('here')
    pass
