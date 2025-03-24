import subprocess
import time
import webbrowser

# Define the backend server command
BACKEND_COMMAND = ["uvicorn", "api.main:app", "--host", "127.0.0.1", "--port", "8000", "--reload"]

def run_backend():
    """Start the FastAPI backend server."""
    print("Starting FastAPI backend...")
    backend_process = subprocess.Popen(BACKEND_COMMAND)
    time.sleep(3)  # Wait for server to start
    return backend_process

def open_frontend():
    """Open the frontend in a web browser."""
    frontend_url = "http://127.0.0.1:8000"
    print(f"Opening frontend at {frontend_url} ...")
    webbrowser.open(frontend_url)

if __name__ == "__main__":
    backend_process = run_backend()
    open_frontend()

    try:
        backend_process.wait()
    except KeyboardInterrupt:
        print("Shutting down backend server...")
        backend_process.terminate()
