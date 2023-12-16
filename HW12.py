import os
import shutil
# with open('file3','r',encoding='utf-8') as file3:
#     nsl = set(file3.read().splitlines())
# with open('file1','r',encoding='utf-8') as file1, open('file2','w',encoding='utf-8') as file2:
#     b = file1.read()
#     print(b)
#     for j in b.split():
#         if j not in nsl:
#             file2.write(j+' ')


# from translate import Translator
# with open('rus','r',encoding='utf-8') as rus, open('eng','w',encoding='utf-8') as eng:
#     s1=rus.read()
#     translator=Translator(from_lang='ru',to_lung='en')
#     perevod=translator.translate(s1)
#     eng.write(perevod)


# while True:
#     dfile=input()
#     if dfile=='quit':
#         break
#     with open('file4', 'a', encoding='utf-8') as vfile, open(dfile, 'r', encoding='utf-8') as file:
#         s = file.read()
#         vfile.write(s)
#         vfile.write('\n')

# files=[]
# while True:
#     dfile=input()
#     if dfile=='quit':
#         break
#     files.append(dfile)
# with open(files[0], 'r', encoding='utf-8') as vfile:
#     znaki1=set(vfile.read())
# for file in files[1:]:
#     a=open(file, 'r', encoding='utf-8')
#     znaki=set(a.read())
#     obznaki=znaki1.intersection(znaki)
#     with open('file4', 'w', encoding='utf-8') as pfile:
#         pfile.write(''.join(obznaki))

# c=os.path.join(os.getcwd(), 'watch_me')
# os.makedirs(c, exist_ok=True)
# video_path=os.path.join(os.getcwd(), 'video')
# a=os.listdir(video_path)
# for file in a:
#     s1=os.path.join(video_path, file)
#     d1=os.path.join(c, file)
#     shutil.copy(s1, d1)
# sub_path=os.path.join(os.getcwd(), 'sub')
# b=os.listdir(sub_path)
# for file in b:
#     s2=os.path.join(sub_path, file)
#     d2=os.path.join(c, file)
#     shutil.copy(s2, d2)
# print(os.listdir(c))


# files_path=os.getcwd()
# files=os.listdir(files_path)
# for file in files:
#     parts=file.split('_')
#     if len(parts)==2:
#         imia, familia = parts
#         new_file=f"{familia}_{imia}"
#         os.rename(os.path.join(files_path, file),os.path.join(files_path, new_file))

# files_path=os.getcwd()
# files=os.listdir(files_path)
# os.mkdir('list')
# list_directory = os.path.join(files_path, 'list')
# for file in files:
#     if file == 'list.tvs':
#         with open('list.tvs','r',encoding='utf-8') as list:
#             name_files = [line.strip() for line in list]
# print(name_files)
# for file in files:
#     if file in name_files:
#         path1=os.path.join(files_path, file)
#         path2= os.path.join(list_directory, file)
#         shutil.move(path1, path2)
# print(os.listdir('list'))

# with open('file4','r',encoding='utf-8')as file4:
#     lines_file=file4.readlines()
#     for i in range(len(lines_file)-1):
#         with open('rus','a', encoding='utf-8')as rus:
#             rus.write(lines_file[i])



