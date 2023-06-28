import os
import shutil

file_format = {
        
    "Documents" : [".pdf",".doc",".docx",".txt","ppt",".xls",".xlsx",".pptx",".docm",".odt",".rtf"],
    
    "Audios" : [".mp3",".m4a",".wav",".aiff",".aac",".ogg",".wma","flac"],
    
    "Videos" : [".mp4",".mpeg",".mpg",".mov",".mkv",".webm",".wmv",".flv"],
    
    "Images" : [".png",".jpg",".jpeg",".gif",".bmp",".svg",".bpg",".psd",".avif"],
    
    "Websites" : [".html",".htm","xhtml",".html5",".jsp",".asp"],
    
    "Zipfiles" : [".zip",".7z",".tar",".gzip",".tgz",".rar",".iso",".img"],

    "Executables" : [".exe",".msi",".pkg",".bat",".run",".inf",".deb"]
}
print ("****** WELCOME TO THE FILE ORGANIZER ******")
print()
path = input("Enter the path of the folder that you wish yo organize: ")
files = os.listdir(path)

fileTypes = list (file_format.keys())
file_formats = list(file_format.values())

for file in files: 
    filename, extension = os.path.splitext(file)
    
    if os.path.isdir(path+'/'+file):
        continue
    else:
        if extension == "" or extension not in file_formats:
            if os.path.exists(path+'/'+"Other"):
                shutil.move(path+'/'+file, path+'/'+"Other"+'/'+file)
                continue            
            else:
                os.makedirs(path+'/'+"Other")
                shutil.move(path+'/'+file, path+'/'+"Other"+'/'+file)
                continue
            
        for format in file_formats:
            
            if extension in format:
                folder = fileTypes[file_formats.index(format)]
                if os.path.exists(path+'/'+folder):
                    shutil.move(path+'/'+file, path+'/'+folder+'/'+file)
                                
                else:
                    os.makedirs(path+'/'+folder)
                    shutil.move(path+'/'+file, path+'/'+folder+'/'+file)
                break

print("All your files have been successfully organized into folders.")
print("Thank you.. Bye..")