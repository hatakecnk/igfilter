# IG Follower Filter 🕵️‍♂️

Script Python interaktif untuk memfilter akun Instagram yang:
- ❌ Tidak follow kamu balik
- 🟢 Kamu tidak follow balik

hasil disimpan otomatis, dan support input dari file HTML/JSON/MIX Instagram.

---

## ✨ Fitur

- ✅ Dukungan file `followers_1.html` / `.json` dan `following.html` / `.json`
- ✅ Interaktif di terminal (menu pilihan)
- ✅ Tampilan berwarna (pakai `colorama`)
- ✅ Hasil disimpan ke `.txt`
- ✅ Kompatibel dengan WSL / Linux / Windows
- ✅ Banner keren dan ringan dijalankan

---

## 🧰 Cara Pakai

1. **Download data followers & following dari Instagram**
   - File yang dibutuhkan: `followers_1.html` dan `following.html` (atau versi `.json`)

2. **Install dependencies (hanya sekali)**

```bash
pip install -r requirements.txt
```

3. **Jalankan Script**
```bash
python igfilter.py
```

| File                       | Isi                               |
| -------------------------- | --------------------------------- |
| `not_following_back.txt`   | Akun yang tidak follow kamu balik |
| `you_dont_follow_back.txt` | Akun yang kamu belum follow balik |

👨‍💻 Author Febry Afriansyah
📧 Email: febryafriansyah@programmer.net
🌐 GitHub: @hatakecnk