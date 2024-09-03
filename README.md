# Time Scraper Project

This project uses the `requests` library to fetch the HTML from Time.com, and the `html.parser` library to parse the HTML and extract the latest 6 news stories. The `Flask` library is used to create a simple web API that returns the latest stories in JSON format.

## How to Run the Project

1. Create a new project directory and add the above files to it.
2. Open a terminal in the project directory.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Run the app by running `python app.py`.
5. Open a web browser and navigate to `http://localhost:5000` to test the app.