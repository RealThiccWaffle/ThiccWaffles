import streamlit as st
import random

def generate_workout(training_type, target_muscle, fitness_level, add_extras):
    workouts = {
        "split": {
            "chest": {
                "beginner": [("Bench Press", 3, 8), ("Push-ups", 3, 12)],
                "intermediate": [("Bench Press", 4, 10), ("Incline Bench Press", 3, 8), ("Push-ups", 3, 15)],
                "advanced": [("Bench Press", 5, 10), ("Incline Bench Press", 4, 8), ("Decline Bench Press", 4, 8), ("Dips", 3, 12)],
            },
            "back": {
                "beginner": [("Pull-ups", 3, 5), ("Bent-over Rows", 3, 8)],
                "intermediate": [("Pull-ups", 4, 8), ("Bent-over Rows", 3, 10), ("Seated Rows", 3, 10)],
                "advanced": [("Pull-ups", 5, 10), ("Bent-over Rows", 4, 10), ("Seated Rows", 4, 10), ("T-bar Rows", 4, 10)],
            },
            "quads": {
                "beginner": [("Squats", 3, 8), ("Lunges", 3, 8)],
                "intermediate": [("Squats", 4, 10), ("Lunges", 3, 10), ("Leg Press", 3, 10)],
                "advanced": [("Squats", 5, 10), ("Lunges", 4, 10), ("Leg Press", 4, 10), ("Hack Squat", 4, 10)],
            },
            "hamstrings": {
                "beginner": [("Romanian Deadlift", 3, 8), ("Lying Leg Curls", 3, 8)],
                "intermediate": [("Romanian Deadlift", 4, 10), ("Lying Leg Curls", 3, 10), ("Seated Leg Curls", 3, 10)],
                "advanced": [("Romanian Deadlift", 5, 10), ("Lying Leg Curls", 4, 10), ("Seated Leg Curls", 4, 10), ("Stiff Leg Deadlift", 4, 10)],
            },
            "biceps": {
                "beginner": [("Bicep Curls", 3, 8), ("Hammer Curls", 3, 8)],
                "intermediate": [("Bicep Curls", 4, 10), ("Hammer Curls", 3, 10), ("Concentration Curls", 3, 10)],
                "advanced": [("Bicep Curls", 5, 10), ("Hammer Curls", 4, 10), ("Concentration Curls", 4, 10), ("Preacher Curls", 4, 10)],
            },
            "triceps": {
                "beginner": [("Tricep Dips", 3, 8), ("Tricep Pushdowns", 3, 8)],
                "intermediate": [("Tricep Dips", 4, 10), ("Tricep Pushdowns", 3, 10), ("Skull Crushers", 3, 10)],
                "advanced": [("Tricep Dips", 5, 10), ("Tricep Pushdowns", 4, 10), ("Skull Crushers", 4, 10), ("Close-grip Bench Press", 4, 10)],
            },
            "shoulders": {
                "beginner": [("Shoulder Press", 3, 8), ("Lateral Raises", 3, 8)],
                "intermediate": [("Shoulder Press", 4, 10), ("Lateral Raises", 3, 10), ("Front Raises", 3, 10)],
                "advanced": [("Shoulder Press", 5, 10), ("Lateral Raises", 4, 10), ("Front Raises", 4, 10), ("Bent-over Reverse Fly", 4, 10)],
            },
            "calves": {
                "beginner": [("Standing Calf Raises", 3, 12), ("Seated Calf Raises", 3, 12)],
                "intermediate": [("Standing Calf Raises", 4, 15), ("Seated Calf Raises", 3, 15), ("Leg Press Calf Raises", 3, 15)],
                "advanced": [("Standing Calf Raises", 5, 15), ("Seated Calf Raises", 4, 15), ("Leg Press Calf Raises", 4, 15), ("Donkey Calf Raises", 4, 15)],
            },
        },
        "full_body": {
            "all": {
                "beginner": [("Squats", 3, 8), ("Bench Press", 3, 8), ("Bent-over Rows", 3, 8), ("Shoulder Press", 3, 8), ("Bicep Curls", 3, 8), ("Tricep Dips", 3, 8), ("Standing Calf Raises", 3, 12)],
                "intermediate": [("Squats", 4, 10), ("Bench Press", 4, 10), ("Bent-over Rows", 4, 10), ("Shoulder Press", 4, 10), ("Bicep Curls", 4, 10), ("Tricep Dips", 4, 10), ("Standing Calf Raises", 4, 15)],
                "advanced": [("Squats", 5, 10), ("Bench Press", 5, 10), ("Bent-over Rows", 5, 10), ("Shoulder Press", 5, 10), ("Bicep Curls", 5, 10), ("Tricep Dips", 5, 10), ("Standing Calf Raises", 5, 15)],
            }
        }
    }

    extra_workouts = {
        "triceps": [("Tricep Dips", 3, 10), ("Tricep Pushdowns", 3, 10), ("Skull Crushers", 3, 10)],
        "biceps": [("Bicep Curls", 3, 10), ("Hammer Curls", 3, 10), ("Concentration Curls", 3, 10)],
        "core": [("Planks", 3, 30), ("Russian Twists", 3, 20), ("Leg Raises", 3, 15)]
    }

    if training_type == "full_body":
        workout = workouts[training_type]["all"][fitness_level]
    else:
        workout = workouts[training_type][target_muscle][fitness_level]
    
    random.shuffle(workout)

    if add_extras != "None":
        workout.extend(random.sample(extra_workouts[add_extras], 2))

    return workout

st.title("Hypertrophy Workout Generator")

training_type = st.selectbox("Choose a training type:", ["split", "full_body"])
if training_type == "split":
    target_muscle = st.selectbox("Choose a target muscle:", ["chest", "back", "quads", "hamstrings", "biceps", "triceps", "shoulders", "calves"])
else:
    target_muscle = "all"
fitness_level = st.selectbox("Choose your fitness level:", ["beginner", "intermediate", "advanced"])
add_extras = st.selectbox("Add extra exercises (optional):", ["None", "triceps", "biceps", "core"])

if st.button("Generate Workout"):
    workout = generate_workout(training_type, target_muscle, fitness_level, add_extras)
    st.write(f"Your {training_type} workout for {target_muscle} (Fitness Level: {fitness_level.capitalize()}):")
    for exercise, sets, reps in workout:
        st.write(f"{exercise}: {sets} sets x {reps} reps")

