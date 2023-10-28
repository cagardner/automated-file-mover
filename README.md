File Automation System Summary

**Goal**: Automatically organize files in the "Downloads" folder based on their file type.

**Libraries Used**:
- `watchdog` (install via `!pip install watchdog`)

**How it Works**:
1. The project sets up an observer to monitor the "Downloads" folder for any new files added.
2. If any files are already present in the "Downloads" folder when the script starts, they are immediately organized.
3. For each file, it determines the file's type based on its extension (e.g., `.pdf` becomes `PDF`).
4. If a sub-folder for that file type doesn't exist, the script creates one (e.g., a folder named "PDF" for `.pdf` files).
5. The file is then moved into the appropriate sub-folder.
6. If the file doesn't have a recognizable extension, it's placed in a folder named "OTHERS".
7. The script runs continuously, watching for new files and organizing them immediately upon detection.
8. The user can stop the script manually, which also stops the file monitoring.

