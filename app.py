from flask import Flask, render_template, request, jsonify
import yt_dlp
import os
from threading import Thread

app = Flask(__name__)

def download_youtube_video(url, output_path='downloads'):
    try:
        # สร้างโฟลเดอร์สำหรับเก็บไฟล์ที่ดาวน์โหลด
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # กำหนดตัวเลือกสำหรับการดาวน์โหลด
        ydl_opts = {
            'format': 'best[ext=mp4]',  # เลือกคุณภาพวิดีโอที่ดีที่สุดในรูปแบบ MP4
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # รูปแบบชื่อไฟล์
        }

        # ดาวน์โหลดวิดีโอ
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # ดึงข้อมูลวิดีโอ
            info = ydl.extract_info(url, download=True)
            
            return {
                'success': True,
                'message': f'ดาวน์โหลดเสร็จสิ้น: {info["title"]}'
            }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({
            'success': False,
            'error': 'กรุณาใส่ URL'
        })

    # เริ่มดาวน์โหลดในเธรดแยก
    result = download_youtube_video(url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
