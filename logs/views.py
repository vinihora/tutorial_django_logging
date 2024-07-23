from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

import logging

logger = logging.getLogger('fidc-credit-assignment.assignment')

# Create your views here.
class TestView(APIView):

    def get(self, request):
        logger.error({
            "message": "Debug Django APP",
            "request": request.data
        })
        return Response(data={"message": "Log succesfully registred!"})