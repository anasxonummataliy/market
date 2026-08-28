# Flask Market — Loyiha Rejasi va TODO

## Loyiha g'oyasi
Flask asosida onlayn market (marketplace) platformasi. Foydalanuvchilar mahsulot e'lon qilishi mumkin, mahsulotlar kategoriyalarga bo'linadi, admin esa barcha mahsulotlarni va ularning egasi kimligini ko'ra oladi.

## Rollar
- **User** — ro'yxatdan o'tadi, login qiladi, o'z mahsulotlarini (e'lonlarini) qo'shadi/tahrirlaydi/o'chiradi
- **Admin** — barcha foydalanuvchilar va barcha mahsulotlarni ko'radi, har bir mahsulotning egasini ko'ra oladi, kerak bo'lsa mahsulot/foydalanuvchini bloklashi yoki o'chirishi mumkin

---

## 1. Modellar (Database Models)

### User
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    products = db.relationship('Product', backref='owner', lazy=True)
```

### Category
```python
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)

    products = db.relationship('Product', backref='category', lazy=True)
```

### Product
```python
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    is_approved = db.Column(db.Boolean, default=True)   # admin tasdiqlashi kerak bo'lsa
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
```

**Munosabatlar (relationships):**
- User → Product: one-to-many (bitta user ko'p mahsulot qo'shishi mumkin)
- Category → Product: one-to-many (bitta kategoriyada ko'p mahsulot bo'ladi)
- Har bir Product albatta bitta `user_id` va bitta `category_id` ga bog'langan

### Cart
```python
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)

    items = db.relationship('CartItem', backref='cart', lazy=True, cascade='all, delete-orphan')
```

### CartItem
```python
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1, nullable=False)

    product = db.relationship('Product')
```

**Cart munosabatlari:**
- User → Cart: one-to-one (har bir userda bitta cart bo'ladi)
- Cart → CartItem: one-to-many (cartda bir nechta mahsulot turi bo'lishi mumkin)
- CartItem → Product: many-to-one (qaysi mahsulot va nechta dona)

---

## 2. TODO — Bosqichma-bosqich

### Bosqich 1: Loyihani sozlash
- [ ] Virtual environment yaratish (`python -m venv venv`)
- [ ] Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF o'rnatish
- [ ] Loyiha strukturasini tuzish (`app/`, `templates/`, `static/`, `config.py`, `run.py`)
- [ ] `.env` va `config.py` orqali sozlamalarni ajratish (SECRET_KEY, DATABASE_URI)
- [ ] SQLite (dev) yoki PostgreSQL (prod) uchun DB ulanishini sozlash

### Bosqich 2: Modellarni yaratish
- [ ] `User`, `Category`, `Product` modellarini yozish
- [ ] `flask db init`, `migrate`, `upgrade` orqali migratsiya qilish
- [ ] Boshlang'ich kategoriyalarni DB ga qo'shish (seed data)

### Bosqich 3: Autentifikatsiya (auth)
- [ ] Ro'yxatdan o'tish (register) formasi va route
- [ ] Login/logout (Flask-Login orqali)
- [ ] Parolni hash qilish (`werkzeug.security`)
- [ ] `login_required` decorator bilan himoyalangan sahifalar
- [ ] Admin uchun alohida `admin_required` decorator (`current_user.is_admin` tekshiruvi)

### Bosqich 4: User funksiyalari
- [ ] Mahsulot qo'shish formasi (title, description, price, category, image)
- [ ] Foydalanuvchining o'z mahsulotlarini ko'rish sahifasi ("Mening e'lonlarim")
- [ ] Mahsulotni tahrirlash va o'chirish (faqat o'ziniki bo'lsa)
- [ ] Profilni tahrirlash (email, parol o'zgartirish)

### Bosqich 5: Umumiy market sahifalari
- [ ] Bosh sahifa — barcha mahsulotlar ro'yxati (pagination bilan)
- [ ] Kategoriya bo'yicha filtrlash
- [ ] Mahsulot qidiruvi (search by title)
- [ ] Bitta mahsulot detali sahifasi (product detail page)

### Bosqich 6: Admin panel
- [ ] Admin uchun alohida `/admin` blueprint yaratish
- [ ] Barcha mahsulotlar ro'yxati (kim joylaganini — user — ko'rsatuvchi ustun bilan)
- [ ] Barcha foydalanuvchilar ro'yxati
- [ ] Mahsulotni o'chirish/tasdiqlash imkoniyati
- [ ] Foydalanuvchini bloklash/faolsizlantirish (`is_active`)

### Bosqich 7: Frontend (template)
- [ ] `base.html` — umumiy layout (navbar, footer)
- [ ] Bootstrap yoki Tailwind ulash
- [ ] Har bir sahifa uchun template: home, product_detail, add_product, admin_dashboard, login, register

### Bosqich 8: Savatcha (Cart)
- [ ] `Cart` va `CartItem` modellarini yaratish, migratsiya qilish
- [ ] User ro'yxatdan o'tganda avtomatik bo'sh cart yaratish (yoki birinchi "add to cart"da)
- [ ] "Add to cart" route (mahsulot detail sahifasidan)
- [ ] Cart sahifasi — mahsulotlar, miqdori, umumiy narx
- [ ] Miqdorni o'zgartirish / mahsulotni cartdan o'chirish
- [ ] Navbar'da cart icon + ichidagi mahsulotlar soni

### Bosqich 9: Xavfsizlik va tozalash
- [ ] Formalarni `Flask-WTF` + CSRF himoyasi bilan yozish
- [ ] Fayl yuklashda (rasm) ruxsat etilgan formatlarni tekshirish
- [ ] Xatoliklarni qayta ishlash (404, 403, 500 sahifalari)

### Bosqich 10: Test va joylashtirish (deploy)
- [ ] Asosiy funksiyalarni qo'lda test qilish (register → login → mahsulot qo'shish → admin ko'rish)
- [ ] `requirements.txt` yaratish
- [ ] Deploy qilish (Render, PythonAnywhere yoki VPS)

---

## Keyingi qadam
Birinchi navbatda **Bosqich 1 va 2** ni bajarish tavsiya etiladi — loyiha skeletoni va modellarsiz keyingi qadamlarni qilib bo'lmaydi. Cart (Bosqich 8) qasddan Order/checkout'dan oldin va asosiy market funksiyalaridan keyin qo'yilgan — shu tartibda borilsa loyiha bosqichma-bosqich, murakkablashib ketmasdan o'sadi.
