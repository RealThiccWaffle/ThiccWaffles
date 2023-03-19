
Bodybuilding Workout Generator

Model: Default (GPT-3.5)

RealThiccWaffle
Create a streamlit python app with goal of being used on mobile, it should be able to output a workout woth the selected training type and muscle type. You should include all major muscle types. Use knowledge of bodybuilding training models to determine the random workout. Make it look super easy to use. And add a user login with no password, so people can hold data about their main lift max and reps and so they can see it in a dataframe graph

Sure, I can help you create a streamlit python app with the goal of being used on mobile. Here's a basic outline of what the app will do:

Display a welcome message and ask the user to select their training type (strength or hypertrophy) and muscle group.
Generate a random workout based on the selected training type and muscle group using bodybuilding training models.
Display the workout to the user in an easy-to-read format.
Allow the user to log in with a unique username and store their main lift max and reps in a database.
Display the user's data in a dataframe and graph so they can easily track their progress over time.
Here's some sample code to get you started:

python
Copy code
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
    training_type = st.selectbox('Select your training type:', workout_types)
    muscle_group = st.selectbox('Select your muscle group:', muscle_groups)

    # Generate a random workout based on the selected training type and muscle group
    exercises = training_models[muscle_group][

    exercises = training_models[muscle_group][training_type]
workout = random.sample(exercises, 3) # Select 3 random exercises

# Display the workout to the user
st.write('Your workout for today:')
for i, exercise in enumerate(workout):
    st.write(str(i+1) + '. ' + exercise)

# Allow the user to enter their main lift max and reps
st.write('Enter your main lift max and reps:')
max_lift = st.number_input('Max Lift', value=user_data['Max Lift'].values[0])
max_reps = st.number_input('Max Reps', value=user_data['Max Reps'].values[0])

# Update the user's data
user_db.loc[user_data.index[0], 'Max Lift'] = max_lift
user_db.loc[user_data.index[0], 'Max Reps'] = max_reps

# Display the user's data in a dataframe and graph
st.write('Your data:')
st.write(user_db)
st.line_chart(user_db[['Max Lift', 'Max Reps']])
