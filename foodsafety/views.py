from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


products = [
    {
        "id": "1",
        "image": "https://images.openfoodfacts.org/images/products/316/893/000/2987/front_en.134.400.jpg",
        "title": "Lay's Cuites au four nature",
        "brand": "Lay's",
        "score": "4",
        
    },
    {
        "id": "2",
        "image": "https://images.openfoodfacts.org/images/products/316/893/000/2987/front_en.134.400.jpg",
        "title": "Lay's Cuites au four nature",
        "brand": "Lay's",
        "score": "4",
        
    },
    {
        "id": "3",
        "image": "https://images.openfoodfacts.org/images/products/316/893/000/2987/front_en.134.400.jpg",
        "title": "Lay's Cuites au four nature",
        "brand": "Lay's",
        "score": "4",
        
    },
    {
        "id": "4",
        "image": "https://images.openfoodfacts.org/images/products/316/893/000/2987/front_en.134.400.jpg",
        "title": "Lay's Cuites au four nature",
        "brand": "Lay's",
        "score": "4",
        
    },
    {
        "id": "5",
        "image": "https://images.openfoodfacts.org/images/products/316/893/000/2987/front_en.134.400.jpg",
        "title": "Lay's Cuites au four nature",
        "brand": "Lay's",
        "score": "4",
        
    },
    {
        "id": "6",
        "image": "https://images.openfoodfacts.org/images/products/316/893/000/2987/front_en.134.400.jpg",
        "title": "Lay's Cuites au four nature",
        "brand": "Lay's",
        "score": "4",
        
    },
    {
        "id": "7",
        "image": "https://images.openfoodfacts.org/images/products/316/893/000/2987/front_en.134.400.jpg",
        "title": "Lay's Cuites au four nature",
        "brand": "Lay's",
        "score": "4",
        
    },
    {
        "id": "8",
        "image": "https://images.openfoodfacts.org/images/products/316/893/000/2987/front_en.134.400.jpg",
        "title": "Lay's Cuites au four nature",
        "brand": "Lay's",
        "score": "4",
        
    },
    {
        "id": "9",
        "image": "https://images.openfoodfacts.org/images/products/316/893/000/2987/front_en.134.400.jpg",
        "title": "Lay's Cuites au four nature",
        "brand": "Lay's",
        "score": "4",
        
    },
    {
        "id": "10",
        "image": "https://images.openfoodfacts.org/images/products/316/893/000/2987/front_en.134.400.jpg",
        "title": "Lay's Cuites au four nature",
        "brand": "Lay's",
        "score": "4",
        
    },
    

    
]

def home(request):
    return render(request, 'foodsafety/main.html')

def about(request):
    return render(request, 'foodsafety/about.html')

def report(request):
    return render(request, 'foodsafety/uploaddoc.html')

def dash(request):
    return render(request, 'foodsafety/dash.html')


# @login_required(login_url='login')
def productDetails(request, product):
    template_name = ''
    if product == 'lays':
        template_name = 'foodsafety/lays.html'
    elif product == 'pepsi':
        template_name = 'foodsafety/pepsi.html'
    elif product == 'sprite':
        template_name = 'foodsafety/sprite.html'
    elif product == 'maggie':
        template_name = 'foodsafety/maggie.html'
    else:
        # Handle invalid product cases, such as showing a 404 page
        return render(request, '404.html', status=404)

    return render(request, template_name)



def productsList(request):
    context = {
        "products": products
    }
    return render(request, 'foodsafety/container.html', context)



# def productDetails(request, pk):
#     # Dummy data for the product details
#     product_details = {
#         "id": "1",
#         "name": "Lay's Cuites au four nature - 130 g",
#         "description": "This product page is not complete. You can help to complete it by editing it and adding more data from the photos we have, or by taking more photos using the app for Android or iPhone/iPad. Thank you!",
#         "barcode": "3168930002987 (EAN / EAN-13)",
#         "common_name": "Produit à base de pommes de terre cuit au four nature",
#         "quantity": "130 g",
#         "packaging": "Plastic, Bag, fr:Sachet en plastique",
#         "brands": "Lays",
#         "categories": "Plant-based foods and beverages, Plant-based foods, Snacks, Cereals and potatoes, Salty snacks, Appetizers, Chips and fries, Crisps, Crisps made from reconstituted potato",
#         "labels": "No preservatives, No colorings, Nutriscore, Nutriscore Grade B, Nutriscore Grade D",
#         "product_link": "https://www.lays.fr/assortiment-de-produ...",
#         "stores": "Cora, Auchan, Magasins U, carrefour.fr, E.Leclerc",
#         "countries_sold": "Belgium, France, Réunion",
#     }

#     context = {
#         "product": product_details,
#     }
    
#     return render(request, 'foodsafety/product.html', context)



