# Smart Email Extractor 📧

A GUI-based Python application that automatically extracts email addresses from text files using Regular Expressions (Regex). The extracted emails are displayed in the application window and saved to a separate text file for easy access.

## 🚀 Features

* Select any text file (.txt)
* Automatically extract all email addresses
* Display extracted emails in the GUI
* Count total emails found
* Save extracted emails to a new file
* User-friendly interface using Tkinter

## 🛠️ Technologies Used

* Python 3
* Tkinter
* Regular Expressions (Regex)
* File Handling

## 📂 Project Structure

```text
CodeAlpha_EmailExtractor/
│
├── email_extractor.py
├── sample.txt
├── extracted_emails.txt
├── README.md
└── screenshots/
    ├── home.png
    ├── extraction_result.png
    └── output_file.png
```

## ▶️ How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python email_extractor.py
```

## 📋 How It Works

1. Click the **Select Text File** button.
2. Choose a `.txt` file containing email addresses.
3. The application scans the file using Regex.
4. All detected email addresses are displayed on the screen.
5. Extracted emails are automatically saved to `extracted_emails.txt`.

## 📄 Sample Input

```text
Contact us at support@gmail.com
admin@company.in
hr.department@yahoo.com
```

## 📤 Sample Output

```text
support@gmail.com
admin@company.in
hr.department@yahoo.com
```


## 📚 Concepts Used

* GUI Programming
* File Handling
* Regular Expressions (Regex)
* Error Handling
* Python Functions

## 🎯 Learning Outcomes

This project demonstrates how automation can be used to extract useful information from text files efficiently. It provides practical experience with Python GUI development, file operations, and pattern matching.

## 👨‍💻 Author

Kartik Gupta

## 🏆 Internship Project

Developed as part of the CodeAlpha Python Programming Internship Program.
