import os

# Enter the folder path here
folder_path = 'C:/Users/DittNamn/Documents/pictures'

# Byt namn på alla filer i mappen
for count, filename in enumerate(os.listdir(folder_path), start=1):
    file_ext = os.path.splitext(filename)[1]
    new_name = f"bild_{count}{file_ext}"
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)
    os.rename(src, dst)

print("✅ All files have been renamed!")
