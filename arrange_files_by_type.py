import os
import shutil


def sorter():
    try:
        pc_name = input('Enter your PC name: ')
        path = input('Enter the source directory. e.g C:/Users/My_PC/Downloads: ')
        destination = 'C:/Users/%s'%pc_name

        # path = 'C:/Users/USER/Downloads'
        # destination = 'C:/Users/USER/Desktop/'

        destination = 'C:/Users/%s'%user_source


        list_ = os.listdir(path)

        for file_ in list_:
            name, ext = os.path.splitext(file_)

            ext = ext[1:]
            src_path = os.path.join(path, file_)
            
                #Videos
            if ext in ['mp4', 'mkv', '3gp', 'mov', 'avi', 'webm', 'flv', 'wmv'] and os.path.exists(destination+'/'+'Videos'):
                print('Moving Video files to %s/Videos'%destination)
                shutil.move(src_path,destination+'/'+'Videos'+ '/'+file_)
                
            elif ext in ['mp4', 'mkv', '3gp', 'mov', 'avi', 'webm', 'flv', 'wmv']:
                os.makedirs(destination+'/'+'Videos')
                shutil.move(src_path, destination+'/'+'Videos'+ '/'+file_)

                #Pictures
            elif ext in ['png', 'jpg', 'bmp', 'jpeg', 'gif','ico', 'jpe', 'webp'] and os.path.exists(destination+'/'+'Pictures'):
                print('Moving Image files to %s/Pictures'%destination)
                shutil.move(src_path, destination+'/'+ 'Pictures'+'/'+file_)
            
            elif ext in ['png', 'jpg', 'bmp', 'jpeg', 'gif','ico', 'jpe', 'webp']:    
                os.makedirs(destination+'/'+'Pictures')
                shutil.move(src_path, destination+'/'+ 'Pictures'+'/'+file_)
                
                #Documents
            elif ext in ['pdf', 'doc', 'docx', 'txt', 'rtf','epub', 'mobi', 'csv', 'ipynb'] and os.path.exists(destination+'/'+'Documents'):
                print('Moving Document files to %s/Documents'%destination)
                shutil.move(src_path, destination+'/'+ 'Documents'+'/'+file_)
            
            elif ext in ['pdf', 'doc', 'docx', 'txt', 'rtf','epub', 'mobi', 'csv', 'ipynb']:      
                os.makedirs(destination+'/'+'Documents')
                shutil.move(src_path, destination+'/'+ 'Documents'+'/'+file_)

               #Subtitles
            elif ext in ['srt'] and os.path.exists(destination+'/'+'Subtitles'):
                print('Moving Subtitle files to %s/Subtitles'%destination)
                shutil.move(src_path, destination+'/'+ 'Subtitles'+'/'+file_)
            
            elif ext in ['srt']:      
                os.makedirs(destination+'/'+'Subtitles')
                shutil.move(src_path, destination+'/'+ 'Subtitles'+'/'+file_)

                #ZipArchives
            elif ext in ['zip', 'rar', '7z', 'gz'] and os.path.exists(destination+'/'+'Archive'):
                print('Moving Zip files to %s/Archive'%destination)
                shutil.move(src_path, destination+'/'+ 'Archive'+'/'+file_)
            
            elif ext in ['zip', 'rar', '7z', 'gz']:      
                os.makedirs(destination+'/'+'Archive')
                shutil.move(src_path, destination+'/'+ 'Archive'+'/'+file_)
            
             #Music
            elif ext in ['mp3', 'ogg', 'wav', 'aac', 'flac'] and os.path.exists(destination+'/'+'Music'):
                print('Moving Music files to %s/Music'%destination)
                shutil.move(src_path, destination+'/'+ 'Music'+'/'+file_)
            
            elif ext in ['mp3', 'ogg', 'wav', 'aac', 'flac']:      
                os.makedirs(destination+'/'+'Music')
                shutil.move(src_path, destination+'/'+ 'Music'+'/'+file_)

            else:
                ('No file to Move!!!')
    except KeyboardInterrupt:
        exit('\nClosing!!!')
    except FileNotFoundError:
        print('Invalid Directory!!')
        return sorter()

sorter()
