from pathlib import Path
import sys
folder_path = Path(input('enter folder path:').strip())
if not folder_path.is_dir():
    print('Please enter a valid folder')
    sys.exit()
counter = 1
user_picks = input('Enter a prefix: ').strip()

while True:
    confirm = input('Rename files:(y/n) ?').lower()
    if confirm in ('y', 'yes'):
        break
    else:
        print('exiting...')
        sys.exit()
for file in folder_path.iterdir():
    if file.is_dir():
        continue
    if file.name.lower().startswith('.') or file.name.lower() in ('thumbs.db', 'desktop.ini'):
        continue
    file_suffix = file.suffix
    name_create = f'{user_picks}_{counter:03}{file_suffix}'
    new_path = folder_path / name_create
    if new_path.exists():
        while new_path.exists():
            counter += 1
            name_create = f'{user_picks}_{counter:03}{file_suffix}'
            new_path = folder_path / name_create 
    file.rename(new_path)
    print(f'\n✓ Renamed: \n\n{file.name} \n↓\n\n{new_path.name}')
    counter += 1
print("\n==========")
print("Finished!")
print(f"Files renamed: {counter - 1}")
print("==========")