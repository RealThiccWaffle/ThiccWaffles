import streamlit as st

# Define workout exercises and their respective muscle groups
exercises = {
    "Chest": ["Bench Press", "Incline Bench Press", "Dumbbell Flyes", "Chest Dips", "Push-Ups"],
    "Back": ["Deadlift", "Bent Over Rows", "Pull-Ups", "Chin-Ups", "Lat Pulldown"],
    "Legs": ["Squats", "Leg Press", "Lunges", "Leg Curls", "Calf Raises"],
    "Shoulders": ["Military Press", "Lateral Raises", "Front Raises", "Rear Delt Flyes", "Arnold Press"],
    "Arms": ["Bicep Curls", "Tricep Dips", "Hammer Curls", "Skull Crushers", "Concentration Curls"],
}

# Define sets and reps for different fitness levels
sets_and_reps = {
    "Beginner": (3, 10),
    "Intermediate": (4, 8),
    "Advanced": (5, 6),
}

# Create Streamlit app
st.title("Hypertrophy Workout Generator")

# Get user inputs
training_type = st.selectbox("Choose training type:", ["Split", "Full Body"])
muscle_group = st.selectbox("Choose a muscle group:", list(exercises.keys()))
fitness_level = st.selectbox("Choose your fitness level:", list(sets_and_reps.keys()))

# Generate workout
st.header("Generated Workout")

sets, reps = sets_and_reps[fitness_level]

if training_type == "Split":
    st.write(f"**Target Muscle Group**: {muscle_group}")
    for exercise in exercises[muscle_group]:
        st.write(f"{exercise}: {sets} sets of {reps} reps")
else:
    for muscle, exercise_list in exercises.items():
        st.write(f"**Target Muscle Group**: {muscle}")
        for exercise in exercise_list[:2]:  # Select the first two exercises for each muscle group
            st.write(f"{exercise}: {sets} sets of {reps} reps")
