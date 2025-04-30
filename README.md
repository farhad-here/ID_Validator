# 🪪This is my Id validator web application
# 🆔 Iranian National ID Validator

A simple Python project to validate Iranian National Identification Numbers based on the official checksum algorithm. This project is implemented using **Object-Oriented Programming (OOP)** principles.

---

## ✅ Features

- Checks if the entered National ID is exactly 10 digits
- Ensures the input contains only numeric characters
- Rejects invalid IDs with all identical digits (e.g., `1111111111`)
- Implements the official **checksum algorithm** used for validation
- Clean and readable structure using **Python classes**

---

## 📦 Requirements

- Python 3.x

All libraries used are from Python’s standard library, so no additional packages are required.

---

## 🔢 Validation Algorithm

1. The ID must be a **10-digit number**.
2. All digits **cannot be the same**.
3. Compute the **checksum** as follows:
checksum = (10×digit1 + 9×digit2 + ... + 2×digit9) % 11

4. Then:
- If `checksum < 2`, it must be equal to the **10th digit**.
- If `checksum >= 2`, then `10th digit = 11 - checksum`.

---

## 🎨UI

![validid1](https://github.com/user-attachments/assets/35f27482-860a-4fb5-8eb5-e21c6645f01a)


## 👨‍💻Used Technologies
- streamlit
- python
