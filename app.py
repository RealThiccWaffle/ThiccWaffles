import streamlit as st
import pandas as pd
import random

# Define the major muscle groups
muscle_groups = ['Chest', 'Back', 'Shoulders', 'Legs', 'Arms']

# Define the different workout types
workout_types = ['Strength', 'Hypertrophy']

# Define the bodybuilding training models for each muscle group and workout type
training_models = {
    'Chest': {
        'Strength': ['Bench Press', 'Incline Press', 'Dumbbell Flyes'],
        'Hypertrophy': ['Incline Bench Press', 'Cable Crossover', 'Dumbbell Flyes']
    },
    'Back': {
        'Strength': ['Deadlift', 'Barbell Rows', 'Pull-ups'],
        'Hypertrophy': ['Lat Pulldowns', 'Seated Rows', 'T-Bar Rows']
    },
    'Shoulders': {
        'Strength': ['Military Press', 'Push Press', 'Arnold Press'],
        'Hypertrophy': ['Dumbbell Shoulder Press', 'Lateral Raises', 'Rear Delt Flyes']
    },
    'Legs': {
        'Strength': ['Squats', 'Deadlift', 'Leg Press'],
        'Hypertrophy': ['Leg Press', 'Leg Extensions', 'Hamstring Curls']
    },
    'Arms': {
        'Strength': ['Barbell Curl', 'Close-grip Bench Press', 'Skull Crushers'],
        'Hypertrophy': ['Dumbbell Curl', 'Tricep Pushdowns', 'Cable Curls']
    }
}

# Define the user database
user_db = pd.DataFrame(columns=['Username', 'Max Lift', 'Max Reps'])

# Define the streamlit app
def app():
    st.set_page_config(page_title='Workout Generator', page_icon=':muscle:', layout='wide')
    st.title('Random Workout Generator')

    # Check if the user is logged in
    if 'username' not in st.session_state:
        st.write('Please enter a username to log in:')
        username = st.text_input('Username')
        st.session_state['username'] = username
        user_db.loc[len(user_db)] = [username, 0, 0] # Add the user to the database

    # Display the user's data
    st.write('Welcome, ' + st.session_state['username'])
    user_data = user_db[user_db['Username'] == st.session_state['username']]
    st.write('Max Lift: ' + str(user_data['Max Lift'].values[0]))
    st.write('Max Reps: ' + str(user_data['Max Reps'].values[0]))

    # Allow the user to select their training type and muscle group
    st.write('Select your training type and muscle group:')
    col1, col2 = st.columns([2, 1])
    with col1:
        training_type = st.selectbox('Training Type', workout_types)
    with col2:
        muscle_group = st.selectbox('Muscle Group', muscle_groups)

    # Generate a random workout based on the selected training type and muscle group
    exercises = training_models[muscle_group][training_type]
    workout = random.sample(exercises, 3) # Select 3 random exercises

    # Display the workout to the user
    st.write('Your workout for today:')
    for i, exercise in enumerate(workout):
        st.write(str(i+1) + '. ' + exercise)

    # Allow the user to enter their main lift max and reps
    st.write('Enter your main lift max and reps:')
    col1, col2 = st.columns(2)
    with col1:
        max_lift = st.number_input('Max Lift', value=user_data['Max Lift'].values[0], step=5)
    with col2:
        max_reps = st.number_input('Max Reps', value=user_data['Max Reps'].values[0], step=5)
    
    # Update the user's data
    user_db.loc[user_data.index[0], 'Max Lift'] = max_lift
    user_db.loc[user_data.index[0], 'Max Reps'] = max_reps
    
    # Display the user's data in a dataframe and graph
    st.write('Your data:')
    st.write(user_db)
    
    # Show a graph of the user's progress over time
    user_history = user_db[user_db['Username'] == st.session_state['username']]
    user_history = user_history[['Max Lift', 'Max Reps']]
    user_history['Date'] = pd.to_datetime(user_db.index)
    user_history = user_history.set_index('Date')
    st.line_chart(user_history, use_container_width=True)