# Flask Market — Loyiha Rejasi va TODO

## Loyiha g'oyasi
Flask asosida onlayn market (marketplace) platformasi. Foydalanuvchilar mahsulot e'lon qilishi mumkin, mahsulotlar kategoriyalarga bo'linadi, admin esa barcha mahsulotlarni va ularning egasi kimligini ko'ra oladi.

## Rollar
- **User** — ro'yxatdan o'tadi, login qiladi, o'z mahsulotlarini (e'lonlarini) qo'shadi/tahrirlaydi/o'chiradi
- **Admin** — barcha foydalanuvchilar va barcha mahsulotlarni ko'radi, har bir mahsulotning egasini ko'ra oladi, kerak bo'lsa mahsulot/foydalanuvchini bloklashi yoki o'chirishi mumkin

---

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
