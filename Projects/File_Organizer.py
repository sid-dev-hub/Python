import os
import shutil
import glob
import base64

my_code = base64.b64encode(b'''

def listdir_nohidden(path):
    return glob.glob(os.path.join(path, '.'))

file_format = {
        
    "Documents" : [".pdf",".doc",".docx",".txt",".ppt",".pptx",".xls",".xlsx",".pptx",".docm",".odt",".rtf"],
    
    "Audios" : [".mp3",".m4a",".wav",".aiff",".aac",".ogg",".wma","flac"],
    
    "Videos" : [".mp4",".mpeg",".mpg",".mov",".mkv",".webm",".wmv",".flv"],
    
    "Images" : [".png",".jpg",".jpeg",".gif",".bmp",".svg",".bpg",".psd",".avif"],
    
    "Websites" : [".html",".htm","xhtml",".html5",".jsp",".asp"],
    
    "Zipfiles" : [".zip",".7z",".tar",".gzip",".tgz",".rar",".iso",".img",".war"],

    "Executables" : [".exe",".msi",".pkg",".bat",".run",".inf",".deb"]
}

print ("****** WELCOME TO FILE ORGANIZER ******")
print()
print("This application will sort all your files in a")
print("folder based on the file extensions")
print()
path = input("Enter the path of the folder that you wish yo organize: ")

try:
    if os.path.isdir(path):
        files = os.listdir(path)
        fileTypes = list (file_format.keys())
        file_formats = list(file_format.values())
        cleaned_ext = [item for sublist in file_formats for item in sublist]

        for file in files: 
            filename, extension = os.path.splitext(file)
            if listdir_nohidden(file) is True:
                continue  
            if os.path.isdir(path+'/'+file) or extension == ".tmp":
                continue
            else:
                if extension not in cleaned_ext:
                    try:
                        if os.path.exists(path+'/'+"Other"):
                            shutil.move(path+'/'+file, path+'/'+"Other"+'/'+file)
                            continue            
                        else:
                            os.makedirs(path+'/'+"Other")
                            shutil.move(path+'/'+file, path+'/'+"Other"+'/'+file)
                            continue
                    except Exception as e:
                        print("Unable to move one or more file, due to permission error", e)
                
                for format in file_formats:
                    
                    if extension in format:
                        folder = fileTypes[file_formats.index(format)]
                        try:
                            if os.path.exists(path+'/'+folder):
                                shutil.move(path+'/'+file, path+'/'+folder+'/'+file)        
                            else:
                                os.makedirs(path+'/'+folder)
                                shutil.move(path+'/'+file, path+'/'+folder+'/'+file)
                            break
                        except Exception as e:
                            print("Unable to move one or more file, due to permission error", e)
               
        print("Files have been successfully organized in folders.")
        print("*********** Thank you. Bye ***********")
        ex = input("Press ANY eky to exit.")

    else:
        invalid = input("You have entered an invalid path")
except:
    print("Something went wrong. Bye")
    ex = input("Press ANY eky to exit.")
    
''')
exec(base64.b64decode(my_code))
    