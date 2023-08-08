from category.models import category

def categoryProduct(request):
    categories = category.objects.all()
    categg = list(categories)
    # You can add any data you want to send to the base.html here
    data = {
        'categ':categg
    }
    return data