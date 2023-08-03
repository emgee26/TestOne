from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from TestOneApp.schema import schema

urlpatterns = [
    path(
        "sampleapi/",
        csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)),
        # GraphQLView.as_view(graphiql=True, schema=schema),
        name="sampleapi",
    ),
]
