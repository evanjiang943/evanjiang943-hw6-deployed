# Prototype 4: Django Full-Stack with SQLite (SUCCESS CASE)

## Design Dimensions Tested
- **Tech Stack**: Django (full-stack Python framework)
- **UI Style**: Clean, professional custom CSS (no heavy libraries)
- **Data Storage**: SQLite database with proper models and relationships
- **Architecture**: MVC (Model-View-Controller) pattern
- **Deployment**: Production-ready structure

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Create database and run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional, for admin access)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

Visit http://localhost:8000

## Features

**Complete CRUD Operations**
- Create assignments with full validation
- List all assignments with metadata
- View detailed assignment pages
- Proper database persistence

**Database Models**
- `Assignment` model with all fields
- `RubricCriterion` model for structured rubrics
- Foreign key relationships
- JSON field for AI-generated data

**AI Rubric Generation**
- Mock AI generation with realistic delay
- Structured rubric criteria (name, points, description, grading notes)
- Confidence scores
- Automatic criterion creation in database

**Admin Interface**
- Built-in Django admin
- Inline rubric editing
- Search and filtering
- Access at http://localhost:8000/admin

**Professional UI**
- Clean, modern design
- Responsive layout
- Loading states
- Form validation
- Success/error messages

**File Handling**
- Proper file upload with media storage
- Support for multiple file types
- Secure file serving in development

## Why This One Works Best

**Everything in one place.** Django handles frontend, backend, and database in a single framework. No coordinating between React and Flask, no CORS issues, no wondering which server died. Just one `python manage.py runserver` and you're good.

**Real data persistence.** Unlike the other prototypes, this one actually saves your assignments to a SQLite database. Close the browser, restart the server, data's still there. For production, you'd swap SQLite for PostgreSQL, but the code stays the same.

**Built-in admin interface.** This is honestly the killer feature. Run `python manage.py createsuperuser` and you get a full admin panel where TAs can view, edit, and manage assignments without any custom UI work. That alone saves weeks of development time.

**Fast to build.** Django's scaffolding gives you models, forms, authentication, CSRF protection, and file uploads out of the box. I built this prototype in about the same time as the Node/Express one, but got way more functionality.

**Production-ready patterns.** Security is handled (CSRF tokens, XSS protection), file uploads are safe, the ORM prevents SQL injection. Django's been around forever and has patterns for everything you'd need.

**Easy deployment.** Railway, Render, and PythonAnywhere all have one-click Django deployment. Add a `requirements.txt` and a `Procfile` and you're done.

## Trade-offs

**Pros:**
- Complete solution in one framework
- Excellent documentation and community
- Built-in admin interface
- ORM abstracts database complexity
- Template system prevents XSS vulnerabilities
- Middleware for authentication, CSRF, etc.
- Easy deployment to multiple platforms

**Cons:**
- Heavier than micro-frameworks (Flask)
- Python/Django learning curve
- Server-side rendering may feel less "snappy" than React
- Larger memory footprint than Node

## Quick Comparison

| Feature | React+Flask | Node/Express | Chat UI | Django |
|---------|-------------|--------------|---------|--------|
| Setup | Complex (2 servers) | Medium | Easy (no server) | Medium |
| Database | None | None | None | SQLite |
| Admin Panel | No | No | No | Yes |
| Deployment | Hard | Medium | Easy | Easy |
| Maintainability | Medium | Medium | Low | High |

## If I Were Deploying This

Best hosting options:
1. **Railway** - Auto-detects Django, one-click deploy
2. **Render** - Free tier with persistent storage
3. **PythonAnywhere** - Good for academic projects

All of them support SQLite for prototypes and make it easy to upgrade to PostgreSQL later.

## What I'd Add for Production

- User authentication (Django has it built-in)
- Real OpenAI/Anthropic API for rubric generation
- Edit rubric after AI generates it
- File type validation
- Export to PDF/JSON
- Canvas/Gradescope integration

## Bottom Line

If I had to pick one prototype to actually deploy and maintain, this is it. The admin interface alone makes it worth it - TAs can manage everything without me building a custom UI. Plus the database means assignments persist across semesters, which is kind of essential for a real tool.

