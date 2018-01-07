from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status

from . import serializers

# Create your views here.

class HelloAPIView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_APIview = [
        "Uses HTTP methods as function (get, post, patch, put, delete)", "It is similar to a traditional Django view", "It eats butts so you can focus on licking farts", "Gives you the most control over your logic", "Is mapped manually to URLs"
        ]

        return Response({"message": "Hello!", "apiView": an_APIview})

    def post(self, request):
        """create a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get("name")
            message = "Hello {}".format(name)
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object"""

        return Response({"Method": "put"})

    def patch(self, request, pk=None):
        """patch request only updates fields provided in request"""

        return response({"method": "patch"})

    def delete(self, request, pk=None):
        """Deletes an object"""

        return Response({"method": "delete"})
