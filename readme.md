Build a Simple Task Management API

Models:

Create a Task model with the following fields:
user (forgeinkey)
title (CharField, max_length=100)
description (TextField, optional)
completed (BooleanField, default=False)
due_date (DateField, optional)
created_at (DateTimeField, auto_now_add=True)
updated_at (DateTimeField, auto_now=True)

Endpoints: Implement the following CRUD API endpoints:

List tasks: Retrieve all tasks.
Retrieve a task: Retrieve a single task by its ID.
Create a task: Add a new task.
Update a task: Edit an existing task by its ID.
Delete a task: Delete a task by its ID.

Authentication:
Use Token-based authentication to secure the API. Only authenticated users should access the endpoints.

Pagination:
Add pagination to the task listing endpoint with a page size of 10.

Validation:
Ensure that due_date is not in the past when creating or updating a task.
