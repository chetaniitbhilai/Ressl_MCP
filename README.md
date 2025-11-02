# ✅ MCP Server – Keyword Search Tool (Case-Insensitive)

This project is a simple **MCP (Model Context Protocol) Server** built using FastAPI.
It includes a tool that allows users to **search for a keyword inside a file** (case-insensitive).

---

## 📁 Project Structure

```
mcp-server/
├── server.py
├── tools/
│   ├── __init__.py
│   └── search_tool.py
├── requirements.txt
└── README.md
```

---

## ⚙️ 1. Setup Instructions

### ✅ Step 1: Clone or Create Project Folder

```bash
cd mcp-server
```

### ✅ Step 2: Create and Activate Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
# Activate it:
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

### ✅ Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 2. Run the MCP Server

```bash
uvicorn server:app --reload --port 8000
```

If successful, you will see:

```
Uvicorn running on http://127.0.0.1:8000
```

Visit in browser:

```
http://127.0.0.1:8000
```

Or API docs (auto-generated):

```
http://127.0.0.1:8000/docs
```

---

## 🔍 3. Search Keyword in a File (API Usage)

### ✅ Request Format (POST `/search`)

```json
{
  "file_path": "path/to/file.txt",
  "keyword": "example"
}
```

### ✅ Example using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/search" \
-H "Content-Type: application/json" \
-d '{"file_path": "sample.txt", "keyword": "hello"}'
```

### ✅ Example Response:

```json
{
  "results": [
    "Line 2: Hello World",
    "Line 5: hElLo again"
  ]
}
```

---

## 🛠 4. Code Summary


### `server.py`

Defines API endpoint `/search`.

---

## ✅ 5. Features

✔ FastAPI-powered MCP server
✔ Case-insensitive keyword search
✔ Shows line number + text where keyword exists
✔ Error handling for missing files

---

## 📌 6. Future Improvements (Optional)

* 🔹 Search across directories
* 🔹 Regex support
* 🔹 Return JSON with `{line_number, content}` format
* 🔹 File type filtering (.txt, .py, .md, etc.)

