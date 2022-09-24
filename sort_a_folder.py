import os
import shutil

user_source = input('Enter your PC name: ')
source = input('Enter the source directory. e.g Downloads: ').capitalize()
path = 'C:/Users/%s/%s'%(user_source, source)

list_ = os.listdir(path)

for file_ in list_:
    name, ext = os.path.splitext(file_)


    ext = ext[1:]
        #Videos
    if ext in ['mp4', 'mkv'] and os.path.exists(path+'/'+'Vids'):
        print('Moving Videos to %s/Vids'%path)
        shutil.move(path+'/'+file_, path+'/'+'Vids'+ '/'+file_)
        
    elif ext in ['mp4', 'mkv'] and os.path.exists(path+'/'+'Vids') == False:
        os.makedirs(path+'/'+'Vids')
        shutil.move(path+'/'+file_, path+'/'+'Vids'+ '/'+file_)

        #Pictures
    elif ext in ['png', 'jpg', 'bmp', 'jpeg', 'gif','ico', 'jpe', 'webp'] and os.path.exists(path+'/'+'Pictures'):
        print('Moving Pictures to %s/Pictures'%path)
        shutil.move(path+'/'+file_, path+'/'+'Pictures'+'/'+file_)
    
    elif ext in ['png', 'jpg', 'bmp', 'jpeg', 'gif','ico', 'jpe', 'webp'] and os.path.exists(path+'/'+'Pictures') == False:      
        os.makedirs(path+'/'+'Pictures')
        shutil.move(path+'/'+file_, path+'/'+'Pictures'+ '/'+ file_)
        
        #Documents
    elif ext in ['pdf', 'doc', 'docx', 'txt', 'rtf','epub', 'mobi', 'csv', 'ipynb'] and os.path.exists(path+'/'+'Documents'):
        print('Moving Documentsto %s/Documents'%path)
        shutil.move(path+'/'+file_, path+'/'+'Documents'+'/'+file_)
    
    elif ext in ['pdf', 'doc', 'docx', 'txt', 'rtf','epub', 'mobi', 'csv', 'ipynb'] and os.path.exists(path+'/'+'Documents') == False:      
        os.makedirs(path+'/'+'Documents')
        shutil.move(path+'/'+file_, path+'/'+'Documents'+ '/'+ file_)
       
       
       #Subtitles
    elif ext in ['srt'] and os.path.exists(path+'/'+'Subtitles'):
        print('Moving Subtitles to %s/Subtitles'%path)
        shutil.move(path+'/'+file_, path+'/'+'Subtitles'+'/'+file_)
    
    elif ext in ['srt'] and os.path.exists(path+'/'+'Subtitles') == False:      
         os.makedirs(path+'/'+'Subtitles')
         shutil.move(path+'/'+file_, path+'/'+'Subtitles'+ '/'+ file_)
    
        #ZipArchives
    elif ext in ['zip', 'rar', '7z', 'gz'] and os.path.exists(path+'/'+'Archive'):
        print('Moving Zips to %s/Archive'%path)
        shutil.move(path+'/'+file_, path+'/'+'Archive'+'/'+file_)
    
    elif ext in ['zip', 'rar', '7z', 'gz'] and os.path.exists(path+'/'+'Archive') == False:      
        os.makedirs(path+'/'+'Archive')
        shutil.move(path+'/'+file_, path+'/'+'Archive'+ '/'+ file_)
       
    elif ext in ['html', 'htm'] and os.path.exists(path+'/'+'Html'):
        print('Moving Html to %s/Html'%path)
        shutil.move(path+'/'+file_, path+'/'+'Html'+'/'+file_)
    
    elif os.path.exists(path+'/'+'Html') == False:      
        os.makedirs(path+'/'+'Html')
        shutil.move(path+'/'+file_, path+'/'+'Html'+ '/'+ file_)
    
    elif ext in ['mp3', 'ogg', 'wav', 'aac', 'flac'] and os.path.exists(path+'/'+'Music'):
        print('Moving Music files to %s/Music'%path)
        shutil.move(src_path, destination+'/'+ 'Music'+'/'+file_)

    elif os.path.exists(path+'/'+'Music') == False:     
        os.makedirs(path+'/'+'Music')
        shutil.move(path+'/'+ file_, path + '/'+ 'Music'+'/'+file_)

