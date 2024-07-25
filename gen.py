import google.generativeai as genai
import streamlit as st
import json

def generate_recipe(food, profession, dietary_restrictions="", cuisine="", meal_type=""):
    """Generates a recipe based on given parameters.

    Args:
        food: The type of food.
        profession: The target user's profession.
        dietary_restrictions: Any dietary restrictions (optional).
        cuisine: Desired cuisine (optional).
        meal_type: Type of meal (e.g., breakfast, lunch, dinner, optional).

    Returns:
        A dictionary containing the recipe, or None if an error occurs.
    """

    try:
        # Configure API key
        genai.configure(api_key="AIzaSyCHqUPsZJPk1X6D4nYRlZ9wZ6dWfhwIwSk")  # Replace with your actual API key

        # Create the model
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction="You are an expert chef. Create delicious recipes tailored to the user's needs, including food type, profession, dietary restrictions, cuisine, and meal type.",
        )

        # Construct the prompt
        prompt = (
            f"Create a {meal_type} recipe for a {profession} that features {food}. "
            f"Consider dietary restrictions: {dietary_restrictions}. "
            f"Desired cuisine: {cuisine}. "
            f"Include a clear list of ingredients with quantities and detailed instructions."
        )

        # Generate the recipe
        response = model.generate_content(prompt)
        recipe_text = response.text

        # Basic recipe formatting (you can enhance this)
        recipe_dict = {"ingredients": [], "instructions": []}
        current_section = "ingredients"
        for line in recipe_text.split("\n"):
            if line.startswith("Ingredients:"):
                current_section = "ingredients"
            elif line.startswith("Instructions:"):
                current_section = "instructions"
            else:
                recipe_dict[current_section].append(line)

        return recipe_dict

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def main():
    st.title("Recipe Generator")

    # Input fields
    food = st.text_input("Enter the type of food:")
    profession = st.text_input("Enter the profession:")
    dietary_restrictions = st.text_input("Enter dietary restrictions (optional):")
    cuisine = st.text_input("Enter desired cuisine (optional):")
    meal_type = st.text_input("Enter meal type (e.g., breakfast, lunch, dinner, optional):")

    if st.button("Generate Recipe"):
        if food and profession:
            recipe = generate_recipe(food, profession, dietary_restrictions, cuisine, meal_type)
            if recipe:
                st.subheader("Recipe")
                st.write("**Ingredients:**")
                for ingredient in recipe["ingredients"]:
                    st.write(f"- {ingredient}")
                st.write("**Instructions:**")
                for step in recipe["instructions"]:
                    st.write(f"- {step}")
            else:
                st.write("Failed to generate recipe.")
        else:
            st.warning("Please provide both food type and profession.")

if __name__ == "__main__":
    main()
