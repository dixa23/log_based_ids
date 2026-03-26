# 🔐 Log-Based Intrusion Detection System (IDS)

## 📌 Overview
This project is a Python-based Intrusion Detection System that analyzes Linux authentication logs (`auth.log`) to detect brute-force attacks.

It identifies suspicious IP addresses by counting repeated failed login attempts and generates structured alerts.

---

## 🚀 Features
- Detects brute-force login attempts
- Extracts IP addresses using Regex
- Counts failed login attempts per IP
- Generates alerts when threshold is exceeded
- Outputs alerts in JSON format (SIEM-style)

---

## 🛠️ Technologies Used
- Python
- Regex
- Linux (WSL)
- JSON

---

## 📂 Project Structure 


---

## ⚙️ How It Works
1. Reads `auth.log`
2. Filters "Failed password" entries
3. Extracts IP addresses
4. Counts attempts per IP
5. Generates alert if attempts exceed threshold

---

## ▶️ How to Run

```bash
python3 detector.py
