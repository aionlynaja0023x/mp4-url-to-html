# YouTube Video Downloader

โปรแกรมดาวน์โหลดวิดีโอจาก YouTube ด้วย Python

## การติดตั้ง

1. ติดตั้ง Python 3.x
2. สร้าง virtual environment:
```bash
python -m venv .venv
```

3. เปิดใช้งาน virtual environment:
- Windows:
```bash
.venv\Scripts\activate
```

4. ติดตั้ง dependencies:
```bash
pip install yt-dlp
```

## การใช้งาน

1. รันโปรแกรม:
```bash
python mp4.py
```

2. ใส่ลิงค์ YouTube ที่ต้องการดาวน์โหลด
3. รอจนกว่าการดาวน์โหลดจะเสร็จสิ้น
4. ไฟล์วิดีโอจะถูกบันทึกในโฟลเดอร์ `downloads`

## คุณสมบัติ

- ดาวน์โหลดวิดีโอในคุณภาพสูงสุดที่มี (MP4)
- แสดงความคืบหน้าการดาวน์โหลด
- แสดงข้อมูลวิดีโอ (ชื่อ, ความยาว)
- จัดการข้อผิดพลาดอัตโนมัติ
