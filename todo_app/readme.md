# Todo App

A simple **Todo App** built with Django, designed to manage and organize daily tasks effectively. This app allows users to create, update, and delete tasks, helping to keep track of their to-do lists.

## Features

- Create tasks with title and description
- Mark tasks as completed
- Delete tasks
- View tasks by their completion status (all, completed, pending)
- Drag and Drop Sorting
- Store tasks in a SQLite database (default)

## Technologies Used

- **Django** - Web framework for building the app
- **SQLite** - Database for storing tasks
- **HTML/CSS** - Frontend for task display
- **JavaScript** - For any dynamic behavior (e.g., task completion toggle, darg and drop sorting)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/dibyansu06/django-project-archive.git
   cd django-project-archive/todo_app
   ```
## Run the Development Server
  ```bash
  python manage.py runserver
  ```

The app should now be running at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Usage

1. Open the app in your browser.
2. Add tasks by entering a title and description.
3. Mark tasks as complete by clicking on the checkbox next to them.
4. Delete tasks by clicking the delete button next to each task.

## Future Improvements

- Add user authentication (registration/login/logout)
- Implement task due dates and reminders
- Add task categories
- Implement task search/filter functionality

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or fixes.

## License

This project is open-source and available under the MIT License.
