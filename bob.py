import streamlit as st
import pandas as pd
import random
"""
# Let's Get Big
"""
chestPriority = {"Chest Primary": ["Barbell bench press 5x12", "incline dumbbell press 5x12", "Barbell incline dumbell press 5x12", "Dumbbell bench press 5x12", "Decline Dumbell press 5x12", "Decline barbell press 5x12"]}
chestSecondary = {"Chest Secondary": ["Decline flys 4x12","Incline flys 4x12","Flys 4x12","Dips 6x12","Band push-ups 4x12","Straight bar dips 6x12"]}
legPriority = {"Leg Primary": ["Leg Priority 1","Leg Priority 2","Leg Priority 3","Leg Priority 4"]}
legSecondary = {"Leg Secondary":["Leg Secondary 1","Leg Secondary 2","Leg Secondary 3","Leg Secondary 4","Leg Secondary 5","Leg Secondary 6","Leg Secondary 7","Leg Secondary 8","Leg Secondary 9","Leg Secondary 10","Leg Secondary 11","Leg Secondary 12","Leg Secondary 13","Leg Secondary 14","Leg Secondary 15","Leg Secondary 16","Leg Secondary 17","Leg Secondary 18","Leg Secondary 19"]}
backPriority = {"Back Primary":["Back Priority 1","Back Priority 2","Back Priority 3","Back Priority 4","Back Priority 5",]}
backSecondary = {"Back Secondary":["Back Secondary 1","Back Secondary 2","Back Secondary 3","Back Secondary 4","Back Secondary 5","Back Secondary 6","Back Secondary 7","Back Secondary 8","Back Secondary 9","Back Secondary 10","Back Secondary 11","Back Secondary 12","Back Secondary 13","Back Secondary 14","Back Secondary 15","Back Secondary 16","Back Secondary 17","Back Secondary 18","Back Secondary 19","Back Secondary 20"]}
tricep ={"Tricep Workout":["Skullcrushers 4x12", "Rope pull-downs 4x12", "tricep kick-backs 4x12", "band diamond push-ups 4x12"]}
bicep = {"Bicep Workout":["bicep 1", "bicep 2", "bicep 3", "bicep 4", "bicep 5"]}
core = {"Core Workout":["core 1", "core 2", "core 3", "core 4", "core 5"]}



todaysExcersize = st.radio("What we doing today? Chest, leg, back? ", ('chest', 'back', 'leg', 'none'))
todaysSecondaryExcersize = st.radio("Do you want to add these to your workout", ('tricep', 'bicep', 'core', 'none'))
priorityNumber = st.slider("Number of priority excersizes: ", 0, 4)
secondaryNumber = st.slider("Number of secondary exersizes: ", 0, 4)
def randomizer(excersize, priority, secondary):
    if excersize == "chest":
       x = pd.DataFrame(chestPriority)
       y = x.sample(n = priority)
       st.write(y)
       a = pd.DataFrame(chestSecondary)
       b = a.sample(n = int(secondary))
       st.write(b)
        #st.write(*random.sample(chestPriority,priority), sep = "\n")
        #st.write(*random.sample(chestSecondary,secondary))
    elif excersize == "leg":
       x = pd.DataFrame(legPriority)
       y = x.sample(n = priority)
       st.write(y)
       a = pd.DataFrame(legSecondary)
       b = a.sample(n = secondary)
       st.write(b)
        #st.write(*random.sample(legPriority,priority), sep = "\n")
        #st.write(*random.sample(legSecondary,secondary), sep = "\n")
    elif excersize == "back":
       x = pd.DataFrame(backPriority)
       y = x.sample(n = priority)
       st.write(y)
       a = pd.DataFrame(backSecondary)
       b = a.sample(n = secondary)
       st.write(b)
        #st.write(*random.sample(backPriority,priority), sep = "\n")
        #st.write(*random.sample(backSecondary,secondary), sep = "\n")
    elif excersize == "tricep":
       x = pd.DataFrame(tricep)
       y = x.sample(n = 4)
       st.write(y)
      #st.write(*random.sample(tricep, 4), sep = "\n")
    elif excersize == "core":
       x = pd.DataFrame(core)
       y = x.sample(n = 4)
       st.write(y)
      #st.write(*random.sample(core, 4), sep = "\n")
    elif excersize == "bicep":
       x = pd.DataFrame(bicep)
       y = x.sample(n = 4)
       st.write(y)
      #st.write(*random.sample(bicep, 4), sep = "\n"
    else:
       st.write("waffles")
st.write(randomizer(todaysExcersize, priorityNumber, secondaryNumber))
st.write(randomizer(todaysSecondaryExcersize, 0, 0))
