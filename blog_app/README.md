# Personal Blog (Flask + Filesystem)

A simple personal blog built with Flask that lets you write, edit, and delete articles.  
Content is stored as JSON files on the filesystem instead of a database, so the whole project stays lightweight and easy to understand.

Created for https://roadmap.sh/projects/personal-blog
___

## Features

- Guest (public) section:
  - Home page listing all published articles (newest first).
  - Article detail page showing full content and publication date.
- Admin section (password‑protected):
  - Dashboard listing all articles.
  - Add new article via form (title, content, publication date).
  - Edit existing article.
  - Delete article.
- File‑based storage:
  - Each article is stored as a separate JSON file in the `articles/` directory.
- No JavaScript required:
  - All pages rendered with Flask + Jinja2 templates and basic HTML/CSS.

## Tech Stack

- Python
- Flask (server + routing + templates)
- Jinja2 (HTML templating)
- HTML & CSS (frontend)
- JSON files on the filesystem for storage

## Project Structure

```text
project-root/
│
├── app.py              # Main Flask application
├── storage.py          # Helper functions for reading/writing article JSON files
├── articles/           # JSON files for each article (created at runtime)
├── templates/
│   ├── base.html       # Base layout with nav and footer
│   ├── home.html       # Home page with list of articles
│   ├── article.html    # Single article page
│   ├── dashboard.html  # Admin dashboard (list + actions)
│   ├── article_form.html  # Shared Add/Edit article form
│   └── login.html      # Admin login page
└── static/
    └── styles.css      # Minimal styling for blog, forms, and tables
