import os

jpg_folder = 'jpg_font_ah/아'
extraction_folder = 'extraction'
prefix = 'Gaji_'

# 'extraction' 폴더의 파일 리스트를 가져옵니다.
extraction_files = os.listdir(extraction_folder)

# 'jpg_font_ah' 폴더의 파일 리스트를 가져옵니다.
jpg_files = os.listdir(jpg_folder)

# 'jpg_folder' 폴더에 있는 파일명 앞에 'Gaji_'를 붙입니다.
extraction_files_prefixed = [prefix + file for file in jpg_files]

# 'jpg_font_ah' 폴더에 있는 파일 중 'extraction' 폴더에 없는 파일을 찾습니다.
files_not_in_extraction = [file for file in jpg_files if file not in extraction_files_prefixed]

# 결과를 출력합니다.
print("The following JPG files are not in the 'extraction' folder:")
for file in files_not_in_extraction:
    print(file)