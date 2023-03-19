import streamlit as st
import random
import itertools

# Define workout exercises and their respective muscle groups
exercises = {
    # ...
}

# Define sets and reps for different fitness levels
sets_and_reps = {
    "Beginner": (3, (10, 12)),
    "Intermediate": (4, (8, 10)),
    "Advanced": (5, (6, 8)),
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

def generate_superset(exercises, muscle_group, num_supersets=2):
    selected_exercises = random.sample(exercises[muscle_group], k=min(num_supersets, len(exercises[muscle_group])))
    superset = " / ".join(selected_exercises)
    return superset

# Button to start generating the workout
if st.button("Generate Workout"):
    # Generate workout
    st.header("Generated Workout")

    sets, rep_range = sets_and_reps[fitness_level]

    if training_type == "Split":
        st.write(f"**Target Muscle Group**: {muscle_group}")
        selected_exercises = random.sample(exercises[muscle_group], k=min(4, len(exercises[muscle_group])))

        for i, exercise in enumerate(selected_exercises):
            reps = random.randint(rep_range[0], rep_range[1])

            if i % 2 == 0 and len(selected_exercises) - i > 1:
                superset = generate_superset(exercises, muscle_group)
                st.write(f"Superset: {superset}: {sets} sets of {reps} reps")
            elif i % 2 != 0:
                pass  # Skip printing because the exercise is part of a superset
            else:
                st.write(f"{exercise}: {sets} sets of {reps} reps")

            if i == len(selected_exercises) - 1 and len(selected_exercises) % 2 != 0:
                st.write(f"Drop set: {exercise}: {sets} sets of {reps} reps (perform drop sets on the last two sets)")

        if extra_exercises != "None":
            st.write("**Extra Exercises**")
            selected_extra_exercises = random.sample(
                exercises[extra_exercises_options[extra_exercises]], k=min(2, len(exercises[extra_exercises_options[extra_exercises]]))
            )
            for exercise in selected_extra_exercises:
                reps = random.randint(rep_range[0], rep_range[1])
                st.write(f"{exercise}: {sets} sets of {reps} reps")

    else:
        for muscle, exercise_list in exercises.items():
            st.write(f"**Target Muscle Group**: {muscle}")
            selected_exercises = random.sample(exercise_list, k=min(3, len(exercise_list)))

            for i, exercise in enumerate(selected_exercises):
                reps = random.randint(rep_range[0], rep_range[1])

                if i % 2 == 0 and len(selected_exercises) - i > 1:
                    superset = generate_superset(exercises, muscle_group)
                    st.write(f"Superset: {superset}: {sets} sets of {reps} reps")
                elif i % 2 != 0:
                    pass  # Skip printing because the exercise is part of a superset
                else:
                    st.write(f"{exercise}: {sets} sets of {reps} reps")

                if i == len(selected_exercises) - 1 and len(selected_exercises) % 2 != 0:
                    st.write(f"Drop set: {exercise}: {sets} sets of {reps} reps (perform drop sets on the last two sets)")

