# File Organizer

A small Python script that sorts files in the current working directory into category folders.

## What it does

- Creates these folders if needed: `Images`, `Videos`, `Documents`, `Audio`, `Miscellaneous`
- Moves files into the matching folder based on file extension
- Skips directories and the script file itself
- Handles name collisions by appending ` (1)`, ` (2)`, etc.
- Uses only `os` and `shutil`

## Supported extensions

- `Images`: `.jpg`, `.jpeg`, `.png`, `.gif`
- `Videos`: `.mp4`, `.avi`, `.mov`
- `Documents`: `.pdf`, `.docx`, `.txt`
- `Audio`: `.mp3`, `.wav`
- All other files go to `Miscellaneous`

## Usage

Run the script from the directory you want to organize:

```powershell
E:/Python/python3.14t.exe D:\path\to\FileOrganizer.py
```

Or, change to your target folder first:

```powershell
cd C:\path\to\folder
E:/Python/python3.14t.exe D:\path\to\FileOrganizer.py
```

## Notes

- The script is not recursive: it only organizes files in the current folder.
- Hidden files are treated like regular files.
- If a destination file already exists, the script renames the moved file to avoid overwriting.
