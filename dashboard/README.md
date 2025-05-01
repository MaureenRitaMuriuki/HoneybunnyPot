# HoneybunnyPot 🍯

A simple honeypot built with Python and Flask to monitor incoming connections and visualize attack logs via a web dashboard.

## Features
- Custom TCP honeypot
- Logs attack attempts
- Dashboard to view logs
- Written in Python3

## Usage
1. Run the honeypot:
   ```bash
   python3 src/honeybunny.py
2. In a new terminal, start the dashboard:

bash
Copy
Edit
python3 dashboard/app.py
3. 
---

### **🌐 Step 3: Create a GitHub repo**

1. Go to [https://github.com/new](https://github.com/new)
2. Name it something like `HoneybunnyPot`
3. Leave it **empty** (no README, .gitignore, etc.)

---

### **📤 Step 4: Push Code to GitHub**

In your `HoneybunnyPot` directory:
```bash
git init
git add .
git commit -m "Initial commit: Add honeypot and dashboard"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/HoneybunnyPot.git
git push -u origin main
Visit http://127.0.0.1:5000 to view logs
