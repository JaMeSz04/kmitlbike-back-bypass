from django.shortcuts import render

from kmitl_bike_django.utils import AbstractAPIView


class GetTermsConditionsView(AbstractAPIView):

    def get(self, request):
        return render(request, "terms_conditions.html")


def as_view():
    return GetTermsConditionsView.as_view()
