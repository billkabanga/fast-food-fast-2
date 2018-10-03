[![Build Status](https://travis-ci.org/billkabanga/fast-food-fast-2.svg?branch=ft-challenge-three-160814023)](https://travis-ci.org/billkabanga/fast-food-fast-2)
[![Coverage Status](https://coveralls.io/repos/github/billkabanga/fast-food-fast-2/badge.svg?branch=ft-challenge-three-160814023)](https://coveralls.io/github/billkabanga/fast-food-fast-2?branch=ft-challenge-three-160814023)

# Fast-food-fast
This is a food delivery service app for a restaurant. An app where customers can place orders for food and get served instantly.

## Getting started
This following information will help you setup and run the application on your local machine.

## Prerequisites
You will need the following:
* Internet
* GIT
* IDE
* Postman

## Project links:
**API endpoints:** The code for the endpoints can be found using the URL: (https://github.com/billkabanga/fast-food-fast-2/tree/ft-challenge-three-160814023)

## Project functionality
**API endpoints**
* Create User accounts that can signin/signout from the app
* Place an order for food.
* Get list of orders.
* Get a specific order.
* Update the status of an order.
* Get the menu
* Add food option to the menu
* View the order history for a particular user.

## Getting the application on the local machine.
* Clone the remote repository to your local machine using the following command: `git  clone https://github.com/billkabanga/fast-food-fast-2.git`
* Navigate to the local repository using `cd` and `code .` if using Visual Studio code will open the code location.
* Create a virtual environment in the local repository using the following code: `python -3 -m venv env`
* Activate the virtual environment: `env/scripts/activate`

## Installing dependencies.
* Use the following command: `pip install -r requirements.txt` , to install the dependencies.
* Run the `psql` command to access the postgreSQL shell interface.
* Create two databases **fastfoodfastdb** and **fastfoodtestdb** using the `CREATE DATABASE {database name}` command.
Application should now be up and ready to test.

## Running tests:
**Testing the API endpoints.**
Run the `run.py` file and test the endpoints in Postman as shown below:

|     Endpoint                        | Verb          | Action                     |   Parameters     | Privileges |
| ----------------------------------- |:-------------:|  ------------------------- | ----------------- | -----------|
| api/v1/auth/signup                     | POST          | Register a user          | username,email,contact,password,role   | client/admin |
| api/v1/auth/login        | POST           | Login a user          | username, password  | client/admin |
| /api/v1/users/orders        | POST          | Place an order for food          | item,quantity | client |
| /api/v1/users/orders | GET     | Get the order history of particular user | none  | client |
| /api/v1/orders | GET     | Get all orders | none | admin |
| /api/v1/orders/<int:orderId> | GET     | Fetch specific order | order_id(URL) | admin |
| /api/v1/orders/<int:orderId> | PUT     | Update status of an order | order_status | admin |
| /api/v1/menu | GET     | Get available menu | none  | client/admin |
| /api/v1/menu | POST     | Add a meal option to the menu | item,price | admin |

**Running unittests for the API endpoints**
* Use the `pytest tests --cov=api --cov-report term-missing` command to run the tests and get the coverage report.

## Deployment:
N/A

## Built with:
**API endpoints**
* Python 3
* Flask
* Flask-restful
* PostgreSQL

## Author:
Author of this project-Twinomuhwezi Kabanga Bill, 
a young aspiring software developer utilising each day as one to learn and provide solutions to world problems.
