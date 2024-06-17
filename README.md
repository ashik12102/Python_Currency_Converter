
# Currency Converter Web Application

## Project Overview
This project is part of the **Redi - Python Foundation** course. It demonstrates a currency converter web application built using Python, CSS, and HTML.

## Team Members
- Mohamed Ashik
- Milica Gareski
- Matheus Zago

## Project Description
The Currency Converter Web Application allows users to convert an amount from one currency to another using real-time exchange rates from the Fixer API. The application ensures that the input currencies are valid and provides the converted amount based on the current exchange rates.

## Implementation Details

### Python Backend
- **Currency Validation**: The application validates the input currencies by checking against the Fixer API's available symbols.
- **Amount Validation**: Ensures the entered amount is a positive number.
- **Currency Conversion**: Uses the Fixer API to convert the amount from the source currency to the target currency.

### HTML and CSS Frontend
- **HTML**: Provides the structure for the web application, including input fields for the source and target currencies, the amount to be converted, and a button to trigger the conversion.
- **CSS**: Styles the HTML elements, ensuring a user-friendly and visually appealing interface.

## Code Explanation

### Python Code
1. **Currency Validation Function**: 
   - Prompts the user to input the source and target currencies.
   - Checks the validity of these currencies using the Fixer API.
2. **Amount Validation**: 
   - Prompts the user to input the amount to be converted.
   - Ensures the amount is a valid positive number.
3. **Currency Conversion**: 
   - Constructs a URL with the source and target currencies, and the amount.
   - Sends a GET request to the Fixer API to retrieve the converted amount.
   - Displays the result to the user.


# How to Run the Application
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-repo/currency-converter.git
   ```
2. **Navigate to the Project Directory**:
   ```sh
   cd currency-converter
   ```
3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Application**:
   ```sh
   python main.py
   ```
5. **Open `index.html`** in your web browser to use the web interface.

This project is a collaborative effort demonstrating the integration of Python for backend processing and HTML/CSS for frontend design.

