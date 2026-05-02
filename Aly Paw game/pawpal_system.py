from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    description: str
    time: str
    frequency: str
    is_complete: bool = False

    def mark_complete(self):
        """Mark the task as completed."""
        self.is_complete = True


@dataclass
class Pet:
    name: str
    type: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to the pet."""
        self.tasks.append(task)

    def get_tasks(self):
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to the owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return all tasks across all pets."""
        tasks = []
        for pet in self.pets:
            tasks.extend(pet.tasks)
        return tasks


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_today_tasks(self):
        """Get sorted tasks and detect conflicts."""
        tasks = self.owner.get_all_tasks()
        sorted_tasks = self.sort_tasks_by_time(tasks)
        conflicts = self.detect_conflicts(sorted_tasks)
        return sorted_tasks, conflicts   # ✅ FIXED

    def sort_tasks_by_time(self, tasks: List[Task]):
        """Sort tasks by time (HH:MM format)."""
        return sorted(tasks, key=lambda t: t.time)

    def filter_tasks(self, completed=None, pet_name=None):
        """Filter tasks by completion status or pet name."""
        tasks = self.owner.get_all_tasks()

        if completed is not None:
            tasks = [t for t in tasks if t.is_complete == completed]

        if pet_name:
            tasks = [
                t for pet in self.owner.pets if pet.name == pet_name
                for t in pet.tasks
            ]

        return tasks

    def detect_conflicts(self, tasks: List[Task]):
        """Detect tasks scheduled at the same time."""
        conflicts = []
        seen = {}

        for task in tasks:
            if task.time in seen:
                conflicts.append((seen[task.time], task))
            else:
                seen[task.time] = task

        return conflicts