"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""
    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        all_videos = self._video_library.get_all_videos()
        sorted_videos = sorted(all_videos, key=lambda x:x.title) #lambda function to grab titles,and sort titles out
        print("Here's a list of all available videos:")
        for sorted_videos in sorted_videos:#for loop adding atttributes,
            title_txt = str(sorted_videos.title)
            video_id_text = "("  + "".join(sorted_videos.video_id) + ")"
            tags_txt = "[" + " ".join(sorted_videos.tags) + "]"
            print(f"{title_txt} {video_id_text} {tags_txt}")

    def play_video(self, video_id):
        all_videos = self._video_library.get_all_videos()
        vidlist = []                #adds videos to list,so it can grab currently playing video
        for x in all_videos:
            vidlist.append(x.video_id)      #adds videoid,and checks if the video is valid

        if vidlist.count(video_id) ==1:

            play = self._video_library.get_video(video_id)  #plays video
            if len(self._video_library.vidlist) ==0:
                print("Playing video: " + str(play.title))
                self._video_library.vidlist.append(play.title)
            elif len(self._video_library.vidlist) > 0:              #stops current video,and plays next one
                print("Stopping video: " + self._video_library.vidlist[0])
                print("Playing video: " + str(play.title))
                self._video_library.pause.clear()
                self._video_library.vidlist.clear()
                self._video_library.vidlist.append(play.title)
        else:
            print("Cannot play video: Video does not exist")        #case if video doesnt exist



    def stop_video(self):
        current_video = self

        if len(self._video_library.vidlist) > 0:
            print("Stopping video: " + self._video_library.vidlist[0])#stops video and clears vidlist,and the pause function
            self._video_library.vidlist.clear()
            self._video_library.pause.clear()
        else:
            print("Cannot stop video: No video is currently playing")#cause for no stop,video not playing


    def play_random_video(self):

        if len(self._video_library.vidlist) ==0:
            all_videos = self._video_library.get_all_videos()
            digit = random.randint(0, (len(all_videos) - 1))#uses random digits to generate random video
            print("Playing video: " + str(all_videos[digit].title))
            self._video_library.vidlist.append(all_videos[digit].title)
        elif len(self._video_library.vidlist) >0:
            all_videos = self._video_library.get_all_videos()
            digit = random.randint(0, (len(all_videos) - 1))
            print("Stopping video: " + self._video_library.vidlist[0])
            print("Playing video: " + str(all_videos[digit].title))
            self._video_library.vidlist.clear()
            self._video_library.vidlist.append(all_videos[digit].title)




    def pause_video(self):              #pauses video by adding pause to another functions,
        if len(self._video_library.vidlist) > 0 and len(self._video_library.pause) == 0:
            print("Pausing video: " + self._video_library.vidlist[0])
            self._video_library.pause.append("pause")
        elif len(self._video_library.pause) == 1:
            print("Video already paused: " + self._video_library.vidlist[0])
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        if len(self._video_library.pause) == 0 and len(self._video_library.vidlist) > 0:
            print("Cannot continue video: Video is not paused")
        elif len(self._video_library.pause) == 0 and len(self._video_library.vidlist) == 0:
            print("Cannot continue video: No video is currently playing")
        elif len(self._video_library.pause) > 0:
            print("Continuing video: " + str(self._video_library.vidlist[0]))





    def show_playing(self):#shows playing by finding the video among the list of ids, using the index function,
        if len(self._video_library.vidlist) > 0:#to get the attributes
            all_videos = self._video_library.get_all_videos()
            vidlist = []
            for x in all_videos:
                vidlist.append(x.title)
            position = vidlist.index(self._video_library.vidlist[0])

            title_txt = str(all_videos[position].title)
            video_id_text = "(" + "".join(all_videos[position].video_id) + ")"
            tags_txt = "[" + " ".join(all_videos[position].tags) + "]"
            if len(self._video_library.pause)==1:
                print("Currently playing: " + f"{title_txt} {video_id_text} {tags_txt}" + " - PAUSED")
            else:
                print("Currently playing: " + f"{title_txt} {video_id_text} {tags_txt}")
        else:
            print("No video is currently playing")


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

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
