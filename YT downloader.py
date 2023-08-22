import importlib
import time

def install_pytube():
    try:
        importlib.import_module('pytube')
        print("pytube is already installed.")
    except ImportError:
        try:
            import pip
            pip.main(['install', 'pytube'])
            print("pytube has been successfully installed.")
        except Exception as e:
            print(f"An error occurred while installing pytube: {str(e)}")

def download_youtube_video(url, output_path='.'):
    try:
        from pytube import YouTube
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()  # You can customize the stream based on your preferences
        
        print(f"Downloading: {yt.title}")
        video_path = video.download(output_path)
        print("Download completed!")

        # Get file size
        file_size = video.filesize / (1024 * 1024)  # Convert to MB
        print(f"File saved at: {video_path}")
        print(f"File size: {file_size:.2f} MB")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    try:
        import pytube
    except ImportError:
        print("pytube is not installed. Installing it...")
        install_pytube()

    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video(video_url)

    # Wait for 5 seconds before closing
    time.sleep(5)
