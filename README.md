# 🎮 To-Do List App - Retro Pixel Art Edition

A modern Django-based task management application with a retro 8-bit gaming aesthetic. Built for productivity with a nostalgic twist!

![Django](https://img.shields.io/badge/Django-5.2.6-green.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.2-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **🎨 Retro Pixel Art UI**: Complete 8-bit gaming aesthetic with custom fonts and styling
- **👤 User Management**: Create accounts, login/logout functionality
- **📝 Task Management**: Create, edit, delete, and mark tasks as complete
- **📅 Due Dates**: Set and track task deadlines
- **✅ Task Status**: View active and completed tasks separately
- **🎯 Responsive Design**: Works on desktop and mobile devices
- **💾 Persistent Storage**: SQLite database for data persistence

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- pip (Python package manager)
- Git (optional, for cloning)

### Installation

1. **Clone the repository** (or download ZIP)
```bash
git clone https://github.com/rubendjg/To-Do-List-app.git
cd To-Do-List-app
```

2. **Create and activate virtual environment**
```bash
# Windows
python -m venv myvenv
myvenv\Scripts\activate

# macOS/Linux
python -m venv myvenv
source myvenv/bin/activate
```

3. **Install dependencies**
```bash
pip install django==5.2.6
```

4. **Run database migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Start the development server**
```bash
python manage.py runserver
```

6. **Open your browser** and navigate to `http://127.0.0.1:8000/`

## 🎮 Usage

### Getting Started
1. **Create Account**: Click "Sign Up" to create a new user account
2. **Login**: Use your username and password to access your dashboard
3. **Create Tasks**: Click "Create New Task" to add tasks with descriptions and due dates
4. **Manage Tasks**: Use the action buttons to complete, edit, or delete tasks
5. **View Progress**: Check completed tasks in the "Completed Tasks" section

### Navigation
- **Dashboard**: View all active tasks and create new ones
- **Completed Tasks**: Review all finished tasks
- **Account Settings**: Manage your user profile (coming soon)

## 🏗️ Project Structure

```
To-Do app/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── README.md                # This file
├── myvenv/                  # Virtual environment
├── tasks_app/               # Main Django app
│   ├── models.py           # Database models (User, Task)
│   ├── views.py            # View controllers
│   ├── forms.py            # Django forms
│   ├── urls.py             # URL routing
│   ├── static/             # Static files
│   │   ├── styles/         # CSS stylesheets
│   │   │   └── main.css    # Retro pixel art styling
│   │   └── *.png           # Custom action icons
│   ├── templates/          # HTML templates
│   │   ├── base.html       # Base template
│   │   ├── user.html       # Dashboard
│   │   ├── completed.html  # Completed tasks
│   │   ├── login.html      # Login page
│   │   ├── create_user.html # Registration
│   │   ├── create_task.html # Task creation
│   │   └── modify_task.html # Task editing
│   └── migrations/         # Database migrations
└── ToDoApp/                # Django project settings
    ├── settings.py         # Project configuration
    ├── urls.py             # Main URL routing
    └── wsgi.py             # WSGI configuration
```

## 🎨 Design Features

### Retro Pixel Art Theme
- **Fonts**: Orbitron (headings) and VT323 (body text) for authentic retro feel
- **Color Scheme**: Forest green primary (`#2a4d3a`) with gold accents (`#ffb000`)
- **Background**: Subtle checkerboard pattern for retro gaming aesthetic
- **Typography**: Dark, readable fonts with pixel-perfect styling
- **Buttons**: 8-bit style with pixel borders and hover effects

### Custom Action Icons
The app includes custom PNG icons for task actions and home page:
- `Completado.png` - Mark task as complete
- `Modificar.png` - Edit task
- `Eliminar.png` - Delete task
- `Descompletado.png` - Mark task as incomplete
- `Sign up.png / Log in.png` - Respective use in home page
- `To Do.png` - Visually improving the home page

## 🔧 Technical Details

### Built With
- **Backend**: Django 5.2.6 (Python web framework)
- **Database**: SQLite (default Django database)
- **Frontend**: Bootstrap 5.3.2 + Custom CSS
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Orbitron, VT323)
- **Images**: Aseprite v1.3.15.3

### Key Components
- **Models**: User and Task models with relationships
- **Views**: Function-based views for all CRUD operations
- **Forms**: Django forms for user input validation
- **Templates**: Responsive HTML templates with template inheritance
- **Static Files**: CSS, images, and other assets

### Database Schema
```python
# User Model
class User(models.Model):
    username = CharField(max_length=25, unique=True)
    password = CharField(max_length=40)

# Task Model  
class Task(models.Model):
    name = CharField(max_length=100)
    description = CharField(max_length=100, optional)
    deadline = DateField()
    completed = BooleanField(default=False)
    user = ForeignKey(User)
```

## 🚀 Deployment

### Local Development
The app is configured for local development with Django's built-in server.

### Production Considerations
For production deployment, consider:
- Using PostgreSQL instead of SQLite
- Configuring environment variables for sensitive settings
- Setting up proper static file serving
- Implementing user authentication security measures
- Adding CSRF protection and other security headers

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Django Community** for the excellent web framework
- **Bootstrap Team** for the responsive CSS framework
- **Font Awesome** for the beautiful icons
- **Google Fonts** for the retro typography
- **Aseprite** for the great tool for creating pixel art

## 📞 Contact

**Developer**: Ruben DJG  
**Repository**: [https://github.com/rubendjg/To-Do-List-app](https://github.com/rubendjg/To-Do-List-app)

---


*Built with ❤️ and a passion for retro gaming aesthetics*

