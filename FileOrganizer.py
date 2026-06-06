import os
import shutil

base = os.getcwd()
categories = {
    "Images": (".jpg", ".jpeg", ".png", ".gif"),
    "Videos": (".mp4", ".avi", ".mov"),
    "Documents": (".pdf", ".docx", ".txt"),
    "Audio": (".mp3", ".wav"),
    "Miscellaneous": (),
}

for name in categories:
    os.makedirs(os.path.join(base, name), exist_ok=True)

script_path = os.path.abspath(__file__) if "__file__" in globals() else None

def move_file(src_path, dest_dir):
    try:
        filename = os.path.basename(src_path)
        target = os.path.join(dest_dir, filename)
        if os.path.exists(target):
            name, ext = os.path.splitext(filename)
            i = 1
            while True:
                new_name = f"{name} ({i}){ext}"
                new_target = os.path.join(dest_dir, new_name)
                if not os.path.exists(new_target):
                    target = new_target
                    break
                i += 1
        shutil.move(src_path, target)
    except Exception as e:
        print(f"Failed to move {src_path!r}: {e}")

for entry in os.listdir(base):
    path = os.path.join(base, entry)
    if not os.path.isfile(path):
        continue
    if script_path and os.path.abspath(path) == script_path:
        continue
    ext = os.path.splitext(entry)[1].lower()
    for name, exts in categories.items():
        if exts and ext in exts:
            move_file(path, os.path.join(base, name))
            break
    else:
        move_file(path, os.path.join(base, "Miscellaneous"))