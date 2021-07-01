"""A video player class."""
import random

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""
    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        the_videos = self._video_library.get_all_videos()
        the_videos.sort(key=lambda x: x.title)  # sorts
        print("Here's a list of all available videos:")
        for x in the_videos:
            print(f'{x.title} ({x.video_id}) [{" ".join(x.tags)}]')

    isPlay = False
    global current
    global currentids
    isPlaying = False
    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """
        # need to make a bool that will determine if vid is playing or not
        videoidgot = self._video_library.get_video(video_id)
        self.currentids = videoidgot

        # need to do exception handling
        try:
            videoidgot.video_id
        except AttributeError:
            print("Video does not exists")
        else:
            self.isPlaying = True
            #print(self.isPlay)
            if self.isPlay is False:
                self.current = videoidgot.title

                print("Playing video:", videoidgot.title)
                self.isPlay = True
            elif self.isPlay is True:
                print("Stopping video:", self.current)
                print("Playing video:", videoidgot.title)

    Stopped = False
    def stop_video(self):
        #print(self.isPlaying)
        """Stops the current video."""
        if self.isPlaying is True:
            print("Stopping video:", self.current)
            self.isPlaying = False
        elif self.isPlaying is False:
            print("Cannot stop video: No video is currently playing")


    def play_random_video(self):
        """Plays a random video from the video library."""
        ranvid = self._video_library.get_all_videos()
        titles = []
        for x in ranvid:
            titles.append(x.title)
        print("Playing video: ", random.choice(titles))
    #stop video play video thingy
    isPaused = False
    def pause_video(self):
        """Pauses the current video."""
        if self.isPaused is False and self.isPlaying is True:
            print("Pausing video:", self.current)
            self.isPaused = True
        elif self.isPaused is True and self.isPlaying is True:
            print("Video Already Paused")
            self.isPaused = False
        if self.isPlaying is False:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.isPaused is False and self.isPlaying is True:
            print("Cannot continue video: Video is not paused")
        elif self.isPaused is True and self.isPlaying is True:
            print("Continuing video:", self.current)
            self.isPaused = False
        if self.isPlaying is False:
            print("No video is currently playing")


    def show_playing(self):
        """Displays video currently playing."""
        if self.isPlaying is True:
            i = self.currentids.tags
            print("Currently playing:", f'{self.currentids.title} ({self.currentids.video_id}) [{" ".join(i)}]')
        elif self.isPlaying is False:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("Successfully created new playlist:", playlist_name)

    global currentplaylist
    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        self.currentplaylist = playlist_name
        if self.currentplaylist != playlist_name:
            print("Successfully created new playlist:", playlist_name)
        elif self.currentplaylist == playlist_name:
            print("Cannot create playlist: A playlist with the same name already exists")


    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
