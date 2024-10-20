import asyncio
import tkinter as tk
from tkinter import scrolledtext
from websockets.sync.client import connect

def run_websocket_client(output_text):
    dropped_count = 0
    total_requests = 10000
    
    output_text.insert(tk.END, "Starting WebSocket client...\n")
    with connect("ws://localhost:8765") as websocket:
        for i in range(1, total_requests + 1):
            try:
                message = f"Request [{i}] Hello world!"
                websocket.send(message)
                response = websocket.recv()
                output_text.insert(tk.END, f"Received: {response}\n")
                output_text.see(tk.END)
            except Exception as e:
                dropped_count += 1
                output_text.insert(tk.END, f"Error occurred: {e}\n")
                output_text.see(tk.END)

    output_text.insert(tk.END, f"Total dropped messages: {dropped_count}\n")

def create_ui():
    root = tk.Tk()
    root.title("WebSocket Client")
    output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
    output_text.pack(padx=10, pady=10)
    start_button = tk.Button(root, text="Start Client", command=lambda: run_websocket_client(output_text))
    start_button.pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    create_ui()
