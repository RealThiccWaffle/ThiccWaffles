import streamlit as st
import random

# Define workout exercises and their respective muscle groups
exercises = {
    "Chest": [
        "Bench Press", "Incline Bench Press", "Decline Bench Press", "Dumbbell Flyes", "Chest Dips", "Push-Ups", "Cable Crossovers",
        "Pec Deck Flyes", "Dumbbell Pullover"
    ],
    "Back": [
        "Deadlift", "Bent Over Rows", "T-Bar Rows", "Pull-Ups", "Chin-Ups", "Lat Pulldown", "Seated Cable Rows",
        "One-Arm Dumbbell Rows", "Cable Face Pulls", "Inverted Rows"
    ],
    "Legs": [
        "Squats", "Leg Press", "Lunges", "Leg Curls", "Calf Raises", "Leg Extensions", "Romanian Deadlift", "Glute Bridges",
        "Bulgarian Split Squats", "Box Jumps", "Hack Squats"
    ],
    "Shoulders": [
        "Military Press", "Lateral Raises", "Front Raises", "Rear Delt Flyes", "Arnold Press", "Upright Rows", "Face Pulls", "Shrugs",
        "Push Press", "Dumbbell Press", "Cuban Press"
    ],
    "Arms": [
        "Bicep Curls", "Tricep Dips", "Hammer Curls", "Skull Crushers", "Concentration Curls", "Preacher Curls",
        "Overhead Tricep Extension", "Rope Pushdown", "Close-Grip Bench Press", "EZ Bar Curl", "Drag Curl", "Dumbbell Kickback"
    ],
    "Core": [
        "Plank", "Russian Twist", "Hanging Leg Raise", "Bicycle Crunch", "Leg Raises", "Mountain Climber", "Ab Wheel Rollout",
        "Dead Bug", "Reverse Crunch", "Flutter Kicks", "Sit-Ups", "Standing Cable Crunch"
    ],
}

# Define sets and reps for different fitness levels
sets_and_reps = {
    "Beginner": (3, 10),
    "Intermediate": (4, 8),
    "Advanced": (5, 6),
}

# Create Streamlit app
st.set_page_config(page_title="Hypertrophy Workout Generator", layout="wide")
st.title("Hypertrophy Workout Generator")

# Set up columns for input
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    training_type = st.selectbox("Training type:", ["Split", "Full Body"])
with col2:
    muscle_group = st.selectbox("Muscle group:", list(exercises.keys()))
with col3:
    fitness_level = st.selectbox("Fitness level:", list(sets_and_reps.keys()))
with col4:
    extra_exercises_options = {"None": None, "Bicep": "Arms", "Tricep": "Arms", "Core": "Core"}
    extra_exercises = st.selectbox("Add extra exercises:", list(extra_exercises_options.keys()))

# Button to start generating the workout
if st.button("Generate Workout"):
    # Generate workout
    st.header("Generated Workout")

    sets, reps = sets_and_reps[fitness_level]

    if training_type == "Split":
        st.write(f"**Target Muscle Group**: {muscle_group}")
        selected_exercises = random.sample(exercises[muscle_group], k=min(3, len(exercises[muscle_group])))
        for exercise in selected_exercises:
            st.write(f"{exercise}: {sets} sets of {reps} reps")

        if extra_exercises != "None":
            st.write("**Extra Exercises**")
            selected_extra_exercises = random.sample(
                exercises[extra_exercises_options[extra_exercises]], k=min(2, len(exercises[extra_exercises_options[extra_exercises]]))
            )
            for exercise in selected_extra_exercises:
                st.write(f"{exercise}: {sets} sets of {reps} reps")

    else:
        for muscle, exercise_list in exercises.items():
            st.write(f"**Target Muscle Group**: {muscle}")
            selected_exercises = random.sample(exercise_list, k=min(2, len(exercise_list)))
            for exercise in selected_exercises:
                st.write(f"{exercise}: {sets} sets of {reps} reps")
