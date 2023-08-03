# Django GraphQL Project with Postgres Database

This Django project uses GraphQL and a Postgres database to manage SampleData instances. The project provides an API to create and delete SampleData objects.

## Prerequisites

- Python 3.x
- PostgreSQL (Kindly set the variables for the database connection)
- All the dependencies can be found in the requirements.txt file generated using the pip freeze command

## Installation

1. Clone the repository.
2. Navigate to the project directory:

- cd TestOne/

3. Create and activate a virtual environment (optional but recommended):

- python -m venv venv
- source venv/bin/activate # For Windows, use `venv\Scripts\activate`

4. Install the required packages:

- pip install -r requirements.txt

5. Perform database migrations:

- python manage.py makemigrations
- python manage.py migrate

## Running the Project

1. To run the Django development server, execute the following command:

- python manage.py runserver

The GraphQL API will be available at: http://localhost:8000/sampleapi/

You can access the GraphiQL interface at the same URL and interactively test your GraphQL queries.

## Testing the POST and DELETE Requests

For testing POST and DELETE requests, you can use tools like cURL or Postman.

# Testing POST Request

To test the POST request to create a new SampleData instance, you can use cURL or Postman.

cURL:

curl -X POST -H "Content-Type: application/json" -d '{
"query": "mutation { createSampleData(FirstName: \"Michael\", LastName: \"Osei\", DateOfBirth: \"1996-01-01\", Occupation: \"Software Engineer\", Email: \"mosei@gmail.com\", MobileNumber: \"+233548821275\") { sampleData { Id FirstName LastName DateOfBirth Occupation Email MobileNumber } } }"
}' http://localhost:8000/sampleapi/

Postman:

- Set the request type to "POST."
- Set the request URL to http://localhost:8000/sampleapi/.
- Set the request body to raw and choose "JSON" as the data type.
  Use the following JSON payload structure:
  {
  "query": "mutation { createSampleData(FirstName: \"Michael\", LastName: \"Osei\", DateOfBirth: \"1996-01-01\", Occupation: \"Software Engineer\", Email: \"oseim2154@gmail.com\", MobileNumber: \"+233548821275\") { sampleData { Id FirstName LastName DateOfBirth Occupation Email MobileNumber } } }"
  }

# Testing DELETE Request

To test the DELETE request to remove an existing SampleData instance, you can use cURL or Postman.

cURL:

curl -X POST -H "Content-Type: application/json" -d '{
"query": "mutation { deleteSampleData(id: 1) { success } }"
}' http://localhost:8000/sampleapi/

Postman:

- Set the request type to "POST."
- Set the request URL to http://localhost:8000/sampleapi/.
- Set the request body to raw and choose "JSON" as the data type.
- Use the following JSON payload:

{
"query": "mutation { deleteSampleData(id: 1) { success } }"
}

# Note

- Replace '1' with the ID of the SampleData instance you want to delete.
- You should have at least one SampleData instance in the database with the respective ID for the DELETE request to work correctly.
- CSRF has been disabled in urls.py file for testing purposes
- The migrations folder has been cleared to allow a smooth migration process on other hosts
- You can find the test cases in the tests.py file. Run the following command to execute the unit tests: python manage.py test
