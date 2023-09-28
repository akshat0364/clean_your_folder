import os #OS Python provides functions for interacting with the operating system
import shutil #shutil in python helps in creating folders and directories
#the code can be ammended as per your usage of organising files very easily, you can change the name of the file or check different extensions or file name and follow the same steps as in the code
src = '.'
ppt_files = []
pdf_files = []
word_files = []
excel_files = []

pdf_d = './PDFs'
ppt_d = './PPTs'
word_d = './WordDocs'
excel_d = './ExcelStuff'

#so this loop basically puts all the files in directory to the empty lists i created 
for file in os.listdir(src):
    if file.endswith('.doc') or file.endswith('.docx'):
        word_files.append(file)
    if file.endswith('.xlsx'):
        excel_files.append(file)
    if file.endswith('.ppt') or file.endswith('.pptx'):
        ppt_files.append(file)
    if file.endswith('.pdf'):
        pdf_files.append(file)



#we need a function to make sure files are all with unique names
def make_name(name, dest_list):
    n, e = os.path.splitext(name) #splits into name and extension
    for file_name in dest_list:
        dn, de = os.path.splitext(file_name)
        if not n[-1].isnumeric():  #If the last character of n is numeric, it enters a while loop to increment the numeric suffix until n is no longer found in dn.
            if n == dn:
                n = n + '1'
        if n[-1].isnumeric():
            while True:
                if n in dn:
                    n = n[:-1] + str(int(n[-1])+1)
                else:
                    break

    return n+e



#For each file in the list, it checks if the destination directory (word_d) exists. If it doesn't, it creates the directory. Then, it renames the file using the make_name function to ensure uniqueness and moves it to the word_d directory.
for files in word_files:
 if not os.path.exists(word_d):
    os.makedirs(word_d)  #if file with name doesnt exist in the same folder then we create new foldeer
 os.rename(os.path.join(src,files), os.path.join(src, make_name(files, os.listdir(word_d))))
 shutil.move(os.path.join(src, make_name(files, os.listdir(word_d))), word_d)

for files in excel_files:
    if not os.path.exists(excel_d):
     os.makedirs(excel_d)
    os.rename(os.path.join(src,files), os.path.join(src, make_name(files, os.listdir(excel_d))))
    shutil.move(os.path.join(src, make_name(files, os.listdir(excel_d))), excel_d)

for files in ppt_files:
    if not os.path.exists(ppt_d):
     os.makedirs(ppt_d)
    os.rename(os.path.join(src,files), os.path.join(src, make_name(files, os.listdir(ppt_d))))
    shutil.move(os.path.join(src, make_name(files, os.listdir(ppt_d))), ppt_d)

for files in pdf_files:
    if not os.path.exists(pdf_d):
      os.makedirs(pdf_d)
    os.rename(os.path.join(src,files), os.path.join(src, make_name(files, os.listdir(pdf_d))))
    shutil.move(os.path.join(src, make_name(files, os.listdir(pdf_d))), pdf_d)

