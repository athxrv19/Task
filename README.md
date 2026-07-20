🔍 Duplicate File Finder

A lightweight, production-ready Python utility designed to recursively scan directories, identify duplicate files via secure cryptographic hashing, and calculate recoverable disk real estate instantly. 

---

## ✨ Key Features

* **Recursive Deep Scan:** Traverses complex folder structures seamlessly using Python's object-oriented `pathlib` framework.
* **Low Memory Footprint:** Streams files incrementally in fixed **8 KB chunks**—safely handling multi-gigabyte files without memory spikes.
* **Content-Based Verification:** Identifies duplication strictly by data signature (SHA-1) rather than fragile metrics like file name, extension, or timestamp.
* **Human-Readable Reporting:** Generates a structured terminal breakdown grouping exact duplicates together, tracking isolated overhead, and presenting total savings in both Megabytes (MB) and bytes.

---

## ⚙️ How It Works

```mermaid
graph TD
    A[Start: User Enters Path] --> B[Recursively Walk Directory]
    B --> C{Is Item a File?}
    C -- No --> B
    C -- Yes --> D[Read File in 8KB Chunks]
    D --> E[Compute SHA-1 Cryptographic Hash]
    E --> F[Group File Path under Hash Key]
    F --> G[Analyze Dictionary Values]
    G --> H{Hash Has > 1 File?}
    H -- No --> I[Skip: File is Unique]
    H -- Yes --> J[Print Duplicate Paths & Calculate Recoverable Space]
    J --> K[Output Final Cumulative MB Savings Summary]
