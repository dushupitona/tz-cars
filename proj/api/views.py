from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from car_manager.models import CarModel, CommentModel
from api.serializers import CarListSerializer, CarSerializer, CarCreateSerializer, UpdateCarSerializer, CommentSerializer, CommentCreateSerializer

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response

from api.permissions import OwnerPermission
from django.http import Http404



# просмотр/обновление характеристик машины, удаление машины
class CarDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, OwnerPermission)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CarSerializer
        elif self.request.method == 'PUT':
            return UpdateCarSerializer
    
    def get_object(self):
        pk = self.kwargs['pk']
        try:
            obj = CarModel.objects.select_related('owner').get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except CarModel.DoesNotExist:
            raise Http404({'error': 'Invalid car id'})
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': 'Success'})
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Car deleted successfully'})


# просмотр списка id машин/добавление машины
class CarAPIView(ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)    
    queryset = CarModel.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CarListSerializer
        elif self.request.method == 'POST':
            return CarCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_token = request.auth.key
        serializer.validated_data['owner'] = Token.objects.select_related('user').get(key=user_token).user
        self.perform_create(serializer)

        return Response({'message': 'Success'})
    
    
# просмотр/добавление комментариев
class CommentAPIView(ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)  

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentSerializer
        elif self.request.method == 'POST':
            return CommentCreateSerializer
    

    def get_queryset(self):
        car_id = self.kwargs['pk']
        return CommentModel.objects.select_related('author').filter(car_id=car_id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        car_id = self.kwargs['pk']

        try:
            car = CarModel.objects.get(pk=car_id)
        except CarModel.DoesNotExist:
            raise Http404({'error': 'Invalid car id'})

        user_token = request.auth.key
        serializer.validated_data['author'] = Token.objects.select_related('user').get(key=user_token).user
        serializer.validated_data['car_id'] = self.kwargs['pk']
        self.perform_create(serializer)

        return Response({'message': 'Success'})