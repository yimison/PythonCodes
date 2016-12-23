import os
import time
import  zipfile

source=['D:\\workspace\\coding\\Python\\'];
target_dir=r'D:\workspace\coding\PythonBackUp';
target_file=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip';

f = zipfile.ZipFile( target_file, 'w', zipfile.ZIP_DEFLATED )
for dirpath, dirnames, filenames in os.walk(''.join(source)):
     for filename in filenames:
        filepath=os.path.join(dirpath,filename);
        print(filepath)
        f.write(filepath)

f.close()
print('备份成功');


