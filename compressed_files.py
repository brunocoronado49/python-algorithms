from PIL import Image
import os

#* Declare downsloads folder
downloads_folder = "/Users/brunocoronado/Downloads/"

if __name__=='__main__':
    #* Itrerate the files in downloads folder
    for file in os.listdir(downloads_folder):
        #* Extract the name and extension
        name, extension = os.path.splitext(downloads_folder + file)

        #* Check extensions in the file
        if extension in [".jpg", ".jpeg", ".png"]:
            #* Set the file in variable and save it
            pic = Image.open(downloads_folder + file)
            pic.save(downloads_folder + 'compressed_' + file, optimize=True, quality=40)