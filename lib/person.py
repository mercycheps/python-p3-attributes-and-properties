#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC",
        "Production", "Legal", "Finance"
    ]

    def __init__(self, name="Jane Doe", job="Admin"):
        self._name = None
        self._job = None

        self.name = name
        if self._name is None:
            return  # Exit early if name is invalid

        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = None  # Ensure it's explicitly invalid

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in Person.approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")


