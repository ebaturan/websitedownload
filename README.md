# How to Use the Website Download Script

This document provides step-by-step instructions on how to use the Python script for downloading a website's files and directories to your local machine and optionally uploading them to a remote network folder.

## Prerequisites

1. **Python Installation**:
   - Ensure Python 3.x is installed on your system.
   - Install the required libraries using the following command:
     ```bash
     pip install requests beautifulsoup4
     ```

2. **Permissions**:
   - Ensure you have permission to download content from the website.
   - For remote uploads, ensure you have write access to the SMB network folder.

---

## Script Features

1. Downloads all files and directories recursively from a specified URL.
2. Saves the directory structure locally on your machine.
3. Logs successful and failed downloads in a log file.
4. Retries failed downloads up to 3 times.
5. Optionally uploads the downloaded content to a remote SMB network folder.
6. Automatically resumes from failed downloads using the log file.

---

## Steps to Use the Script

### 1. Running the Script

- Save the script as `download_website.py` on your local machine.
- Open a terminal or command prompt and navigate to the directory containing the script.
- Run the script using the following command:
  ```bash
  python download_website.py
  ```

### 2. Input Parameters

When you run the script, it will prompt you for the following inputs:

1. **Base URL**:
   - Enter the URL of the website you want to download.
   - Example: `https://example.com`

2. **Output Folder**:
   - Enter the local folder path where you want to save the downloaded files.
   - Example: `C:\Users\YourUsername\Downloads\Website`

3. **Remote SMB Folder** (Optional):
   - Enter the path to the SMB network folder where the files will be uploaded after downloading.
   - Example: `\\network\shared-folder`
   - Leave this blank if you do not want to upload the files.

### 3. Log File

- The script generates a log file named `download_log.txt` in the specified output folder.
- **Log Format**:
  - `SUCCESS: <url>` indicates a successful download.
  - `FAILED: <url>` indicates a failed download.

### 4. Automatic Retry

- The script will retry failed downloads up to 3 times.
- On subsequent runs, it reads the log file and resumes downloading any failed files.

---

## Post-Download Operations

### Upload to Remote Folder

- If you provided a remote SMB folder path, the script will automatically copy the downloaded files to the specified location.
- Ensure the remote folder is accessible and writable from your machine.

### Graceful Exit

- The script automatically exits after completing the download and upload processes.

---

## Troubleshooting

1. **Failed Downloads**:
   - Check the `download_log.txt` file for failed URLs.
   - Ensure the URLs are accessible and the server allows downloading.

2. **Remote Upload Errors**:
   - Verify the SMB folder path and ensure you have the necessary permissions.

3. **Script Errors**:
   - If the script encounters issues, ensure the required Python libraries are installed.
   - Check for typos or syntax errors in the script.

---

## Example Usage

### Input Example:

- Base URL: `https://example.com`
- Output Folder: `C:\Users\YourUsername\Downloads\Website`
- Remote SMB Folder: `\\network\shared-folder`

### Output:

- Local files saved in `C:\Users\YourUsername\Downloads\Website`
- Log file created: `C:\Users\YourUsername\Downloads\Website\download_log.txt`
- Files uploaded to `\\network\shared-folder` (if specified).

---

Feel free to modify the script to suit your needs or contact support if you encounter any issues.

Eba Turan  2024 developer 
