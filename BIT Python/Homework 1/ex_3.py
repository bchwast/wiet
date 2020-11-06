import os, shutil
if __name__ == "__main__":
    files = os.listdir()
    print(files)
    images, films, music, docs = 0,0,0,0

    for file in files:
        if file[file.find("."):] == ".jpg" or file[file.find("."):] == ".png":
            if images == 0:
                os.mkdir("images")
                shutil.move(file,"images")
                images += 1
            else:
                shutil.move(file,"images")
        if file[file.find("."):] == ".mp4":
            if films == 0:
                os.mkdir("films")
                shutil.move(file,"films")
                films += 1
            else:
                shutil.move(file,"films")
        if file[file.find("."):] == ".mp3":
            if music == 0:
                os.mkdir("music")
                shutil.move(file,"music")
                music += 1
            else:
                shutil.move(file,"music")
        if (file[file.find("."):] == ".doc" or file[file.find("."):] == ".docx" or\
            file[file.find("."):] == ".odt" or file[file.find("."):] == ".pdf"):
            if docs == 0:
                os.mkdir("docs")
                shutil.move(file,"docs")
                docs += 1
            else:
                shutil.move(file,"docs")
