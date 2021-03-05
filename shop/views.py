from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Test
from .serializers import TestSerializer

class TestListView(APIView):
    def get(self, request):
        _list = Test.objects.all()

        ser = TestSerializer(_list, many=True) # many=True говорит, что запись будет не одна
        return Response(ser.data)

    def post(self, request):

        name = request.data.get('test')
        ser = TestSerializer(data=name)

        if ser.is_valid(raise_exception=True):
            name_saved = ser.save()
            print(name_saved)
        return Response(name_saved.name)

    def put(self, request, pk):
        saved_test = get_object_or_404(Test.objects.all(), pk=pk)
        data = request.data.get('test')
        ser = TestSerializer(instance=saved_test, data=data, partial=True)

        if ser.is_valid(raise_exception=True):
            test_saved = ser.save()

        return Response(test_saved.name)

    def delete(self, request, pk):
        test = get_object_or_404(Test.objects.all(), pk=pk)
        test.delete()
        return Response(pk, status=204)
