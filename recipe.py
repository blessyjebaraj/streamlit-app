import streamlit as st
import requests
import plotly.express as px

def get_recipes(ingredients):
    API_KEY = 'YOUR_API_KEY'
    url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={",".join(ingredients)}&number=5&apiKey={API_KEY}'
    response = requests.get(url)
    return response.json()

def get_nutrition_info(recipe_id):
    API_KEY = 'YOUR_API_KEY'
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/nutritionWidget.json?apiKey={API_KEY}'
    response = requests.get(url)
    return response.json()

def plot_nutrition_graph(nutrition_data):
    fig = px.pie(nutrition_data, names='Nutrient', values='Amount', title='Nutrient Breakdown')
    st.plotly_chart(fig)

# Streamlit UI
st.title('Meal Planner & Recipe Finder')

ingredients_input = st.text_input('Enter available ingredients (comma separated):')
ingredients_list = ingredients_input.split(',')

if ingredients_input:
    recipes = get_recipes(ingredients_list)
    st.write("Here are some recipe suggestions based on the ingredients you have:")
    
    for recipe in recipes:
        st.subheader(recipe['title'])
        st.image(f"https://spoonacular.com/recipeImages/{recipe['id']}-480x360.jpg")
        st.write(f"Ready in {recipe['readyInMinutes']} minutes")
        st.write(f"Used ingredients: {', '.join([i['name'] for i in recipe['missedIngredients']])}")
        
        # Get nutritional info
        nutrition = get_nutrition_info(recipe['id'])
        st.write(f"Calories: {nutrition['calories']}")
        st.write(f"Protein: {nutrition['protein']}g")
        st.write(f"Carbs: {nutrition['carbs']}g")
        st.write(f"Fat: {nutrition['fat']}g")
        
        # Track daily total
        if 'total_calories' not in st.session_state:
            st.session_state.total_calories = 0
        st.session_state.total_calories += nutrition['calories']
        st.write(f"Total calories consumed today: {st.session_state.total_calories}")
        
        # Plot nutrient breakdown
        nutrition_data = {
            'Nutrient': ['Calories', 'Protein', 'Carbs', 'Fat'],
            'Amount': [nutrition['calories'], nutrition['protein'], nutrition['carbs'], nutrition['fat']]
        }
        plot_nutrition_graph(nutrition_data)

