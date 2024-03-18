import os

def createIFNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.rename(file, f"{folderName}/{file}")

if __name__ == "__main__":

    files = os.listdir()
    files.remove("folder cleaner main.py")


    createIFNotExist('Images')
    createIFNotExist('Docs')
    createIFNotExist('Media')
    createIFNotExist('other')

    imgExts = [".png", ".jpg",".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    docExts = [".txt", ".docx", "doc", ".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]


    mediaExts = [".mp3",".mp4"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    other = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
            other.append(file)

       
    move("Images", images)
    move("Docs", docs)
    move("Media", medias)
    move("other", other)

    