import json

from rest_framework.views    import APIView
from rest_framework.response import Response
from rest_framework          import status

from django.db.models import Q
from django.views     import View
from django.http      import JsonResponse
from django.http      import Http404

from products.models      import Product, Image, Stock, ProductTag, MainCategory, SubCategory, Tag
from products.serializers import ProductSerializer

PAGE_SIZE = 10
# DRF APIView
class ProductAPIView(APIView):
    def get(self, request):
        category_id     = request.GET.get('categoryId', None)
        sub_category_id = request.GET.get('subcategoryId', None)
        sort            = request.GET.get('sort-method', None)
        page            = int(request.GET.get('page', 1)) 

        limit  = page*PAGE_SIZE
        offset = limit-PAGE_SIZE

        q = Q()
        
        if category_id:
            q &= Q(sub_category__maincategory_id=category_id)
            products = Product.objects.filter(q)[offset:limit]

        if sub_category_id:
            q &= Q(sub_category_id=sub_category_id)
            products = Product.objects.filter(q)[offset:limit]
        
        if category_id and sort:
            q &= Q(sub_category__maincategory_id=category_id)
            products = Product.objects.filter(q).order_by(sort)[offset:limit]

        if sub_category_id and sort:
            q &= Q(sub_category_id=sub_category_id)
            products = Product.objects.filter(q).order_by(sort)[offset:limit]
        
        # total = Product.objects.filter(q)

        products    = Product.objects.filter(q)
        serializers = ProductSerializer(products, many=True)

        return Response(serializers.data)
    
    def post(self, request):
        serializers = ProductSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

## DRF APIDetailView
class ProductAPIDetailView(APIView):
    def get(self, request, product_id):
        product     = Product.objects.get(id=product_id)
        images      = Image.objects.filter(product_id=product.id)
        tags        = ProductTag.objects.filter(product_id=product.id)
        size_stocks = Stock.objects.filter(product_id=product.id)

        product     = Product.objects.get(pk=product_id)
        serializers = ProductSerializer(product)
        return Response(serializers.data)

    def put(self, request, pk):
        product     = Product.objects.get(pk=pk)
        serializers = ProductSerializer(
            product,
            data = request.data
        )

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

########## 기존 상품 리스트 뷰 로직 ############
# PAGE_SIZE = 8

# class ProductDetailView(View):
#     def get(self, request, product_id):
#         try:
#             product     = Product.objects.get(id=product_id)
#             images      = Image.objects.filter(product_id=product.id)
#             tags        = ProductTag.objects.filter(product_id=product.id)
#             size_stocks = Stock.objects.filter(product_id=product.id)

#             data = {
#                 'main_category': product.sub_category.maincategory.name,
#                 'sub_category' : product.sub_category.name,
#                 'product_id'   : product.id,
#                 'product_name' : product.name,
#                 'product_price': int(product.price),
#                 'product_body' : product.body,
#                 'product_image': [image.url for image in images],
#                 'product_tag'  : [{
#                     'new' :tag.tag.new, 
#                     'sale':tag.tag.sale, 
#                     'best':tag.tag.best} for tag in tags],
#                 'product_mat'  : product.material,
#                 'product_size' : [{
#                     'option_id'   :size_stock.size.id,
#                     'option_stock':size_stock.count,
#                     'option_name' :size_stock.size.size
#                     } for size_stock in size_stocks]
#                 }

#             if product.discount < 1:
#                 data['discount_rate'] = product.discount

#             return JsonResponse({"result":data}, status = 200)

#         except KeyError:
#             return JsonResponse({"result":"KEY_ERROR"}, status = 400)

# class ProductListView(View):
#     def get(self, request):
#         try:
#             category_id     = request.GET.get('categoryId', None)
#             sub_category_id = request.GET.get('subcategoryId', None)
#             sort            = request.GET.get('sort-method', None)
#             page            = int(request.GET.get('page', 1)) 
            
#             limit  = page*PAGE_SIZE
#             offset = limit-PAGE_SIZE

#             q = Q()
            
#             if category_id:
#                 q &= Q(sub_category__maincategory_id=category_id)
#                 products = Product.objects.filter(q)[offset:limit]

#             if sub_category_id:
#                 q &= Q(sub_category_id=sub_category_id)
#                 products = Product.objects.filter(q)[offset:limit]
            
#             if category_id and sort:
#                 q &= Q(sub_category__maincategory_id=category_id)
#                 products = Product.objects.filter(q).order_by(sort)[offset:limit]

#             if sub_category_id and sort:
#                 q &= Q(sub_category_id=sub_category_id)
#                 products = Product.objects.filter(q).order_by(sort)[offset:limit]
            
#             total = Product.objects.filter(q)

#             if not products:
#                 return JsonResponse({"MESSAGE": "해당 상품이 존재하지 않습니다."}, status=404)

#             results = []

#             for product in products:
#                 tags       = ProductTag.objects.filter(product_id=product.id)
#                 main_image = product.image_set.all()
#                 results.append(
#                     {
#                         "product_id"    : product.id,
#                         "product_name"  : product.name,
#                         "product_price" : int(product.price),
#                         "discount_rate" : product.discount,
#                         "product_image" : [img.url for img in main_image],
#                         "product_tag"   : [{
#                             "new":tag.tag.new, 
#                             "sale":tag.tag.sale, 
#                             "best":tag.tag.best} for tag in tags]
#                     }
#                 )
#             return JsonResponse({"results": results, "total_counts" : len(total), "page_count": PAGE_SIZE}, status=200) 
#         except:
#             return JsonResponse({"MESSAGE": "해당 상품이 존재하지 않습니다.", "status": '404'}, status=404)

# class ProductMainView(View):
#     def get(self, request):
#         new_products  = ProductTag.objects.filter(tag__new=1)
#         best_products = ProductTag.objects.filter(tag__best=1)
#         new_product_lists  =[]
#         best_product_lists =[]
        
#         for new_product in new_products:
#             img = Image.objects.get(Q(is_main=True)&Q(product_id=new_product.product.id))
#             new_product_list = {
#                     'product_id'   :new_product.product.id,
#                     'product_name' :new_product.product.name,
#                     'product_price':int(new_product.product.price),
#                     'product_image':img.url
#                     }
#             new_product_lists.append(new_product_list)

#         for best_product in best_products:
#             img = Image.objects.get(Q(is_main=True)&Q(product_id=best_product.product.id))
#             best_product_list = {
#                     'product_id'   :best_product.product.id,
#                     'product_name' :best_product.product.name,
#                     'product_price':int(best_product.product.price),
#                     'product_image':img.url
#                     }

#             best_product_lists.append(best_product_list)
#         return JsonResponse({"result":{"new":new_product_lists[:18],"best":best_product_lists[:6]}}, status = 200)

# ########################