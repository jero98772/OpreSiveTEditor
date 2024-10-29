from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import subprocess
import os
from pathlib import Path
import json

app = FastAPI()

# Serve static files (if needed)
#app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("templates/index.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.get("/tree")
def get_file_tree(path: str = None):
    def walk_directory(path):
        tree = []
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                tree.append({"name": entry, "type": "directory", "path": full_path, "children": []})
            else:
                tree.append({"name": entry, "type": "file", "path": full_path})
        return tree

    # If no path is specified, use the user's home directory
    path = path or str(Path.home())
    return JSONResponse(content=walk_directory(path))

@app.post("/execute")
async def execute_code(code: str):
    try:
        out = ""
        code_lines = code.split("\n")
        for line in code_lines:
            # Simulating the REP function; replace with actual logic
            print(line)  # For debugging purposes, replace with actual logic
            out += f"Executed: {line}\n"  # Placeholder for the actual execution logic
        
        return {"output": out, "error": ""}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail=f"Execution Error: {str(e)}")

@app.get("/load-file")
async def load_file(file_path: str):
    try:
        with open(file_path, "r") as f:
            content = f.read()

        # Infer syntax mode from file extension
        extension = Path(file_path).suffix
        language_map = {
            ".py": "python",
            ".js": "javascript",
            ".html": "htmlmixed",
            ".css": "css",
            ".json": "application/json",
            ".java": "text/x-java",
            ".cpp": "text/x-c++src",
            ".c": "text/x-csrc",
            ".md": "markdown",
            ".xml": "xml",
            ".rb": "ruby",
            ".sh": "shell",
            # Add more mappings as needed
        }
        mode = language_map.get(extension, "plaintext")  # Default to plain text if unknown

        return {"content": content, "mode": mode,"file_path":file_path}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/save-file/")
async def save_file(request: Request):
    try:
        # Read the JSON body directly
        data = await request.json()
        
        # Extract file_path and content
        file_path = data.get("file_path")
        content = data.get("content")

        # Ensure both fields are provided
        if not file_path or not content:
            raise HTTPException(status_code=400, detail="file_path and content are required")

        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Write content to the specified file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return {"message": "File saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to save file") from e