import yt_dlp
import os
import random
import string

def generate_random_filename(length=8):
    """Generate a random filename of 6-10 characters."""
    length = random.randint(6, 10)  # Random length between 6 and 10
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return ''.join(random.choice(characters) for _ in range(length))

def get_unique_filename(output_path, base_name, extension='mp4'):
    """Generate a unique filename by appending a version number if needed."""
    file_path = os.path.join(output_path, f"{base_name}.{extension}")
    version = 1
    while os.path.exists(file_path):
        file_path = os.path.join(output_path, f"{base_name}v{version}.{extension}")
        version += 1
    return file_path

def download_youtube_video(url, output_path='downloads'):
    try:
        # Create download folder if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Generate random filename
        random_name = generate_random_filename()

        # Get unique filename with version number if needed
        unique_filename = get_unique_filename(output_path, random_name, 'mp4')
        filename_template = unique_filename.replace(f'.mp4', '')

        # Define download options
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': f'{filename_template}.%(ext)s',  # Use random filename
            'progress_hooks': [lambda d: print(f"\rDownloading: {d['_percent_str']}", end="")
                             if d['status'] == 'downloading' else None],
        }

        print("Starting download...")

        # Download video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video info
            info = ydl.extract_info(url, download=False)
            
            # Display video info
            print(f"\nVideo title: {info['title']}")
            print(f"Duration: {info['duration']} seconds")
            
            # Download video
            ydl.download([url])
        
        print(f"\nดาวน์โหลดสำเร็จ!!: {unique_filename}")
        
    except Exception as e:
        print(f"\nเกิดข้อผิดพลาด: {str(e)}")
        print("กรุณาตรวจสอบว่า URL ถูกต้องและเข้าถึงได้")

if __name__ == "__main__":
    video_url = input("กรุณาใส่ URL ของ YouTube: ")
    download_youtube_video(video_url)