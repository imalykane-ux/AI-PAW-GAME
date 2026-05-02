from pawpal_system import Task, Pet, Owner, Scheduler

# Create owner and pets
owner = Owner("Aly")

dog = Pet("Max", "Dog")
cat = Pet("Luna", "Cat")

owner.add_pet(dog)
owner.add_pet(cat)

# Add tasks (intentionally out of order + conflict)
dog.add_task(Task("Walk dog", "09:00", "daily"))
cat.add_task(Task("Feed cat", "08:00", "daily"))
dog.add_task(Task("Vet visit", "14:00", "once"))
dog.add_task(Task("Feed dog", "09:00", "daily"))  # conflict

# Scheduler
scheduler = Scheduler(owner)

tasks, conflicts = scheduler.get_today_tasks()

print("\nToday's Schedule:")
for task in tasks:
    print(f"{task.time} - {task.description}")

# Show conflicts
if conflicts:
    print("\n⚠️ Conflicts detected:")
    for t1, t2 in conflicts:
        print(f"{t1.description} conflicts with {t2.description}")
else:
    print("\nNo conflicts detected.")