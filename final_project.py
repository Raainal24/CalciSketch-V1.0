
from pathlib import Path
from tkinter import Tk, Canvas, Button, colorchooser, Scale, Label, HORIZONTAL
from PIL import Image, ImageGrab
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import google.generativeai as genai
import tempfile
import os

api_key = "AIzaSyCLMQuQich4jg7c4FzGx8OfIuUWU9KakHk"  # Replace with your actual API key
genai.configure(api_key=api_key)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\\Studies\\Mini Project 3\\Final codes\\assets\\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


root = Tk()

root.geometry("1920x1080")
root.configure(bg = "#FFFFFF")

brush_color = "black"
brush_size = 5
eraser_on = False
last_x = None
last_y = None


canvas = Canvas(
    root,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

def paint(event):
    global last_x, last_y, brush_color, brush_size, eraser_on
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    color = "white" if eraser_on else brush_color
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)
    last_x, last_y = event.x, event.y
    
    



def change_color(new_color):
    global brush_color
    brush_color = new_color

def reset(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y
    
def save_text():
   
    recognized_text = recognized_text.replace(" ", "").replace("\n", "")
    recognized_text = recognized_text.replace('X', '*').replace('x', '*')

def change_size(value):
    global brush_size
    brush_size = int(value)

def use_brush():
    global eraser_on
    eraser_on = False

def use_eraser():
    global eraser_on
    eraser_on = True

def clear_canvas():
    canvas.delete("all")

def evaluate_expression():
    global last_x, last_y
    # Capture the canvas as an image
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    # Capture canvas area to image
    image = ImageGrab.grab().crop((x, y, x1, y1))

    # Save the image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        image.save(temp_file.name)
        temp_image_path = temp_file.name

    # Configure generation settings for Google Gemini API
    generation_config = {
        "temperature": 0.2,
        "top_p": 0.8,
        "top_k": 64,
        "max_output_tokens": 8192,
    }

    try:
        # Create model with generation configuration
        model = genai.GenerativeModel(
            model_name="gemini-1.5-pro",
            generation_config=generation_config,
        )

        # Upload the temporary image file for recognition and evaluation
        prompt = [
            genai.upload_file(temp_image_path),
            "Please evaluate the expression drawn on this image and provide only the answer."
        ]

        # Generate response with Google Gemini API
        response = model.generate_content(prompt)

        # Display the result on the canvas
        if response and response.text:
            result = response.text
            if last_x is not None and last_y is not None:
                eq_pos_x = last_x + 300  # Adjust X position to be beside "="
                eq_pos_y = last_y  # Keep Y position the same
                canvas.create_text(eq_pos_x, eq_pos_y, text=f"{result}", fill="black", font=("Helvetica", 48, "bold"))
        else:
            print("Failed to get a valid response from Gemini.")
    except Exception as e:
        print(f"Error during API call: {e}")
    finally:
        # Clean up the temporary file
        os.remove(temp_image_path)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    960.0,
    540.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=190.0,
    y=906.0,
    width=1540.0,
    height=123.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_color("red"),
    relief="flat"
)
button_2.place(
    x=224.0,
    y=936.0,
    width=63.0,
    height=63.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_color("yellow"),
    relief="flat"
)
button_3.place(
    x=288.0,
    y=937.0,
    width=63.0,
    height=63.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_color("yellow"),
    relief="flat"
)
button_4.place(
    x=353.0,
    y=937.0,
    width=63.0,
    height=63.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_color("blue"),
    relief="flat"
)
button_5.place(
    x=417.0,
    y=937.0,
    width=63.0,
    height=63.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_color("white"),
    relief="flat"
)
button_6.place(
    x=481.0,
    y=937.0,
    width=63.0,
    height=63.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_color("black"),
    relief="flat"
)
button_7.place(
    x=545.0,
    y=937.0,
    width=63.0,
    height=63.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=use_eraser,
    relief="flat"
)
button_8.place(
    x=883.0,
    y=928.0,
    width=83.0,
    height=83.0
)

button_image_9 = PhotoImage(


    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=use_brush,
    relief="flat"
)
button_9.place(
    x=749.0,
    y=934.0,
    width=69.0,
    height=69.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=evaluate_expression,
    relief="flat"
)
button_10.place(
    x=1517.0,
    y=920.0,
    width=97.0,
    height=97.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=clear_canvas,
    relief="flat"
)
button_11.place(
    x=1414.0,
    y=938.0,
    width=68.0,
    height=68.0
)

size_slider = Scale( from_=1, to=10, orient=HORIZONTAL, command=change_size)
size_slider.set(brush_size)
size_slider.place(x=1060,y=938.0,width=300,
    height=50)

canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", reset)

root.resizable(False, False)
root.mainloop()
