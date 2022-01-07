# Repo to test out how permissions work in Django

## Internal Roles for this test project

view/add/change/delete

- Superuser can:
    - view/add/change/delete anything (no action needed)

- CEO can:
    - view Blog
    - view/add/change/delete Employees
    - view/change Students
    - view/change Users => shouldn't be able to edit permissions and superuser status!
 
 - Marketing can:
    - view/add/change/delete Blog
 
 - Program Manager can:
    - view/change Students
 
 - Business Manager can:
    - view Employees
    - view Students

If we need to give rights to anyone to edit users (maybe for first and last name), we should implement a custom 
permission that disables some fields. Else these users can give themselves superuser status or grant any permission.
[Custom User admin with disabled fields](https://realpython.com/manage-users-in-django-admin/)
[Conditionally define which fields should get shown](https://stackoverflow.com/a/60178627/10802391)
