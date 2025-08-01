from flask import Flask, render_template, request, jsonify
import yt_dlp

app = Flask(__name__)

def get_youtube_video_url(url):
    try:
        # Define basic options
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Prefer MP4, fallback to best
            'get_url': True,  # Extract direct URL
        }

        # Extract video info with yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
            if formats:
                # Filter formats with both video and audio
                video_formats = [f for f in formats if f.get('vcodec') != 'none' and f.get('acodec') != 'none']
                if video_formats:
                    # Select format with highest resolution and bitrate
                    best_format = max(video_formats, key=lambda f: (f.get('height', 0), f.get('tbr', 0)))
                    video_url = best_format.get('url')
                    video_title = info.get('title')
                    return {
                        'success': True,
                        'video_url': video_url,
                        'title': video_title
                    }
                else:
                    raise Exception("No video formats with audio available")
            else:
                raise Exception("No downloadable formats available")
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
            'error': 'Please provide a URL'
        })
    result = get_youtube_video_url(url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)