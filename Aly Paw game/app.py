import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

# ----------------------------
# SESSION STATE (memory)
# ----------------------------
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Default Owner")

# ----------------------------
# INPUTS
# ----------------------------
st.subheader("Owner & Pet Info")

owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")

col1, col2, col3 = st.columns(3)

with col1:
    task_title = st.text_input("Task title", value="Morning walk")

with col2:
    task_time = st.text_input("Time (HH:MM)", value="09:00")

with col3:
    frequency = st.selectbox("Frequency", ["daily", "once"], index=0)

# ----------------------------
# ADD TASK BUTTON
# ----------------------------
if st.button("Add task"):
    task = Task(task_title, task_time, frequency)

    if not st.session_state.owner.pets:
        pet = Pet(pet_name, species)
        st.session_state.owner.add_pet(pet)
    else:
        pet = st.session_state.owner.pets[0]

    pet.add_task(task)
    st.success("✅ Task added successfully!")

# ----------------------------
# DISPLAY TASKS
# ----------------------------
st.subheader("📋 Current Tasks")

all_tasks = st.session_state.owner.get_all_tasks()

if all_tasks:
    task_data = [
        {"Time": t.time, "Task": t.description, "Frequency": t.frequency}
        for t in all_tasks
    ]
    st.table(task_data)
else:
    st.info("No tasks yet.")

# ----------------------------
# GENERATE SCHEDULE
# ----------------------------
st.divider()
st.subheader("🗓️ Today's Schedule")

if st.button("Generate schedule"):
    scheduler = Scheduler(st.session_state.owner)
    tasks, conflicts = scheduler.get_today_tasks()

    if tasks:
        st.success("✅ Schedule generated successfully!")

        for task in tasks:
            st.write(f"{task.time} - {task.description}")

    else:
        st.info("No tasks to schedule.")

    # ----------------------------
    # SHOW CONFLICT WARNINGS
    # ----------------------------
    if conflicts:
        st.warning("⚠️ Task conflicts detected!")

        for t1, t2 in conflicts:
            st.write(f"Conflict: '{t1.description}' and '{t2.description}' at {t1.time}")