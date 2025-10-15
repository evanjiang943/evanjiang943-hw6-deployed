# Deploying to Railway

## Quick Deploy

1. **Install Railway CLI:**
   ```bash
   brew install railway
   ```

2. **Login to Railway:**
   ```bash
   railway login
   ```

3. **Initialize and deploy:**
   ```bash
   cd prototypes/p4-django-success
   railway init
   railway up
   ```

4. **Add PostgreSQL database:**
   ```bash
   railway add -p postgresql
   ```

5. **Set environment variables:**
   ```bash
   railway variables set SECRET_KEY="your-secret-key-here"
   railway variables set DEBUG="False"
   ```

6. **Open your deployed app:**
   ```bash
   railway open
   ```

## Environment Variables

Railway will automatically set:
- `DATABASE_URL` (from PostgreSQL addon)
- `PORT` (for the web service)

You should set:
- `SECRET_KEY` - Generate with: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
- `DEBUG` - Set to "False" for production

## What's Configured

- ✓ Gunicorn for production server
- ✓ WhiteNoise for static file serving
- ✓ PostgreSQL support (via dj-database-url)
- ✓ SQLite fallback for local development
- ✓ Automatic migrations on deploy
- ✓ Static files collection

## Deployment Process

Railway will:
1. Detect Python app
2. Install dependencies from requirements.txt
3. Run migrations automatically
4. Collect static files
5. Start gunicorn server
6. Provide a public URL

## Local Testing

Test the production setup locally:
```bash
source venv/bin/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput
gunicorn assignment_creator.wsgi
```

Visit http://localhost:8000

## Troubleshooting

**Check logs:**
```bash
railway logs
```

**Run migrations manually:**
```bash
railway run python manage.py migrate
```

**Create superuser:**
```bash
railway run python manage.py createsuperuser
```

## Alternative: Render

If you prefer Render:
1. Go to render.com
2. New → Web Service
3. Connect GitHub repo
4. Root Directory: `prototypes/p4-django-success`
5. Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
6. Start Command: `gunicorn assignment_creator.wsgi`
7. Add environment variables (SECRET_KEY, DEBUG=False)
8. Create PostgreSQL database and link it

