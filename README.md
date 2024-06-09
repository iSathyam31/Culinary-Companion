# Culinary Companion 🍽️🔍
Welcome to the Recipe Culinary-Companion! This project aims to provide personalized recipe suggestions based on user preferences, making meal planning easier and more enjoyable.

## Features

- **Personalized Suggestions**: Users can select their meal time, eating type, and cuisine preferences to receive tailored recipe suggestions.
- **Interactive Interface**: The app features an intuitive and user-friendly interface with dropdown menus and buttons for easy navigation.
- **Visual Appeal**: The app includes images and emojis to enhance the visual appeal and engagement of the user interface.

## Requirements

To run the Recipe Suggestion App locally, you'll need:

- Python 3.x
- Streamlit
- Google Generative AI (Gemini Pro model)
- A Google API key for accessing the Gemini Pro model

## Project Structure

The project structure is organized as follows:
```
recipe-suggestion-app/
│
├── app.py                 # Main Streamlit app script
├── README.md              # Project README file
├── requirements.txt       # Python dependencies
├── food.jpg       # Local image file for the app
├── LICENSE                # License file (e.g., MIT License)
└── .gitignore             # Git ignore file
```

## Getting Started

1. Clone this repository to your local machine:
```
git clone https://github.com/iSathyam31/Culinary-Companion.git
```
2. Install the Python dependencies:
```
pip install -r requirements.txt
```
3. Set up your Google API key:

- Visit the Google Cloud Console.
- Create a new project or select an existing one.
- Enable the Google Generative AI (Gemini) API.
- Create an API key and save it securely.

4. Update the `.env` file with your Google API key:
```
GOOGLE_API_KEY=your-api-key-here

```

5. Run the Streamlit app:
```
streamlit run app.py
```

6. Access the app in your browser at `http://localhost:8501`.

## License
This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.


