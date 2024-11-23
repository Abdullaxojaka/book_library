# Kutubxona boshqaruv tizimi

## Loyihaning asosiy vazifalari
- Kitoblarni qo‘shish, o‘chirish va tahrirlash.
- Foydalanuvchilarni ro‘yxatdan o‘tkazish va boshqarish.
- Kitoblarni vaqtinchalik berish va qaytarib olish.

## API Endpoint'lar
- `GET /api/books/` - Kitoblar ro‘yxati.
- `POST /api/borrow/` - Kitobni olish.
- `POST /api/borrow/<id>/return/` - Kitobni qaytarish.

## Ishlatish bo‘yicha yo‘riqnoma
1. Django loyihasini yuklang.
2. Django migratsiyalarini bajaring:
   ```bash
   python manage.py makemigrations
   python manage.py migrate


```bash
pip install -r requirements/development.txt
```

```bash
pre-commit install && pre-commit autoupdate
```
