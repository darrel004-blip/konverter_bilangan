NUMBER CONVERTER - FLASK + VERCEL

ISI PROJECT (SEMUA FILE HARUS ADA DI ROOT REPOSITORY)
- main.py                    Flask app; mengekspor objek `app`
- process.py                 class konversi asli (disalin tanpa perubahan)
- konverter_bilangan.html    interface satu file (CSS + JavaScript terintegrasi)
- requirements.txt           dependency Flask

DEPLOY KE VERCEL
1. Extract ZIP ini.
2. Upload ISI folder ini ke ROOT GitHub repository, bukan folder luarnya.
   Di root repository harus langsung terlihat main.py, process.py,
   konverter_bilangan.html, dan requirements.txt.
3. Import repository di Vercel.
4. Gunakan Root Directory yang berisi main.py.
5. Jangan isi Start Command `python main.py`; Vercel mengimpor objek Flask `app`.
6. Vercel akan memasang Flask dari requirements.txt dan mendeteksi main.py.

JALANKAN LOKAL DI WINDOWS
1. Buka terminal pada folder yang berisi keempat file.
2. Jalankan:
   py -m venv .venv
   .venv\\Scripts\\activate
   py -m pip install -r requirements.txt
   py main.py
3. Buka http://127.0.0.1:8000

CATATAN
- `process.py` disalin dari file yang diberikan dan tidak dimodifikasi.
- HTML memanggil API dengan URL relatif `/api/convert`.
- `main(8).py` yang lama masih merupakan server http.server. Gunakan main.py
  dari paket ini sebagai pengganti; jangan upload keduanya dengan nama berbeda.
