import os
from pytube import YouTube
from pytube import Playlist
from pytube import Channel

desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

def download_v_a(yt=None, type_=None, is_single_video=False, path_out=None, path_v=None,path_a=None) : 
    '''
    path_v, path_a = for create when using playlist or channel
    path_out for link from video (with single = True)
    '''
    title = yt.title
    if type_ == 'v' :
        stream = yt.streams.get_highest_resolution()
        
        if is_single_video : # create folder
            path_v = os.path.join(path_out,'videos')
            os.makedirs(path_v, exist_ok=True)
            print(f' ... downloading video | {title}\n to {path_v}')
        else :
            print(f' ... downloading video | {title}')
        
        stream.download(path_v)
        print(' >> successfully downloaded ')
    
    else: # audio
        stream = yt.streams.get_audio_only()
        
        if is_single_video : # create folder
            path_a = os.path.join(path_out,'audio')
            os.makedirs(path_a, exist_ok=True)
            print(f' ... downloading audio | {title}\n to {path_a}')
        else :
            print(f' ... downloading audio | {title}')
        
        out_file = stream.download(path_a)

        # to mp3
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(' >> successfully downloaded ')


print(' you can use URL from video(v), playlist(p) or channel(c)')
url_type = input('url from : ').lower()
URL = input('url : ')

if url_type == 'p' : # playlist
    p = Playlist(URL)
    playlist_name = p.title
    print(f'>> {playlist_name}')
    video_url = p.video_urls
    
    print(' video(v) or audio(a) ? ')
    type_ = input(': ').lower()
    print('how many to download ? , all(a)')
    num_va = input('number of videos : ')
    num_va = int(num_va) if num_va != 'a' else num_va.lower()

    # makedirs
    path_va = os.path.join(desktop_path,'yt_videos',playlist_name)
    os.makedirs(path_va, exist_ok=True)

    video_url = video_url[:num_va] if num_va != 'a' else video_url
    for url in video_url :
        yt = YouTube(url)
        download_v_a(yt,type_=type_,path_v=path_va,path_a=path_va)
    print()
    print(f'    download all video\n    to {path_va}')

elif url_type == 'c' : # channael
    c = Channel(URL)
    channel_name = c.channel_name
    print(f'>> {channel_name}')
    video_url = list(c.video_urls)
    
    print(' video(v) or audio(a) ? ')
    type_ = input(': ').lower()
    print('how many to download ? , all(a)')
    num_va = input('number of videos : ')
    num_va = int(num_va) if num_va != 'a' else num_va.lower()

    # makedirs
    path_va = os.path.join(desktop_path,'yt_videos',channel_name)
    os.makedirs(path_va, exist_ok=True)
    
    # recently ?
    if num_va != 'a' :
        print('from recenly(y) or not(n) ?')
        from_ = input(' recenly ? : ').lower()
        
        if from_ == 'n':
            video_url_reversed = []
            i = 1
            for video in range(num_va) :
                video_url_reversed.append(video_url[-i])
                i+=1
            video_url = video_url_reversed

        else :
            video_url = video_url[:num_va] 
    
    for url in video_url :
        yt = YouTube(url)
        download_v_a(yt,type_=type_,path_v=path_va,path_a=path_va)
    print()
    print(f'    download all video\n    to {path_va}')


else : # url from video
    yt = YouTube(URL)
    title = yt.title
    print(f' {title}')
    print(' video(v) or audio(a) ? ')
    type_ = input(': ').lower()

    # path 
    path_out = os.path.join(desktop_path,'yt_videos')
    os.makedirs(path_out, exist_ok=True)
    
    download_v_a(yt,type_=type_,is_single_video=True, path_out=path_out)



    