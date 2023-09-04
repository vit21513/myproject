from django.shortcuts import render
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)
# Create your views here.


def index(request):
    logger.info("index pfge acsees")
    content = {"index": 'Hello people its template rendered'}
    return render(request, "myapp/index.html", content)


def about(request):

    # try:
    #     # some code that might raise an exception
    #     result = 1 / 0
    # except Exception as e:
    #     logger.exception(f'Error in about page: {e}')
    #     return HttpResponse("Oops, something went wrong.")
    # else:
    logger.debug('About page accessed')
    content ={'about':'this page about us'}
    return render(request, "myapp/about.html", content)