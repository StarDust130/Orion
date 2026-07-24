# 🚀 Backend Setup

## 📦 1. Create a Virtual Environment

```bash
python -m venv .venv
```

---

## ⚡ 2. Activate the Virtual Environment

### 🪟 Windows (Git Bash)

```bash
source .venv/Scripts/activate
```

### 🪟 Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

### 🍎 macOS / 🐧 Linux

```bash
source .venv/bin/activate
```

---

## 📥 3. Install Dependencies

```bash
python -m pip install fastapi uvicorn groq python-dotenv pydantic httpx
```

---

## 📝 4. Save Dependencies

```bash
python -m pip freeze > requirements.txt
```

---

## ✅ 5. Verify Installation

```bash
python --version
python -m pip --version
which python
which pip
```

Expected output:

* ✅ `which python` → `.venv/.../python`
* ✅ `which pip` → `.venv/.../pip`

If both commands point to **`.venv`**, your backend is ready to go. 🚀
