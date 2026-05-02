from pawpal_system import Task, Pet, Owner, Scheduler


def test_mark_complete():
    task = Task("Feed", "08:00", "daily")
    task.mark_complete()
    assert task.is_complete == True


def test_add_task():
    pet = Pet("Max", "Dog")
    task = Task("Walk", "09:00", "daily")
    pet.add_task(task)
    assert len(pet.tasks) == 1


def test_sorting():
    owner = Owner("Aly")
    pet = Pet("Max", "Dog")
    owner.add_pet(pet)

    pet.add_task(Task("Task1", "10:00", "daily"))
    pet.add_task(Task("Task2", "08:00", "daily"))

    scheduler = Scheduler(owner)
    tasks, _ = scheduler.get_today_tasks()

    assert tasks[0].time == "08:00"


def test_conflicts():
    owner = Owner("Aly")
    pet = Pet("Max", "Dog")
    owner.add_pet(pet)

    pet.add_task(Task("Task1", "09:00", "daily"))
    pet.add_task(Task("Task2", "09:00", "daily"))

    scheduler = Scheduler(owner)
    _, conflicts = scheduler.get_today_tasks()

    assert len(conflicts) > 0