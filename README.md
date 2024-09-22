
# Financial Chatbot Prototype

This is a simple financial chatbot prototype built using Flask and Python. The chatbot provides predefined responses to queries regarding the financial performance of Tesla, Apple, and Microsoft based on data from the last three fiscal years (2021-2023).

## Features
- Responds to queries about **total revenue**, **net income**, and **total assets** for Tesla, Apple, and Microsoft.
- Allows year-specific queries, returning data for the requested year.
- Provides default responses when an unfamiliar question is asked.
- Simple web interface built using Flask.

## How It Works
1. The user enters a financial query in natural language, such as "What is the total revenue for Tesla in 2022?".
2. The chatbot parses the query to identify the company, financial metric (revenue, net income, or assets), and the year (if specified).
3. The chatbot searches the financial data for the requested information and returns the result. If no year is specified, the chatbot returns the most recent data (2023 by default).
4. If the question is not familiar, the chatbot responds with: "Sorry, I can only provide information on predefined queries."

## Supported Queries
The chatbot can answer questions about:
- Total revenue (e.g., "What is the total revenue for Tesla in 2023?")
- Net income change year-over-year (e.g., "How has net income changed for Apple in 2021?")
- Total assets (e.g., "What are the total assets for Microsoft in 2023?")

If a user asks a question that does not fit these categories, the chatbot will respond with a default message.

### Example Queries:
- "What is the total revenue for Tesla in 2022?"
- "How has net income changed for Apple in 2021?"
- "What are the total assets for Microsoft in 2023?"

## Setup Instructions
1. Clone this repository.
2. Install the required dependencies by running:
   ```
   pip install Flask pandas
   ```
3. Run the Flask application:
   ```
   python app.py
   ```
4. Open your web browser and navigate to `http://127.0.0.1:5000/` to interact with the chatbot.

## File Structure
- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for the web interface.
- `README.md`: Documentation for the project.

## Limitations
- The chatbot only supports predefined financial queries for Tesla, Apple, and Microsoft.
- It only handles three financial metrics: total revenue, net income change, and total assets.
- The chatbot responds with data for the most recent three fiscal years (2021-2023).

## Future Enhancements
- Add support for natural language processing (NLP) to handle more complex and diverse user queries.
- Expand the dataset to include more companies and financial metrics.
- Improve the user interface with advanced features like charts and financial insights.

