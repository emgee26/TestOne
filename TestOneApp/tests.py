from django.test import TestCase
from .models import SampleDataModel


class SampleDataViewTestCase(TestCase):
    def setUp(self):
        self.sample_data = SampleDataModel.objects.create(
            FirstName="Michael",
            LastName="Osei",
            DateOfBirth="1996-01-01",
            Occupation="Engineer",
            Email="mosei27@gmail.com",
            MobileNumber="+233588832989",
        )

    def test_sample_data_list_query(self):
        query = """
            query {
                allSampleData {
                    Id
                    FirstName
                    LastName
                    DateOfBirth
                    Occupation
                    Email
                    MobileNumber
                }
            }
        """
        response = self.client.post(
            "/sampleapi/", {"query": query}, content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(str(self.sample_data.Id), response.content.decode())
        self.assertIn(self.sample_data.FirstName, response.content.decode())
        self.assertIn(self.sample_data.LastName, response.content.decode())

    def test_sample_data_create_mutation(self):
        mutation = """
            mutation {
                createSampleData(
                    FirstName: "April",
                    LastName: "Jessie",
                    DateOfBirth: "1995-05-05",
                    Occupation: "Designer",
                    Email: "apriljess@gmail.com",
                    MobileNumber: "+987654321"
                ) {
                    sampleData {
                        Id
                        FirstName
                        LastName
                        DateOfBirth
                        Occupation
                        Email
                        MobileNumber
                    }
                }
            }
        """
        response = self.client.post(
            "/sampleapi/", {"query": mutation}, content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("April", response.content.decode())
        self.assertIn("Jessie", response.content.decode())

    def test_sample_data_delete_mutation(self):
        mutation = (
            """
            mutation {
                deleteSampleData(id: %d) {
                    success
                }
            }
        """
            % self.sample_data.Id
        )
        response = self.client.post(
            "/sampleapi/", {"query": mutation}, content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("success", response.content.decode())
