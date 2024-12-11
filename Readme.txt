-------------------------------------------------------
IMPORTANT:
    It is required to check two endpoints:
        http://127.0.0.1:8000/restaurant/menu/ - It allows to CRUD Menu Items
        http://127.0.0.1:8000/restaurant/booking/tables/ - It allows to CRUD Booking Tables

    And static content delivery with vanilla Django *:
        http://127.0.0.1:8000/restaurant/

    * For Capstone project it is not required to delivery full website, ONLY TWO ENDPOINTS and static delivery.
    If you want to check fullstack website, there is directory Fullstack that contains whole project.
    If you want to run it, extract Fullstack directory and set up a new virtual enviroment with
    requirements available in piplock file.

    Let's move then to Capstone project.
-------------------------------------------------------

Capstone project notes:
    To install dependencies you can use pip install -r requirements.txt
    This project uses mysql

Credentials:
    Superuser (django admin panel):
        Username: admin
        Password: admin

    DRF user:
        Email: test@little.com
        Username: testuser
        Password: youcantest123

Main endpoints:
    http://127.0.0.1:8000/restaurant/menu/ - It allows to CRUD Menu Items
    http://127.0.0.1:8000/restaurant/booking/tables/ - It allows to CRUD Booking Tables
    http://127.0.0.1:8000/auth/ - All endpoints provided by Djoser library
    http://127.0.0.1:8000/restaurant/api-token-auth/ - Custom token getter endpoint with DRF user credentials as JSON payload
    http://127.0.0.1:8000/restaurant/ - static content delivery with vanilla Django
    http://127.0.0.1:8000/admin/ - Django Admin Panel

Menu API endpoints operations:
    To get token:
        url: http://127.0.0.1:8000/restaurant/api-token-auth/
        username: testuser
        password: youcantest123
        method: POST

    To get menu items or post (token needed):
        url: http://127.0.0.1:8000/restaurant/menu/
        token: 4d4d3943f4327915881acd06350f2af96d7405e0
        method: GET or POST with JSON load
        console: [11/Dec/2024 15:07:55] "POST /restaurant/menu/ HTTP/1.1" 201 61
                 [11/Dec/2024 15:08:02] "GET /restaurant/menu/ HTTP/1.1" 200 140
        result:
        {
            "title": "Salami Pizza",
            "price": "22.00",
            "inventory": 8
        }
        
    To edit menu items (token needed):
        url: http://127.0.0.1:8000/restaurant/menu/2
        token: 4d4d3943f4327915881acd06350f2af96d7405e0
        method: PUT with JSON load
        console: [11/Dec/2024 15:08:49] "PUT /restaurant/menu/2 HTTP/1.1" 200 61
        result:
        {
            "title": "Salami Pizza",
            "price": "26.00",
            "inventory": 8
        }

    To delete menu item (token need):
        url: http://127.0.0.1:8000/restaurant/menu/2
        token: 4d4d3943f4327915881acd06350f2af96d7405e0
        method: DELETE
        console: [11/Dec/2024 15:15:22] "DELETE /restaurant/menu/2 HTTP/1.1" 204 0

Booking tables API endpoints operations:
    To get booking tables or post:
        url: http://127.0.0.1:8000/restaurant/booking/tables/
        token: 4d4d3943f4327915881acd06350f2af96d7405e0
        method: GET or POST with JSON load
        console: [11/Dec/2024 16:32:50] "POST /restaurant/booking/tables/ HTTP/1.1" 201 69
                 [11/Dec/2024 16:32:54] "GET /restaurant/booking/tables/ HTTP/1.1" 200 140
        result:
        [
            {
                "id": 1,
                "name": "Jamie",
                "no_of_guests": 4,
                "booking_date": "2024-12-10"
            }
        ]
    To edit booking tables:
        url: http://127.0.0.1:8000/restaurant/booking/tables/1/
        token: 4d4d3943f4327915881acd06350f2af96d7405e0
        method: PUT
        console: [11/Dec/2024 16:36:11] "PUT /restaurant/booking/tables/1/ HTTP/1.1" 200 68
        result:
        {
            "id": 1,
            "name": "Jamie",
            "no_of_guests": 2,
            "booking_date": "2024-12-10"
        }

    to delete booking tables:
        url: http://127.0.0.1:8000/restaurant/booking/tables/1/
        token: 4d4d3943f4327915881acd06350f2af96d7405e0
        method: DELETE
        console: [11/Dec/2024 16:38:08] "DELETE /restaurant/booking/tables/1/ HTTP/1.1" 204 0




