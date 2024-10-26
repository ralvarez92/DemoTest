# Instructions
- Install Docker. If you don't have it, visit: [Docker](https://www.docker.com/)
- Download the project from Git.
- Navigate to the project folder and open a terminal.
- Run Docker with the command: `docker compose up --build`.
- Once Docker is up, go to the following URL: `http://localhost:7900/`. This is to better visualize the execution of the project.
- Then execute the command: `docker exec -it test-sauce-demo-ecommerce python3 -m pytest -rP test/test_shopping.py`.

# Conclusions
- The project was developed using Selenium with Python and the pytest framework and run with docker.
- The project architecture is based on two sections: **src** for logic and **test** for test files.
- The design patterns POM (Page Object Model) and Page Object Mother (DTO) are included.
- For item selection, the options are hardcoded in the code; however, the method name "add_to_car_bike_light_and_onesie" indicates the items to select.
- Fake data is used for entering the buyer's information.
- A test was developed that covers the entire purchase process, only including the main steps.