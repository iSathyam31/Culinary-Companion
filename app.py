import streamlit as st
import google.generativeai as genai
import os
import textwrap

# Configure the API key for the Gemini Pro model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input, prompt])
    return response.text

# Streamlit app setup
st.title("🍽️ Recipe Suggestion App 🥗")
st.markdown("---")

# Sidebar for user input
with st.sidebar:
    st.title("Preferences")
    time = st.selectbox("Select meal time:", ["🥞 Breakfast", "🍲 Lunch", "🍝 Dinner"])
    eating_type = st.selectbox("Select eating type:", ["🥦 Vegetarian", "🍗 Non Vegetarian"])
    cuisine = st.selectbox("Select cuisine:", ["🇮🇳 North Indian", "🇮🇳 South Indian", "🍕 Italian", "🍜 Chinese", "🍣 Japanese", "🇰🇷 Korean", "🇺🇸 American", "🇫🇷 French", "🇩🇪 German"])
    submit_button = st.button("🔍 Get Recipe Suggestions")
    st.markdown("---")
    st.write("🔥 Looking for inspiration? Try different combinations!")

# Main content area
st.image("food.jpeg", use_column_width=True)

st.header("Welcome to Recipe Suggestion App! 🎉")
st.write("Select your preferences on the sidebar to get personalized recipe suggestions.")
st.markdown("---")

if submit_button:
    if time and eating_type and cuisine:
        prompt_template = """
        Based on the user's requirements, suggest 5 dishes along with their recipes. Ensure the recipes are detailed. If the requirements do not match any known recipes, please state that clearly.

        Requirements:
        - Time: {time}
        - Eating Type: {eating_type}
        - Cuisine: {cuisine}

        Suggested Dishes and Recipes:
        """
        prompt = prompt_template.format(time=time.split()[1], eating_type=eating_type.split()[1], cuisine=cuisine.split()[1])
        response = get_gemini_response(prompt, "Ask Google Gemini Pro")
        
        st.header("Suggested Dishes and Recipes: 🍽️")
        st.markdown(textwrap.indent(response, "> ", predicate=lambda _: True))
    else:
        st.warning("⚠️ Please provide all the inputs.")
