import tkinter.filedialog

from PIL import Image as i, ImageDraw,  ImageFont
import tkinter as tk
from tkinter import filedialog as fd

# Tkinter window
screen = tk.Tk()
screen.title("Watermarker")
screen.minsize(width=100, height=100)
screen.config(pady=20, padx=20)


# Function for button to make watermark on your own and add it on image.
def watermarked():
    filetypes = (
        ('image', '*.png'),
        ('image', '*.jpeg')
    )
    filename = fd.askopenfilename(title='Open a file',
                                  initialdir='/',
                                  filetypes=filetypes)
    if filename:
        im1 = i.open(filename).convert("RGBA")
        width, height = im1.size
        watermark = text.get()
        font = ImageFont.truetype("arial.ttf", 40)
        draw = ImageDraw.Draw(im1, "RGBA")
        # making sure that watermark will be placed in the bottom-right corner
        textwidth, textheight = draw.textsize(watermark, font)
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin
        # add watermark
        draw.text((x, y), watermark, font=font, fill=(0, 0, 0, 0))
        # save the image with watermark
        im1.convert("RGB")
        im1.save(filename)
        # tells that operation is succeeded and location of the file.
        label = tk.Label(text=f"Image watermarked!\n location: {filename}", font=("Arial", 10, "bold"), fg="green")
        label.grid(column=1, row=1, sticky="N")


# tkinter objects
button = tk.Button(screen, text=" Take image", command=watermarked)
button.grid(column=0, row=2)
text = tk.Entry(width=20)
text.grid(column=0, row=1)
write = tk.Label(text="Write down your watermark: ")
write.grid(column=0, row=0)

if __name__ == "__main__":
    screen.mainloop()
