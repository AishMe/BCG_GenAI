from flask import Flask, render_template, request

app = Flask(__name__)

# Financial data for Tesla, Apple, and Microsoft
financial_data = {
    "Tesla": {
        "Revenue": {2021: 53823, 2022: 81462, 2023: 96773},
        "Net Income": {2021: 5644, 2022: 12587, 2023: 14974},
        "Assets": {2021: 62131, 2022: 82338, 2023: 106618}
    },
    "Apple": {
        "Revenue": {2021: 365817, 2022: 394328, 2023: 383934},
        "Net Income": {2021: 94680, 2022: 99803, 2023: 96995},
        "Assets": {2021: 351002, 2022: 352755, 2023: 352583}
    },
    "Microsoft": {
        "Revenue": {2021: 168088, 2022: 198270, 2023: 211915},
        "Net Income": {2021: 61271, 2022: 72738, 2023: 70583},
        "Assets": {2021: 333779, 2022: 364840, 2023: 411179}
    }
}

def simple_chatbot(user_query):
    # Extract year from query, default to latest year
    year = None
    for y in [2021, 2022, 2023]:
        if str(y) in user_query:
            year = y
            break

    if year is None:
        year = 2023  # Default year if not specified

    # Process total revenue query
    if "total revenue" in user_query.lower():
        for company in financial_data.keys():
            if company.lower() in user_query.lower():
                if year in financial_data[company]["Revenue"]:
                    return f"The total revenue for {company} in {year} was ${financial_data[company]['Revenue'][year]} million."
    
    # Process net income query
    elif "net income" in user_query.lower():
        for company in financial_data.keys():
            if company.lower() in user_query.lower():
                if year in financial_data[company]["Net Income"]:
                    prev_year = year - 1
                    if prev_year in financial_data[company]["Net Income"]:
                        change = (financial_data[company]["Net Income"][year] - financial_data[company]["Net Income"][prev_year]) / financial_data[company]["Net Income"][prev_year] * 100
                        return f"The net income for {company} changed by {change:.2f}% from {prev_year} to {year}."
                    else:
                        return f"No data available for net income change for {company} in {year}."

    # Process total assets query
    elif "total assets" in user_query.lower():
        for company in financial_data.keys():
            if company.lower() in user_query.lower():
                if year in financial_data[company]["Assets"]:
                    return f"The total assets for {company} in {year} were ${financial_data[company]['Assets'][year]} million."
    
    # Default response for unfamiliar queries
    return "Sorry, I can only provide information on predefined queries like total revenue, net income, and total assets for Tesla, Apple, and Microsoft."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_query = request.form['query']
    response = simple_chatbot(user_query)
    return render_template('index.html', query=user_query, response=response)

if __name__ == '__main__':
    app.run(debug=True)
