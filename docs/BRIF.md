# "Sabr mikromoliya tashkiloti" MCHJ — veb-sayt loyihasi brifi

> Holati: **qoralama (v0.2)**. ❓ belgisi bilan belgilangan joylar tasdiqlanishi kerak.

---

## 1. Tashkilot haqida

| | |
|---|---|
| **Nomi** | "Sabr mikromoliya tashkiloti" MCHJ |
| **Faoliyati** | Mikromoliya: jismoniy shaxslarga mikroqarzlar |
| **Joylashuvi** | Samarqand shahri, bitta ofis (filiallar yo'q) |
| **Hisob dasturi** | 1C (ofisdagi ichki serverda) |
| **Domen va hosting** | `sabrmmt.uz` — mavjud |
| **Sayt tillari** | O'zbek (lotin) — asosiy, rus, ingliz |

## 2. Loyiha maqsadlari va bosqichlari

| Bosqich | Maqsad | Tarkibi |
|---|---|---|
| **1. Ommaviy sayt (MVP)** | Ishonch + mijoz jalb qilish | Bosh sahifa, biz haqimizda, litsenziya, mahsulotlar, kredit kalkulyatori, onlayn ariza, aloqa va xarita, FAQ |
| **2. Mijoz xizmatlari** | Onlayn xizmat ko'rsatish | Onlayn to'lov (Payme / Click / Uzum); keyinroq — shaxsiy kabinet (qoldiq, to'lov jadvali) va 1C bilan integratsiya |
| **3. Ichki tizim** | Hisobotlarni avtomatlashtirish | Xodimlar paneli: portfel, prosrochka, 180+ kun, bonuslar (K1/K2/K3), SMS hisobotlari |

**1-bosqichning muvaffaqiyat mezonlari (taklif):** ❓
- Oyiga N ta onlayn ariza
- Arizaga javob berish vaqti — 30 daqiqadan kam (ish vaqtida)
- Saytning telefonda yuklanish tezligi — 3 soniyadan kam

## 3. Mahsulotlar (saytda ko'rsatiladigan ma'lumot)

### 3.1. Guruh kafilligi
Takroriy mijozlar uchun limit va stavka yaxshilanib boradi.

| Qaysi marta olinmoqda | Summa | Yillik stavka | Oylik stavka |
|---|---|---|---|
| 1-marta | 2 000 000 – 7 000 000 so'm | 73,2% | 6,1% |
| 2-marta | 10 000 000 so'mgacha | 66% | 5,5% |
| 3-marta | 15 000 000 so'mgacha | 60% | 5% |

Guruh a'zolari: **3 kishidan 7 kishigacha**.

❓ Muddati?

### 3.2. Kafillik (ishsizlar uchun)
| Summa | Yillik stavka | Oylik stavka | Muddat | Talab |
|---|---|---|---|---|
| 2 000 000 – 7 000 000 so'm | 72% | 6% | 12 oygacha | 2 ta kafil + sug'urta ❓ (sug'urta xarajatini mijoz to'laydimi?) |

### 3.3. Kafillik (rasmiy ish haqi oluvchilar uchun)
| Summa | Yillik stavka | Oylik stavka | Muddat | Talab |
|---|---|---|---|---|
| 2 000 000 – 22 000 000 so'm | 60% | 5% | 24 oygacha | Qarzdor va kafilning rasmiy ish haqi bo'lishi |

### 3.4. Garov (avtotransport)
| Summa | Yillik stavka | Oylik stavka | Muddat |
|---|---|---|---|
| 2 000 000 – 50 000 000 so'm | 48% | 4% | ❓ |

Garov qoidasi: qarz summasi avtomobil baholangan qiymatining **50%** idan oshmaydi
(masalan, avtomobil 50 000 000 so'mga baholansa → 25 000 000 so'mgacha qarz). ✅ Tasdiqlangan.

Qo'shimcha xarajatlar (mijoz hisobidan): **notarius** va **sug'urta**.

### 3.5. Umumiy shartlar
- **To'lov turi: differensial** — asosiy qarz har oy teng qismda qaytariladi, foiz esa qolgan qarzga
  hisoblanadi. Shuning uchun birinchi to'lov eng katta, keyingilari kamayib boradi.
- **Yashirin to'lovlar yo'q:** komissiya va boshqa to'lovlar olinmaydi. Faqat garovli qarzda
  notarius va sug'urta xarajati bor. Bu saytda asosiy afzallik sifatida ko'rsatiladi.
- **Minimal hujjatlar** — bu ham afzallik sifatida ko'rsatiladi.
  ❓ Har bir mahsulot uchun aniq ro'yxat kerak (masalan, pasport; ish haqi mahsulotida — ish joyidan
  ma'lumotnoma; garovda — avtomobil texpasporti).
- ❓ Foiz oyma-oy hisoblanadimi yoki kunlik (oydagi kunlar soniga qarab)?

### 3.6. Kalkulyator hisob-kitobi (tekshirish uchun namuna)

Guruh kafilligi, 1-marta: **7 000 000 so'm, 12 oy, oyiga 6,1%**.

| Oy | Asosiy qarz | Foiz | Oylik to'lov | Qolgan qarz |
|---|---|---|---|---|
| 1 | 583 333 | 427 000 | 1 010 333 | 6 416 667 |
| 2 | 583 333 | 391 417 | 974 750 | 5 833 333 |
| … | … | … | … | … |
| 12 | 583 333 | 35 583 | 618 917 | 0 |
| **Jami** | **7 000 000** | **2 775 500** | **9 775 500** | |

Formula: `foiz = qolgan qarz × oylik stavka`, `asosiy qarz = summa ÷ muddat`.
❓ Shu summalar 1C'dagi to'lov jadvali bilan bir xil chiqishini tekshirib bering.

## 4. Sayt tuzilmasi (1-bosqich)

```
Bosh sahifa
│   ├─ Qisqa taklif + "Ariza qoldirish" tugmasi
│   ├─ Mahsulotlar kartochkalari (4 ta)
│   ├─ Kalkulyator
│   ├─ Nega Sabr? (afzalliklar)
│   └─ Aloqa + xarita
├── Mahsulotlar
│   ├── Guruh kafilligi
│   ├── Kafillik (ishsizlar)
│   ├── Kafillik (ish haqi)
│   └── Avtotransport garovi
├── Kredit kalkulyatori
├── Onlayn ariza
├── Biz haqimizda (tarix, rahbariyat, litsenziya, rekvizitlar)
├── Savol-javob (FAQ)
├── Yangiliklar
├── Vakansiyalar
└── Aloqa (manzil, xarita, ish vaqti, telefon, Telegram)
```

## 5. Onlayn ariza

**Maydonlar:** F.I.Sh., telefon raqami, mahsulot turi, kerakli summa, muddat, izoh,
shaxsiy ma'lumotlarni qayta ishlashga rozilik (majburiy belgi).

**Ariza qayerga boradi (bir vaqtda uchalasiga):**
1. **Telegram guruhi** — darhol xabar (bot orqali)
2. **Email** — ❓ qaysi manzilga
3. **Admin panel** — barcha arizalar ro'yxati, holati (yangi / qo'ng'iroq qilindi / rad etildi / berildi), mas'ul xodim

**Spamdan himoya:** telefon raqami formati tekshiruvi, bir raqamdan cheklangan miqdor, ko'rinmas captcha.

## 6. Brend

| Element | Qiymat (logotipdan olingan, taxminiy) |
|---|---|
| Asosiy ko'k (matn) | `#1E3399` |
| To'q ko'k (qush chizig'i) | `#0B4A8A` |
| Och ko'k (qush) | `#A6D8F2` |
| Sariq (tanga) — urg'u rangi | `#FFF200` |

Logotip fayllari: [`brand/logo-full.png`](brand/logo-full.png), [`brand/logo-icon.png`](brand/logo-icon.png).

❓ Logotipning vektor (SVG / AI / PDF) varianti bormi? Hozirgi PNG'lar saytda ishlatsa bo'ladi,
lekin sifatli ko'rinishi uchun vektor fayl kerak. Bo'lmasa, qayta chizib olamiz.

**Ohang:** ishonchli, sodda, hurmatli. Murakkab moliyaviy atamalarsiz, mijozga tushunarli tilda.

## 7. Texnik talablar

- **Mobil birinchi:** dizayn avval telefon uchun qilinadi.
- **3 til:** har bir sahifa uz / ru / en; manzillar `/uz/...`, `/ru/...`, `/en/...`.
- **Admin panel (CMS):** matnlar, stavkalar, yangiliklar va vakansiyalarni dasturchisiz o'zgartirish.
  Stavkalar **bir joyda** saqlanadi — sahifalar ham, kalkulyator ham o'sha joydan oladi.
- **Xavfsizlik:** HTTPS, admin panelga kuchli parol + ikki bosqichli kirish, muntazam zaxira nusxa.
- **Shaxsiy ma'lumotlar:** "Shaxsiy ma'lumotlar to'g'risida"gi qonunga muvofiq — ma'lumotlar
  O'zbekiston hududidagi serverda saqlanadi, maxfiylik siyosati sahifasi bo'ladi.
- **Analitika:** Google Analytics va/yoki Yandex Metrika; arizalar manbasini kuzatish.
- **SEO:** "Samarqand kredit", "mikroqarz Samarqand" kabi so'rovlar; Google Maps va Yandex Kartalarda ro'yxatdan o'tish.
- **2-bosqichga tayyorlik:** 1C bilan keyinchalik ulanish imkoniyati hisobga olinadi.

## 8. Qonuniy talablar

Barcha hujjatlar mavjud — PDF shaklida taqdim etiladi.

- Litsenziya raqami va sanasi (Markaziy bank) — saytda ko'rinarli joyda
- Yillik foiz stavkalari va barcha to'lovlarning oshkor qilinishi
- Tashkilot rekvizitlari (STIR, manzil)
- Maxfiylik siyosati va foydalanish shartlari
- Murojaatlar va shikoyatlar uchun aloqa

## 9. 1C integratsiyasi

**Qaror: hozircha integratsiya qilinmaydi.** 1C ofisdagi ichki serverda ishlaydi va internetga ochilmaydi.
Bu xavfsizlik jihatidan ham to'g'ri.

Oqibatlari:
- Sayt 1C'dan mustaqil ishlaydi: arizalar sayt bazasida saqlanadi, xodim ularni 1C'ga qo'lda kiritadi.
- Shaxsiy kabinet (qoldiq, to'lov jadvali) integratsiyasiz qilib bo'lmaydi, shuning uchun u keyinga qoldiriladi.
- Onlayn to'lovni (Payme / Click) 1C'siz ham ulash mumkin: to'lov tashkilot hisob raqamiga tushadi.
- Kelajakda kerak bo'lsa, xavfsiz variant — 1C'dan saytga **bir tomonlama** ma'lumot yuborish
  (1C internetdan to'g'ridan-to'g'ri ochilmaydi).
- ❓ 1C versiyasi va konfiguratsiyasi (kelajak uchun ma'lumot sifatida).

## 10. Hali kerak bo'lgan ma'lumotlar (nazorat ro'yxati)

- [ ] Litsenziya va yuridik hujjatlar (PDF) — va'da qilingan
- [ ] Ofis manzili, mo'ljal, ish vaqti, telefonlar, Telegram
- [ ] Guruh kafilligi va avto garovning muddatlari
- [x] To'lov turi — differensial; qo'shimcha to'lovlar — faqat garovda notarius va sug'urta
- [ ] Har bir mahsulot uchun hujjatlar ro'yxati
- [ ] Namunaviy to'lov jadvalini 1C bilan solishtirish (3.6-bo'lim)
- [ ] Arizalar uchun email va Telegram guruhi
- [ ] Logotipning vektor varianti
- [ ] Ofis, jamoa rasmlari (professional suratga olish tavsiya etiladi)
- [ ] Tashkilot tarixi, qisqa ma'lumot, raqamlar (yillar, mijozlar soni)
- [x] Domen: `sabrmmt.uz` — mavjud
- [ ] Hosting ma'lumotlari: provayder va tarif (PHP hosting / VPS)? Texnologiya tanlovi shunga bog'liq ❓
- [ ] Yoqqan 2–3 ta sayt namunasi
- [ ] Loyiha bo'yicha qaror qabul qiluvchi shaxs

## 11. Keyingi qadamlar

1. Ushbu brifdagi ❓ savollarga javob berish va brifni tasdiqlash
2. Wireframe — sahifalarning oddiy sxemasi
3. Dizayn maket (bosh sahifa + bitta mahsulot sahifasi) → tasdiqlash
4. Texnologiyani tanlash va ishlab chiqish
5. Matnlarni 3 tilga tayyorlash
6. Test, ishga tushirish, Google/Yandex'da ro'yxatdan o'tish
