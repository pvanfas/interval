# Pre-Deployment Checklist

## Critical Steps Before First Deployment

### 1. Create Logs Directory
**REQUIRED** - Django will fail to start without this directory.

```bash
# On production server, run as deployment user
cd /home/srv/interval/intervaledu/intervaledu
mkdir -p logs
chmod 755 logs
```

If using systemd/supervisor, ensure the process user has write permissions:
```bash
# If running as 'www-data' or similar
chown www-data:www-data logs
```

### 2. Set Production SECRET_KEY
Generate a strong secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Add to `.env`:
```
SECRET_KEY=<generated-key-from-above>
```

### 3. Environment Variables
Verify `.env` contains:
```
DEBUG=False
SECRET_KEY=<your-strong-secret-key>
ALLOWED_HOSTS=intervaledu.com,www.intervaledu.com
CSRF_TRUSTED_ORIGINS=https://intervaledu.com,https://www.intervaledu.com
USE_PROXY_SSL_HEADER=true
SECURE_SSL_REDIRECT=true
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=true
SECURE_HSTS_PRELOAD=true
DATABASE_URL=<your-database-url>
```

### 4. Database Setup
```bash
python manage.py migrate
python manage.py createcachetable
```

### 5. Static Files
```bash
python manage.py collectstatic --noinput
```

### 6. Test Configuration
```bash
python manage.py check --deploy
```

Should show minimal warnings (SECRET_KEY warning will clear after step 2).

### 7. File Permissions
Ensure proper ownership for all directories:
```bash
# Adjust user:group to match your web server process
chown -R www-data:www-data /path/to/project
chmod -R 755 /path/to/project
chmod 755 logs  # Ensure logs directory is writable
chmod 644 db.sqlite3  # If using SQLite
```

## Common Deployment Issues

### Logging Handler Error
**Symptom**: `ValueError: Unable to configure handler 'file'`

**Solution**: Ensure `logs/` directory exists with proper permissions (see step 1).

### Static Files 404
**Symptom**: CSS/JS not loading

**Solutions**:
1. Run `collectstatic` (step 5)
2. Configure Apache/Nginx to serve `/static/` from the correct path
3. Verify `STATIC_ROOT` points to collected files

### Internal Server Error (DEBUG=False)
**Symptom**: Generic 500 error page

**Solutions**:
1. Check logs: `tail -f logs/django.log`
2. Verify `ALLOWED_HOSTS` includes your domain
3. Ensure `CSRF_TRUSTED_ORIGINS` includes https:// scheme
4. Check Apache error logs: `/var/log/apache/error.log`

## Deployment Order
1. ✅ Create logs directory with permissions
2. ✅ Set SECRET_KEY in .env
3. ✅ Configure all environment variables
4. ✅ Run migrations and createcachetable
5. ✅ Collect static files
6. ✅ Run deployment checks
7. ✅ Set file permissions
8. 🚀 Start application server (Gunicorn/uWSGI)
9. 🚀 Start/reload Apache
10. ✅ Monitor logs for errors
