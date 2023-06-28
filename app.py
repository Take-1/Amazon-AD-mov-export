import os
from subprocess import call


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

    command = [
        "ffmpeg.exe",
        "-i",
        f"{i_path}\\L.wav",
        "-i",
        f"{i_path}\\R.wav",
        "-map",
        "0",
        "-map",
        "1",
        "-vcodec",
        "copy",
        "-acodec",
        "copy",
        os.path.join(output, i + ".mov"),
    ]

    call(command)
