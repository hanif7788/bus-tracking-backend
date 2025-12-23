from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DeviceLocation
from .serializers import DeviceLocationSerializer

@api_view(['POST'])
def update_location(request):
    serializer = DeviceLocationSerializer(data=request.data)

    if serializer.is_valid():
        # delete old location for same device id
        DeviceLocation.objects.filter(device_id=request.data["device_id"]).delete()
        serializer.save()
        return Response({"status": "success"})

    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_location(request, device_id):
    try:
        loc = DeviceLocation.objects.get(device_id=device_id)
        serializer = DeviceLocationSerializer(loc)
        return Response(serializer.data)
    except DeviceLocation.DoesNotExist:
        return Response({"error": "Device not found"}, status=404)
