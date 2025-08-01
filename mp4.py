import yt_dlp
import os

def download_youtube_video(url, output_path='downloads'):
    try:
        # Create download folder if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Define download options
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Prefer MP4, fallback to best available
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # File name format
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
        
        print(f"\nDownload complete! File saved to: {output_path}")
        
    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        print("Please check if the URL is valid and accessible")

if __name__ == "__main__":
    video_url = input("Enter YouTube URL: ")
    download_youtube_video(video_url)