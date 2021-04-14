import os,shutil
dic_extensions = {
'audio_extensions' : ('mp3','wma','wav','flac','m4a'),
'video_extensions' : ('mp4','wmv','mkv','flv','avi','mpeg'),
'doc_extentions' : ('doc','docx','pdf','txt'),
'program_extentions' : ('exe','rar','apk','ios')
}

folderpath= input('Enter your path : ')

def file_finder(path,file_extension):
    files=[]
    for file in os.listdir(path):
        for extention in file_extension:
            if file.endswith(extention):
                files.append(file)
    return files 

for extension_name,extension_tuple in dic_extensions.items():
    folder_name=extension_name.split('_')[0]  +" files"
    path=os.path.join(folderpath,folder_name)
    os.mkdir(path)
    for item in file_finder(folderpath,extension_tuple):
        item_path= os.path.join(folderpath,item)
        item_new_path= os.path.join(path,item)
        shutil.move(item_path,item_new_path)

    # print('Calling file finder')
    # print(file_finder(folderpath,extension_tuple))               