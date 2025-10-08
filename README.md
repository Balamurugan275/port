# MyPortfolio

This is a small Django portfolio project. It includes two apps:

- `portfolio` — simple pages (home/about/projects/contact)
- `accounts` — authentication/profile (used for dashboard)

Run locally

```powershell
& .\venv\Scripts\Activate.ps1
python manage.py runserver
```

Notes

- The project expects static files under `portfolio/static/` and templates in `templates/`.
- Database is configured for MySQL in `myportfolio/settings.py`. For quick local testing, switch to sqlite3 in `DATABASES`.
