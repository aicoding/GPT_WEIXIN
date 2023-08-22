import chainlit as cl
import glob
import difflib
import subprocess

MUSIC_DIR ="./tmp"

async def show_images(title: str,paths: str):
    """
    If your return contains images in png or jpg format, you can call this function to display the images.
    Parameters: title: The title of the image. paths: The path of the image.(required)
    paths: The paths of the images as a comma-separated string.(required)
    """
    path_list = paths.split(',')
    elments = []
    for i, path in enumerate(path_list):
        if 'tmp' in path:
            tmp_image = cl.Image(name=f"image{i}",path=path.strip(),display="inline")
        elif path.startswith("./"):
            tmp_image = cl.Image(name=f"image{i}",path='./tmp/'+(path.strip().replace("./","")),display="inline")  #图片和视频都放在本地./tmp目录下
        else:
            tmp_image = cl.Image(name=f"image{i}",path='./tmp/'+path.strip(),display="inline")  #图片和视频都放在本地./tmp目录下

    tmp_image.size = "large"
    elments.append(tmp_image)

    await cl.Message(content=title,elements=elments).send()  # type: ignore
    return {'description': '图片已经显示成功了，下面的回复中不再需要展示它了'}

async def play_music(kw:str):
    """
    根据用户提供的曲名关键字播放音乐.
    Parameters: kw: 歌曲名字关键字.(required)
    """
    fs = glob.glob(f'''{MUSIC_DIR}/*.mp3''')
    matches = difflib.get_close_matches(kw,fs,cutoff=0.01)
    if any(matches):
        best = matches[0]
        # potplayer.run(best)
        subprocess.call(["afplay", best])
        await cl.Message(content='音乐正在播放中').send()
        return {'description': '音乐正在播放中，下面的回复中不再需要展示它了'}
    else:
        await cl.Message(content='没有可以播放的相关音乐').send()
        return {'description': '没有可以播放的相关音乐'}

async def play_movie(kw:str):
    """
    根据用户提供的电影名关键字播放电影.
    Parameters: kw: 电影名关键字.(required)
    """
    fs = glob.glob(f'''{MUSIC_DIR}/*.mov''')
    matches = difflib.get_close_matches(kw,fs,cutoff=0.01)
    if any(matches):
        best = matches[0]
        # potplayer.run(best)
        subprocess.call(["afplay", best])
        await cl.Message(content='电影正在播放中').send()
        return {'description': '电影正在播放中，下面的回复中不再需要展示它了'}
    else:
        await cl.Message(content='没有可以播放的相关电影').send()
        return {'description': '没有可以播放的相关电影'}    

   