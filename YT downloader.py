import importlib
import time
import os

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

def download_youtube_media(url, output_path='.', mode='V'):
    try:
        from pytube import YouTube
        yt = YouTube(url)
        
        if mode == 'V':
            media = yt.streams.get_highest_resolution()
            media_type = 'video'
            extension = 'mp4'
        elif mode == 'A':
            media = yt.streams.filter(only_audio=True).first()
            media_type = 'audio'
            extension = 'mp3'
        else:
            print("Invalid mode. Please choose 'V' for video or 'A' for audio.")
            return
        
        print(f"Downloading {media_type}: {yt.title}")
        media_path = media.download(output_path)
        
        # Convert audio to mp3 if mode is 'A'
        if mode == 'A':
            audio_file_path = os.path.splitext(media_path)[0] + '.mp3'
            os.rename(media_path, audio_file_path)
            media_path = audio_file_path
            
        print(f"{media_type} download completed!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    try:
        import pytube
    except ImportError:
        print("pytube is not installed. Installing it...")
        install_pytube()

    while True:
        video_url = input("Enter the YouTube video URL: ")
        if video_url.lower() == 'exit':
            break
        
        mode = input("Download video (V) or audio (A)? ").upper()
        while mode not in ['V', 'A']:
            print("Invalid input. Please choose 'V' for video or 'A' for audio.")
            mode = input("Download video (V) or audio (A)? ").upper()

        download_youtube_media(video_url, mode=mode)
        
    print("Exiting the program.")

    # Wait for 5 seconds before closing
    time.sleep(5)
