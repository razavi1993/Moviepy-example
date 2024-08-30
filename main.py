from moviepy.editor import *

def gamma_corr(clip, gamma_factor):
    return clip.fx(vfx.gamma_corr, gamma_factor)

clip = VideoFileClip('myvideo.mp4')

corr_clip = gamma_corr(clip, 1.4)

corr_clip.write_videofile('corrvideo.mp4')