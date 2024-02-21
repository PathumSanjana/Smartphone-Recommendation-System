# Smartphone Recommendation System

This is a web application that helps users find smartphones similar to the ones they like. It utilizes fuzzy matching to recommend similar smartphones based on the user's input.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/PathumSanjana/Smartphone-Recommendation-System.git

2. **Navigate to the Project Directory:**
   ```bash
   cd smartphone-recommendation-system

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Start the Wave server:**
   ```bash
   waved.exe

5. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   .\\venv\\Scripts\\activate

## Usage
1. **Run the Application:**
   ```bash
   wave run app
   
2. **Access the Application:**
   Open your web browser and go to http://localhost:10101/smartphone-recommender

3. **Search for Smartphones:**
   - Type the name of a smartphone you like into the search box and click "Search".
   - If the smartphone is found in the database, similar smartphones will be displayed.
   - If not found, suggestions will be provided based on fuzzy matching.


## Requirements
- Python 3.x
- h2o Wave
- fuzzywuzzy


## Contributing
- Contributions are welcome! If you have suggestions or find any issues, please open an issue or a pull request on GitHub.


