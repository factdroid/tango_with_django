from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

def index(request): 
    #Quering Category table for list of categories
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    # Return a rendered response to send to the client. 
    # We make use of the shortcut function to make our lives easier. 
    # Note that the first parameter is the template we wish to use. 
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/about.html')


def show_category(request, category_name_slug):
    #below is a context_dictionary which can be passed to the template through render()
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        # .get() gets a single instance of the object or returns as exception

        pages = Page.objects.filter(category=category)
        #This will pull all pages associated with that particular category 
        #Or it will return an empty list

        context_dict['pages'] = pages
        context_dict['category'] = category
        # Add the data queried to the context dictionary in order to have
        #them available in the template
    except Category.DoesNotExist:
        #When the category doesn't exist...
        #Don't do anything the template will display "no category" message when we ask it to
        context_dict[pages] = None
        context_dict[category] = None
        #Just so the context dictionary is up to date on what is happening

    #rendering the template and the context
    return render(request, 'rango/category.html', context=context_dict)