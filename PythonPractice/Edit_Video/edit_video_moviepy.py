from moviepy.editor import *


def function_1():
    video = VideoFileClip("Final_Demo.mp4").subclip(0,338)
    result = CompositeVideoClip([video]) # Overlay text on video
    result.write_videofile("part1.mp4",fps=25) # Many options...


def function_2():
    video = VideoFileClip("Final_Demo.mp4").subclip(343, 1280)
    result = CompositeVideoClip([video])  # Overlay text on video
    result.write_videofile("part2.mp4", fps=25)  # Many options...

def merge_two_video():
    from moviepy.editor import VideoFileClip, concatenate_videoclips
    clip1 = VideoFileClip('part1.mp4')
    clip2 = VideoFileClip('part2.mp4')
    final_clip = concatenate_videoclips([clip1, clip2])
    final_clip.write_videofile("Final_demo_edited.mp4")

#function_1()
#function_2()
merge_two_video()