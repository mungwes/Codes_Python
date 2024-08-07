# Please install; pytube library in order to be able to use the modules
# TouTube and Playlist
# !pip install pytube
from pytube import YouTube, Playlist
import os

class Download:
    """
    This program allows you to download YouTube videos or playlists 
    and convert them to MP3 files. When downloading a playlist, ensure 
    that the URL is accurate by copying it from the "share" tab.

    Please provide the output path. If the specified path exists, the 
    program won't create a new folder. However, if the path doesn't exist, 
    a folder with the name from the output path will be created.

    Written by: S'yanda Mungwe.
    """

    @staticmethod
    def download_video(video_url, output_path):
        """
        The method downloads one video from YouTube of a given url.
        """
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        yt= YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()
        try:
            video_stream.download(output_path=output_path)
            print(f"Downloaded: {yt.title}")
        except Exception as e:
            print(f"Error downloading {yt.title}: {str(e)}")
        print("Done!")
            
    @staticmethod
    def download_video_as_mp3(video_url, output_path):
        """
        The method downloads one video from YouTube of a given url and 
        converts it to an mp3 file. 
        """
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        try:
            yt = YouTube(video_url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(output_path=output_path)

            # Rename the downloaded file to have a .mp3 extension
            original_filename = audio_stream.default_filename
            mp3_filename = os.path.join(output_path, f"{yt.title}.mp3")
            os.rename(os.path.join(output_path, original_filename), mp3_filename)
            print(f"Video downloaded as MP3: {mp3_filename}")
        except Exception as e:
            print(f"Error downloading {yt.title}: {str(e)}")
        print("Done!")

    @staticmethod
    def download_playlist_videos(playlist_url, output_path):
        """
        The method downloads a playlist (of videos) from YouTube of a 
        given url.
        """
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        playlist = Playlist(playlist_url)
        # Iterate through the videos in the playlist and download each one
        for video_url in playlist.video_urls:
            try:
                yt = YouTube(video_url)
                video_stream = yt.streams.get_highest_resolution()
                video_stream.download(output_path=output_path)
                print(f"Downloaded: {yt.title}")
            except Exception as e:
                print(f"Error downloading {yt.title}: {str(e)}")
        print("Done!")

    @staticmethod
    def download_playlist_as_mp3(playlist_url, output_path):
        """
        The method downloads a playlist (of videos) from YouTube of a 
        given url and converts them to mp3 files.
        """
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        playlist = Playlist(playlist_url)
        for video_url in playlist.video_urls:
            try:
                yt = YouTube(video_url)
                audio_stream = yt.streams.filter(only_audio=True).first()
                audio_stream.download(output_path=output_path)

                # Rename the downloaded file to have a .mp3 extension
                original_filename = audio_stream.default_filename
                mp3_filename = os.path.join(output_path, f"{yt.title}.mp3")
                os.rename(os.path.join(output_path, original_filename), mp3_filename)

                print(f"Video downloaded as MP3: {mp3_filename}")
            except Exception as e:
                print(f"Error downloading {yt.title}: {str(e)}")
        print("Done!")
        

download = Download()
path = "F:/Quantum Computation and Information"
link = "https://youtube.com/playlist?list=PLqLyTdPNhQZwfLoL4QMeI6scnyH1c__tE&si=Odme8JWz0UJ84r-q"

# Choose the appropriate method based on your download needs
download.download_playlist(link, path)