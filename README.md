🚀 Quick Start
Prerequisites
Python 3.6+

No external dependencies or pip installs required. Uses purely native standard libraries (pathlib, hashlib).

Running the Utility
Save duplicate_finder.py to your working directory.

Launch your terminal and execute:

Bash
python duplicate_finder.py
Enter the target directory path when prompted:

Plaintext
Enter folder path: /Users/username/Downloads
📊 Sample Output
Plaintext
==================================================
Duplicate Files:
/Users/username/Downloads/Presentation_Final.pdf
/Users/username/Downloads/Archive/Backup_Pres.pdf
Recoverable: 12451840 bytes

==================================================
Duplicate Files:
/Users/username/Downloads/Photos/IMG_0492.RAW
/Users/username/Downloads/Photos/Duplicates/Copy_IMG_0492.RAW
/Users/username/Downloads/Export/Backup_IMG_0492.RAW
Recoverable: 50331648 bytes

==================================================
Total Recoverable Space: 59.87 MB (62783488 bytes)
🛠️ Implementation Details
Algorithm: SHA-1 (hashlib.sha1)

Chunk Optimization: 8192 bytes provides the optimal balance between I/O call frequency and memory page size matching.

Dictionary Structuring: Utilizes .setdefault(h, []) to build an automated, collision-free grouping engine.
