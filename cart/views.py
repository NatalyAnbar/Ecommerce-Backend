from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from . import models,Serializers
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response

class CartView(ModelViewSet):
    serializer_class = Serializers.CartSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return models.Cart.objects.prefetch_related('cart_items').filter(user=user)
        if self.action == 'list':
            return models.Cart.objects.none()
        return models.Cart.objects.prefetch_related('cart_items').filter(user=None)

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            if models.Cart.objects.filter(user=user).exists():
                return Response({"Cart already exist"})
            serializer.save(user=user)
        else:
            serializer.save()


class CartItemView(ModelViewSet):
    serializer_class = Serializers.CartItemSerializer

    def get_queryset(self):
        pk = self.kwargs['cart_pk']
        if pk:
            return models.CartItem.objects.select_related('product_cart_items').filter(cart_id=pk)
        return models.CartItem.objects.select_related('product_cart_items').all()

    def perform_create(self, serializer):
        pk = self.kwargs['cart_pk']
        try:
            cart = models.Cart.objects.get(cart_id=pk)
        except models.Cart.DoesNotExist:
            return Response('Cart does not exsist')
        serializer.save(cart=cart)


class AddItemView(ModelViewSet):
    queryset = models.CartItem.objects.all()
    serializer_class = Serializers.AddItemSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if user.is_authenticated:
            serializer.save()


class MergeCartView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        visitor_id = self.request.data.get('cart_id')
        try:
            visitor_cart = models.Cart.objects.get(id=visitor_id,user=None)
        except models.Cart.DoesNotExist:
            return Response({'msg' : 'Cart already merged'})
        user = self.request.user
        user_cart,created = models.Cart.objects.get_or_create(user=user)
        items = visitor_cart.cart_items.all()
        for item in items:
            new_item,created = models.CartItem.objects.get_or_create(
                cart = user_cart,
                product = item.product,
                defaults={'quantity': item.quantity}
            )
            if not created :
                new_item.quantity += item.quantity
                new_item.save()
        visitor_cart.delete()
        return Response({'Cart merged successfully':Serializers.CartSerializer(user_cart).data})



        

        
        