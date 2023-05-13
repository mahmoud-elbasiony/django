from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect


book_list = [
    {
        'index': 0,
        'id': 1,
        'name': 'Book-1',
        'author': "mahmoud",
        'description': "book 1 description",
        "price":100
    },
    {
        'index': 1,
        'id': 2,
        'name': 'Book-2',
        'author': "ahmed",
        'description': "book 1 description",
        "price":200

    },
    {
        'index': 2,
        'id': 3,
        'name': 'Book-3',
        'author': "mohamed",
        'description': "book 1 description",
        "price":300

    },
]

# Create your views here.
def index(request):
    # print(request.body)
    # print(request.method)
    # print(request.path)
    # print(request.GET)
    # print(request.POST)
    # print(request.COOKIES)
    # print(request.FILES)
    # print(request.META)
    # render (requst, template name, context=None, content_type=None)
    # redirect (to, *args, **kwargs)
    # redirect('/profile' , {'nick_name': 'iti'})
    #localhost:8000/profile 
    # res = HttpResponse("hello world")
    # res.write("<p> Hello OS </>")
    # res['content-type'] = 'text/plain'
    # return res
    # # return JsonResponse({'Track': 'OS'})
    # return HttpResponseRedirect('/')
    my_context = {'book_list': book_list}
    return render(request, 'index.html',context=my_context)

def show(request,**kwargs):
    book=_get_book(kwargs.get('id'))
    print(book)
    my_context = {'book': book}
    return render(request, 'show.html',context=my_context)

def delete(request,**kwargs):
    book=_get_book(kwargs.get('id'))
    if book:
        book_list.remove( book)
    return redirect("books:books-index")

def update(request,**kwargs):
    book=_get_book(kwargs.get('id'))
    if book:
        # book_list.remove( book)
        book['description']=f"price updated"
    return redirect("books:books-index")

def _get_book(id):
    for book in book_list:
        if book['id']==id:
            return book
    return None