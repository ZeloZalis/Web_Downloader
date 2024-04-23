import pytube

#La siguiente función permite obtener la calidad del vídeo a descargar
def GetVideoQuality(url):
    try:
        #Obtenemos el vídeo, y creamos una lista con las resoluciones y bitrates
        yt = pytube.YouTube(url)
        base_list = []
        for stream in yt.streams:
            resolution = stream.resolution
            bitrate = stream.bitrate
            base_list.append({'resolution':resolution, 'bitrate':bitrate})
    
        #Creamos un diccionario y una lista vacía, en la que estarán las calidades con mayor bitrate
        new_dict = {}
        fixed_list = []

        #Vamos revisando ítem por ítem de la lista para ir agregándolos a la nueva
        #Si el valor 'resolution' está repetido, se va a dejar sólo el que tenga el mayor bitrate dentro
        #De la nueva lista. Si el valor es None, no se agregará a la lista
        for diccionario in base_list:
            resolution = diccionario['resolution']
            bitrate = diccionario['bitrate']
            if resolution is not None:
                if resolution not in new_dict:
                    new_dict[resolution] = bitrate
                    fixed_list.append(diccionario.copy())
                else:
                    if bitrate > new_dict[resolution]:
                        new_dict[resolution] = bitrate
                        fixed_list.remove([d for d in fixed_list if d['resolution'] == resolution][0])
                        fixed_list.append(diccionario.copy())

        #Retornamos la nueva lista
        return fixed_list
    except Exception as e:
        print(f"Error: {e}")

def VideoDownload_mp4(url, res, name):
    try:
        yt = pytube.YouTube(url)
        folder = "YouTube_Videos"
        video = yt.streams.get_by_resolution(resolution=res)
        video.download(folder, filename=f"{name}.mp4")
        print("downloaded.")
    except Exception as e:
        print(f"\n{e}")
        print("Can't download this resolution.")

def VideoDownload_mp3(url, name):
    try:
        yt = pytube.YouTube(url)
        folder = "YouTube_Music"
        stream = yt.streams.get_audio_only()
        stream.download(folder, filename=f"{name}.mp3")
        print("\nDownloaded.")
    except Exception as e:
        print(f"Error: {e}")