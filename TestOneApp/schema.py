import graphene
from graphene_django.types import DjangoObjectType
from .models import SampleDataModel


class SampleDataObjectType(DjangoObjectType):
    class Meta:
        model = SampleDataModel


class Query(graphene.ObjectType):
    all_sample_data = graphene.List(SampleDataObjectType)

    def resolve_all_sample_data(self, info, **kwargs):
        return SampleDataModel.objects.all()


class CreateSampleData(graphene.Mutation):
    class Arguments:
        FirstName = graphene.String()
        LastName = graphene.String()
        DateOfBirth = graphene.Date()
        Occupation = graphene.String()
        Email = graphene.String()
        MobileNumber = graphene.String()

    sample_data = graphene.Field(SampleDataObjectType)

    def mutate(
        self, info, FirstName, LastName, DateOfBirth, Occupation, Email, MobileNumber
    ):
        sample_data = SampleDataModel(
            FirstName=FirstName,
            LastName=LastName,
            DateOfBirth=DateOfBirth,
            Occupation=Occupation,
            Email=Email,
            MobileNumber=MobileNumber,
        )
        sample_data.save()
        return CreateSampleData(sample_data=sample_data)


class DeleteSampleData(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            sample_data = SampleDataModel.objects.get(pk=id)
            sample_data.delete()
            return DeleteSampleData(success=True)
        except SampleDataModel.DoesNotExist:
            return DeleteSampleData(success=False)


class Mutation(graphene.ObjectType):
    create_sample_data = CreateSampleData.Field()
    delete_sample_data = DeleteSampleData.Field()


# Include the Mutation in the root schema
schema = graphene.Schema(query=Query, mutation=Mutation)
