from dataclasses import dataclass


@dataclass
class Video:
    name: str
    format: str
    size: int


class VideoEditor:
    def edit_video(self, filename: str):
        print(f"Editing video: {filename}")
        # resolves video filename and returns a video object
        video = Video(filename, "raw", 26745)
        return video


class VideoConverter:
    def convert_format(self, video: Video) -> Video:
        print("Converting video to mp4 format")
        video.format = "mp4"
        return video


class VideoUploader:
    def upload_video(self, video: Video) -> bool:
        print("Uploading video to Instagram...")
        uploaded = False
        self.generic_upload()
        # Implement upload logic
        uploaded = True

        return uploaded

    def generic_upload(self):
        ...


class VideoPublisher:
    def __init__(self):
        self._video_editor = VideoEditor()
        self._video_uploader = VideoUploader()
        self._video_converter = VideoConverter()

    def publish(self, filename: str):
        video = self._video_editor.edit_video(filename)
        video = self._video_converter.convert_format(video)
        status = self._video_uploader.upload_video(video)

        if status:
            print("The video has been uploaded!")
            return

        print("The video has failed to upload")
