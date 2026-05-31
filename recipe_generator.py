import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

# -------------------------------------------------------
# CALL CLAUDE FUNCTION
# -------------------------------------------------------

async def call_claude(ingredients, preferences):
    """
    Sends ingredients and preferences to Claude via the Agent SDK.
    params: ingredients (list) - list of ingredient strings
    preferences (str)  - dietary note e.g. "vegetarian"
    return: (str) Claude's recipe suggestion
    """
    ingredient_text = ", ".join(ingredients)
    prompt = (
        f"I have these ingredients: {ingredient_text}. "
        f"Dietary preference: {preferences}. "
        "Please suggest ONE simple recipe I can make. "
        "Include: recipe name, ingredients needed, and 3-5 short steps. "
        "Keep it concise and beginner-friendly. "
        "Reply with just the recipe, no extra commentary."
        "Do not use any markdown formatting, asterisks, or special symbols."
    )

    result = ""

    # The Agent SDK streams messages back — we collect the final result
    async for message in query(
        prompt=prompt,
        options=ClaudeAgentOptions(allowed_tools=[])  # no file/bash tools needed
    ):
        # ResultMessage contains Claude's final text response
        if hasattr(message, "result") and message.result:
            result = message.result

    return result

# -------------------------------------------------------
# HELPER FUNCTIONS
# -------------------------------------------------------

def get_ingredients():
    """
    Asks the user to enter ingredients one by one.
    return: (list) list of ingredient strings
    """
    ingredients = []
    print("\nEnter your ingredients one at a time.")
    print("Press ENTER with no input when you are done.\n")

    while True:
        ingredient = input("Ingredient: ").strip()
        if ingredient == "":
            break
        ingredients.append(ingredient)

    return ingredients


def get_preferences():
    """
    Asks the user to select a dietary preference.
    return: (str) the selected preference
    """
    options = {
        "1": "no restrictions",
        "2": "vegetarian",
        "3": "vegan",
        "4": "gluten-free"
    }

    print("\nSelect a dietary preference:")
    for key, value in options.items():
        print(f"  {key}. {value}")

    choice = input("\nEnter 1, 2, 3 or 4: ").strip()

    if choice in options:
        return options[choice]
    else:
        print("Invalid choice. Defaulting to no restrictions.")
        return "no restrictions"


def display_ingredients(ingredients):
    """
    Prints the collected ingredients in a neat numbered list.
    params: ingredients (list)
    """
    print("\n--- Your Ingredients ---")
    for i in range(len(ingredients)):
        print(f"  {i + 1}. {ingredients[i]}")
    print("------------------------")


def save_recipe(recipe, ingredients, preferences):
    """
    Stores the session result in a dictionary and prints a summary.
    params: recipe (str), ingredients (list), preferences (str)
    """
    session = {
        "ingredients": ingredients,
        "preference": preferences,
        "recipe": recipe
    }

    print("\n========================================")
    print("           YOUR RECIPE SUGGESTION")
    print("========================================")
    print(session["recipe"])
    print("========================================\n")


# -------------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------------

async def main():
    print("========================================")
    print("       RECIPE IDEA GENERATOR")
    print("         Powered by Claude")
    print("========================================")

    # Step 1: Collect ingredients
    ingredients = get_ingredients()

    # Step 2: Validate - need at least 2 ingredients
    if len(ingredients) < 2:
        print("\nPlease enter at least 2 ingredients. Try again!")
        return

    # Step 3: Show what was entered
    display_ingredients(ingredients)

    # Step 4: Get dietary preference
    preferences = get_preferences()

    # Step 5: Call Claude via Agent SDK
    print("\nAsking Claude for a recipe idea...")
    recipe = await call_claude(ingredients, preferences)

    # Step 6: Display result
    if recipe:
        save_recipe(recipe, ingredients, preferences)
    else:
        print("\nSomething went wrong. Check that you are logged in: run 'claude login'")

    # Step 7: Ask if they want to try again
    again = input("Try with different ingredients? (yes / no): ").strip().lower()
    if again == "yes":
        await main()
    else:
        print("\nHappy cooking!")

# asyncio.run() is needed because the Agent SDK is async
asyncio.run(main())