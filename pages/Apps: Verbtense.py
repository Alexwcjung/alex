import streamlit as st
import pandas as pd
import random

# Load the CSV file
csv_url = "https://raw.githubusercontent.com/MK316/241214/refs/heads/main/data/verb_sample.csv"
df = pd.read_csv(csv_url)

# Initialize session state
if "remaining_verbs" not in st.session_state:
    st.session_state.remaining_verbs = df.copy()
if "score" not in st.session_state:
    st.session_state.score = 0
if "trials" not in st.session_state:
    st.session_state.trials = 0
if "current_index" not in st.session_state:
    st.session_state.current_index = -1

# Function to select a random verb
def select_random_verb():
    if st.session_state.remaining_verbs.empty:
        return "All verbs have been completed!"
    st.session_state.current_index = random.randint(0, len(st.session_state.remaining_verbs) - 1)
    selected_verb = st.session_state.remaining_verbs.iloc[st.session_state.current_index]
    return f"Verb: {selected_verb['Verb']}"

# Function to check the user's classification and verb forms
def check_answer(user_classification, user_forms):
    if st.session_state.remaining_verbs.empty:
        return "All verbs have been completed!", f"Score: {st.session_state.score}/{st.session_state.trials}"

    index = st.session_state.current_index
    if index == -1:
        return "Please click 'Show the Verb' first.", f"Score: {st.session_state.score}/{st.session_state.trials}"

    verb_data = st.session_state.remaining_verbs.iloc[index]
    verb = verb_data['Verb']
    past = verb_data['Past']
    pp = verb_data['PP']
    regularity = verb_data['Regularity']

    # Update trials
    st.session_state.trials += 1

    # Parse the user input
    user_parts = [part.strip().lower() for part in user_forms.split(",") if part.strip()]
    if len(user_parts) != 2:
        return "Please provide both Past and Past Participle transformations separated by a comma.", f"Score: {st.session_state.score}/{st.session_state.trials}"

    user_past, user_pp = user_parts

    # Check user's answers
    regularity_correct = user_classification.lower() == regularity.lower()
    past_correct = user_past == past.lower()
    pp_correct = user_pp == pp.lower()

    if regularity_correct and past_correct and pp_correct:
        st.session_state.score += 1
        feedback = f"Correct! {verb} - Past: {past}, PP: {pp} - Regularity: {regularity}"
        # Remove the verb from the remaining list
        st.session_state.remaining_verbs = st.session_state.remaining_verbs.drop(st.session_state.remaining_verbs.index[index])
    else:
        feedback = (
            f"Incorrect. Correct: Regularity={regularity}, Past={past}, PP={pp}. "
            f"You entered: Regularity={user_classification}, Past={user_past}, PP={user_pp}."
        )

    if st.session_state.remaining_verbs.empty:
        return "All verbs have been completed!", f"Score: {st.session_state.score}/{st.session_state.trials}"

    return feedback, f"Score: {st.session_state.score}/{st.session_state.trials}"

# Streamlit interface
st.title("🍇VerbMaster: Verb Tense Checking")
st.markdown("""
1. Click the 'Show the Verb' button.
2. Choose regular/irregular.
3. Enter the past and past participle (comma-separated) (e.g., "liked, liked").
4. Click the 'Submit' button.
5. Check your score: Your score will be displayed below.
6. Play again: To continue, click the 'Show the Verb' button and try another verb.
""")

# Button to display a verb
if st.button("Show the Verb"):
    verb_details = select_random_verb()
    st.session_state.verb_details = verb_details

# Display the verb
verb_details = st.session_state.get("verb_details", "Click 'Show the Verb' to start.")
st.text(verb_details)

# Radio buttons for regularity question
user_classification = st.radio("Is the verb regular or irregular?", ["Regular", "Irregular"])

# Input field for past and past participle transformations
user_forms = st.text_input("Enter Past and Past Participle (comma-separated)")

# Submit button and feedback
if st.button("Submit"):
    feedback, score = check_answer(user_classification, user_forms)
    st.text(feedback)
    st.text(score)
