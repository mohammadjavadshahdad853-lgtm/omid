OMID - راهنمای نصب

═══════ روش ۱: Railway (ساده‌ترین) ═══════
1) این فایل‌ها را در یک ریپوی GitHub خودتان بگذارید
2) railway.app -> New Project -> Deploy from GitHub repo
3) در تب Variables این متغیرها را بسازید:
   ADMIN_PASSWORD = رمز ورود پنل شما
   SECRET_KEY = یک متن تصادفی بلند
   اختیاری: TELEGRAM_BOT_TOKEN و TELEGRAM_ADMIN_IDS (ربات تلگرام)
   اختیاری: DATA_DIR = /data (ذخیره دائمی)
4) Deploy بزنید - تمام!
رمز پیش‌فرض پنل اگر ADMIN_PASSWORD ندهید: OMID

═══════ روش ۲: سرور شخصی (VPS) ═══════
docker build -t omid .
docker run -d -p 8000:8000 -e ADMIN_PASSWORD=رمزشما omid
