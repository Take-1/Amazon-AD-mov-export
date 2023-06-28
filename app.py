import os
from subprocess import call


def transcode():
    name, ext = os.path.splitext(file)
    newname = name + ".mp4"

    command = ["E:\\CORE\\Users\\jhayward\\transcode_library\\ffmpeg.exe", "-i", source + file, 
            "-b:v", vkbps, "-c:v", "libx264", "-s", width+"x"+height, 
            "-pix_fmt", "yuv420p", "-threads", "2", "-f", "mp4", 
            "-preset", "superfast", output + "[TRANSCODING]" + newname]

    command[11:0] = audio_arg

    print(command)

    if quality in {"1a", "2a", "3a", "4a",}:
        frame_rate = ""
    elif  quality in {"1b", "2b", "3b"}:
        frame_rate = ["25", "-r"]
        for item in frame_rate:
            command.insert(11, item)

    call(command)

    if os.path.exists(source+file) == True:
        os.rename(output + "[TRANSCODING]" + name + ".mp4", 
                    output + "[INCOMPLETE]" + name + ".mp4")
    else:
        pass
    
    try:
        os.rename(output + "[INCOMPLETE]" + name + ".mp4", 
                    output + name + ".mp4")
    except Exception as e:
        print(e)
        

    tfileinfo = os.stat(os.path.join(output, outfilename))
    outsize = tfileinfo[6]

root = os.getcwd()
print(root)

input = os.path.join(root, "input")
input_list = os.listdir(input)
output = os.path.join(root, "output")
output_list = os.listdir(output)

for i in input_list:
    print(f"converting {i} to mov with two audio tracks")

    i_path = os.path.join(input, i)
    i_list = os.listdir(i_path)

    for f in i_list:
        print(f)

        if f not in ["L.wav", "R.wav"]:
            print("please only add left and right wavs named L.wav and R.wav")
            exit()

    command = ["ffmpeg.exe", "-i", f"{i_path}\\L.wav", "-i", f"{i_path}\\R.wav", "-map", "0", "-map", "1", "-vcodec", "copy", "-acodec", "copy", os.path.join(output, i + ".mov")]

    call(command)

    #ffmpeg -i captain-marvel-trailer.mp4 -i tamil.mp3 -i telugu.mp3 -i hindi.mp3 -map 1 -map 2 -map 3 -metadata:s:a:0 language=eng -metadata:s:a:1 language=tam -metadata:s:a:2 language=tel -metadata:s:a:3 language=hin -codec copy multilanguage.mp4