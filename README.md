Smartphone Recommendation System
This is a web application that helps users find smartphones similar to the ones they like. It utilizes fuzzy matching to recommend similar smartphones based on the user's input.

Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/PathumSanjana/Smartphone-Recommendation-System.git
Navigate to the Project Directory:

bash
Copy code
cd smartphone-recommendation-system
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Start the Wave server:

bash
Copy code
waved.exe
Set up a virtual environment:

bash
Copy code
python -m venv venv
.\venv\Scripts\activate
Usage
Run the Application:

bash
Copy code
wave run app
Access the Application:
Open your web browser and go to http://localhost:10101/smartphone-recommender

Search for Smartphones:

Type the name of a smartphone you like into the search box and click "Search".
If the smartphone is found in the database, similar smartphones will be displayed.
If not found, suggestions will be provided based on fuzzy matching.
Requirements
Python 3.x
h2o Wave
fuzzywuzzy
Contributing
Contributions are welcome! If you have suggestions or find any issues, please open an issue or a pull request on GitHub.
