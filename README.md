# 🐍 Python Projects Collection

A collection of Python-based mini projects built for learning, experimenting, and fun. Each project is self-contained and demonstrates useful concepts and libraries in Python.

## 📁 Projects Included

### 1. 📧 Bulk Email Sender (Gmail API)
Send personalized bulk emails using Gmail and an **App Password** (for accounts with 2FA enabled).
- Reads recipient emails from a file.
- Sends formatted emails using `smtplib`.
- Secure authentication via app passwords.

> **Note:** Never expose your app password or email credentials in code. Use `.env` files or environment variables.

---

### 2. 🎮 Hangman Game
A classic command-line **Hangman** game.
- Random word selection from a word list.
- User-friendly text interface.
- Keeps track of guesses and remaining tries.

---

### 3. 📱 QR Code Generator
Easily generate QR codes for links, messages, or any text.
- Built with the `qrcode` library.
- Saves generated QR codes as image files.
- Can be extended for dynamic content or batch generation.

---

### 4. 🟩 Wordle Game (Terminal-based)
A clone of the popular **Wordle** game, playable in the terminal.
- 5-letter word guessing with feedback.
- Colored hints using ANSI escape codes.
- Customizable word list.

---

## 🛠 Requirements

Make sure Python 3.7+ is installed.

Install project dependencies:

```bash
pip install -r requirements.txt
