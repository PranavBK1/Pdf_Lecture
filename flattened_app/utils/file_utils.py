import os
from pathlib import Path

def save_temp_file(uploaded_file, out_dir: Path) -> str:
    out_path = out_dir / uploaded_file.name
    with open(out_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return str(out_path)
