import yt_dlp
import os

def download_youtube_video(url, output_path='downloads'):
    try:
        # สร้างโฟลเดอร์สำหรับเก็บไฟล์ที่ดาวน์โหลด
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # กำหนดตัวเลือกสำหรับการดาวน์โหลด
        ydl_opts = {
            'format': 'best[ext=mp4]',  # เลือกคุณภาพวิดีโอที่ดีที่สุดในรูปแบบ MP4
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # รูปแบบชื่อไฟล์
            'progress_hooks': [lambda d: print(f"\rกำลังดาวน์โหลด: {d['_percent_str']}", end="")
                             if d['status'] == 'downloading' else None],
        }

        print("กำลังเริ่มดาวน์โหลด...")
        
        # ดาวน์โหลดวิดีโอ
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # ดึงข้อมูลวิดีโอ
            info = ydl.extract_info(url, download=False)
            
            # แสดงข้อมูลวิดีโอ
            print(f"\nชื่อวิดีโอ: {info['title']}")
            print(f"ความยาว: {info['duration']} วินาที")
            
            # ดาวน์โหลดวิดีโอ
            ydl.download([url])
        
        print(f"\nดาวน์โหลดเสร็จสิ้น! ไฟล์ถูกบันทึกที่: {output_path}")
        
    except Exception as e:
        print(f"\nเกิดข้อผิดพลาด: {str(e)}")
        print("กรุณาตรวจสอบว่า URL ถูกต้องและสามารถเข้าถึงได้")

if __name__ == "__main__":
    # ตัวอย่างการใช้งาน
    video_url = input("กรุณาใส่ลิงค์ YouTube: ")
    download_youtube_video(video_url)
