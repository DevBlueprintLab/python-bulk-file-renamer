# 📝 Python Bulk File Renamer

![Python Version](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-pathlib%20%7C%20sys-orange)
![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

A Python CLI automation tool that renames multiple files in a directory using a consistent naming pattern while preserving original file extensions.

The program processes files safely by validating inputs, applying sequential naming, and ensuring no overwriting or conflicts occur during execution.

---

## 🖥️ Pipeline Lifecycle & Live Demo

### Ingestion ➔ Processing ➔ Output

<p align="center">
  <img src="images/before.png" width="380" alt="Original File State" />
  <img src="images/terminal.png" width="380" alt="CLI Execution Process" />
</p>

<p align="center">
  <img src="images/after.png" width="765" alt="Renamed Files Output" />
</p>

---

## 🧠 Core Features & Architecture

* 📝 **Batch File Renaming:** Renames multiple files in a directory using a user-defined prefix.
* 🔢 **Sequential Indexing:** Applies automatic numbering with leading zeros (001, 002, 003…).
* 📂 **Extension Preservation:** Keeps original file types unchanged during renaming.
* 🚫 **Safe Processing:** Skips directories and hidden/system files to avoid unintended modifications.
* ⚠️ **Conflict Prevention:** Ensures no duplicate filenames are created during execution.
* 💬 **User Interaction:** Requires confirmation before applying changes.

---

## 🛠️ Tech Stack & Requirements

* **Core Language:** Python 3.x  
* **File Handling:** `pathlib`  
* **System Utilities:** `sys`  

---

## ⚡ Quick Start & Usage

### 1. Clone repository
```bash
git clone https://github.com/DevBlueprintLab/Python-Bulk-File-Renamer.git
cd Python-Bulk-File-Renamer
```
### 2. Run the tool
```bash
python Bulk-File-Renamer.py

```
### 3. Execution example
```bash
Enter folder path:
D:\RenameTest

Enter a prefix:
Holiday

Rename files (y/n)?
y

✓ Renamed:
IMG001.jpg → Holiday_001.jpg

✓ Renamed:
IMG002.jpg → Holiday_002.jpg

Finished!

Files renamed: 8
```
The script will safely rename all supported files while preserving their original extensions.


## 📁 Project Structure

```text
Python-Bulk-File-Renamer/
├── Bulk File Renamer.py       # Main automation script
├── README.md             # Project documentation
└── images/
    ├── before.png
    ├── terminal.png
    └── after.png
```

---

## 🔮 Roadmap & Future Improvements
 * Add suffix-based renaming support
 * Add preview mode before execution
 * Support metadata-based renaming (dates, timestamps)
 * Add undo functionality
 * GUI version for non-technical users
---

Created by **DevBlueprint Lab**
