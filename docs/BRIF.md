# "Sabr mikromoliya tashkiloti" MCHJ — veb-sayt loyihasi brifi

> Holati: **qoralama (v0.1)**. ❓ belgisi bilan belgilangan joylar tasdiqlanishi kerak.

---

## 1. Tashkilot haqida

| | |
|---|---|
| **Nomi** | "Sabr mikromoliya tashkiloti" MCHJ |
| **Faoliyati** | Mikromoliya: jismoniy shaxslarga mikroqarzlar |
| **Joylashuvi** | Samarqand shahri, bitta ofis (filiallar yo'q) |
| **Hisob dasturi** | 1C |
| **Sayt tillari** | O'zbek (lotin) — asosiy, rus, ingliz |

## 2. Loyiha maqsadlari va bosqichlari

| Bosqich | Maqsad | Tarkibi |
|---|---|---|
| **1. Ommaviy sayt (MVP)** | Ishonch + mijoz jalb qilish | Bosh sahifa, biz haqimizda, litsenziya, mahsulotlar, kredit kalkulyatori, onlayn ariza, aloqa va xarita, FAQ |
| **2. Mijoz xizmatlari** | Onlayn xizmat ko'rsatish | Shaxsiy kabinet (qoldiq, to'lov jadvali), onlayn to'lov (Payme / Click / Uzum), 1C bilan integratsiya |
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

❓ Muddati? Guruhda nechta a'zo bo'ladi?

### 3.2. Kafillik (ishsizlar uchun)
| Summa | Yillik stavka | Oylik stavka | Muddat | Talab |
|---|---|---|---|---|
| 2 000 000 – 7 000 000 so'm | 72% | 6% | 12 oygacha | 2 ta kafil + sug'urta |

### 3.3. Kafillik (rasmiy ish haqi oluvchilar uchun)
| Summa | Yillik stavka | Oylik stavka | Muddat | Talab |
|---|---|---|---|---|
| 2 000 000 – 22 000 000 so'm | 60% | 5% | 24 oygacha | Qarzdor va kafilning rasmiy ish haqi bo'lishi |

### 3.4. Garov (avtotransport)
| Summa | Yillik stavka | Oylik stavka | Muddat |
|---|---|---|---|
| 2 000 000 – 50 000 000 so'm | 48% | 4% | ❓ |

Garov qoidasi: qarz summasi avtomobil baholangan qiymatining **50%** idan oshmaydi
(masalan, avtomobil 50 000 000 so'mga baholansa → 25 000 000 so'mgacha qarz). ❓ Shunday tushundikmi?

### 3.5. Kalkulyator uchun aniqlashtirish kerak
- ❓ To'lov turi: **annuitet** (har oy teng to'lov) yoki **differensial** (asosiy qarz teng, foiz qoldiqqa)?
- ❓ Qo'shimcha to'lovlar bormi (komissiya, sug'urta summasi)? Mijozga **to'liq qiymat** ko'rsatilishi kerak.
- ❓ Kerakli hujjatlar ro'yxati (pasport, ish joyidan ma'lumotnoma, avtomobil texpasporti va h.k.).

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

## 8. Qonuniy talablar (yurist bilan tasdiqlanadi) ❓

- Litsenziya raqami va sanasi (Markaziy bank) — saytda ko'rinarli joyda
- Yillik foiz stavkalari va barcha to'lovlarning oshkor qilinishi
- Tashkilot rekvizitlari (STIR, manzil)
- Maxfiylik siyosati va foydalanish shartlari
- Murojaatlar va shikoyatlar uchun aloqa

## 9. 1C integratsiyasi (2-bosqich uchun ma'lumot yig'ish)

- ❓ 1C versiyasi va konfiguratsiyasi (masalan, 1C:Предприятие 8.3, qaysi konfiguratsiya)?
- ❓ 1C kim tomonidan qo'llab-quvvatlanadi (ichki xodim yoki tashqi kompaniya)?
- ❓ 1C'da HTTP-servis / OData yoqish imkoni bormi?
- Maqsad: mijoz o'z qoldig'i va to'lov jadvalini ko'radi; to'lovlar 1C'ga avtomatik tushadi.

## 10. Hali kerak bo'lgan ma'lumotlar (nazorat ro'yxati)

- [ ] Litsenziya raqami, sanasi, STIR, yuridik manzil
- [ ] Ofis manzili, mo'ljal, ish vaqti, telefonlar, Telegram
- [ ] Guruh kafilligi va avto garovning muddatlari
- [ ] To'lov turi (annuitet / differensial) va qo'shimcha to'lovlar
- [ ] Har bir mahsulot uchun hujjatlar ro'yxati
- [ ] Arizalar uchun email va Telegram guruhi
- [ ] Logotipning vektor varianti
- [ ] Ofis, jamoa rasmlari (professional suratga olish tavsiya etiladi)
- [ ] Tashkilot tarixi, qisqa ma'lumot, raqamlar (yillar, mijozlar soni)
- [ ] Domen (masalan, `sabr.uz` bandmi?) ❓
- [ ] Yoqqan 2–3 ta sayt namunasi
- [ ] Loyiha bo'yicha qaror qabul qiluvchi shaxs

## 11. Keyingi qadamlar

1. Ushbu brifdagi ❓ savollarga javob berish va brifni tasdiqlash
2. Wireframe — sahifalarning oddiy sxemasi
3. Dizayn maket (bosh sahifa + bitta mahsulot sahifasi) → tasdiqlash
4. Texnologiyani tanlash va ishlab chiqish
5. Matnlarni 3 tilga tayyorlash
6. Test, ishga tushirish, Google/Yandex'da ro'yxatdan o'tish
