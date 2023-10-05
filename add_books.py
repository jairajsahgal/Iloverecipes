from PIL import Image, ImageTk

from tkinter import filedialog

import os

import tkinter as tk

from io import BytesIO

from recipes.models import Book, BookPage

from django.core.files.base import ContentFile



def compress_and_optimize_image(image_path):

    img = Image.open(image_path)

    buffer = BytesIO()

    img.save(buffer, format='JPEG', quality=20, optimize=True)

    buffer.seek(0)

    return ContentFile(buffer.read(), name=os.path.basename(image_path))



def create_book():

    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])

    if file_path:

        # Compress and optimize the image before using it

        compressed_image = compress_and_optimize_image(file_path)
        new_book = Book(title="Your Book Title", year=2023)  # You can set the title and year as needed
        new_book.cover_photo = compressed_image
        new_book.save()



        # Update the UI with a success message or further actions if needed



def rip_pages():

    folder_path = filedialog.askdirectory(title="Select a folder with images")

    if folder_path:

        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]



        if image_files:

            # Check if a book already exists

            existing_book = Book.objects.first()



            if existing_book:

                # Use the existing book to associate ripped pages

                for image_file in image_files:

                    image_path = os.path.join(folder_path, image_file)

                    file_name = os.path.splitext(image_file)[0]



                    # Compress and optimize the image before using it

                    compressed_image = compress_and_optimize_image(image_path)



                    # Create a new page and associate it with the existing book

                    new_page = BookPage(book=existing_book, keywords="Page Keywords")  # Customize keywords as needed

                    new_page.page_photo = compressed_image

                    new_page.save()

                    

                # Update the UI with a success message or further actions if needed

            else:

                # Display an error message if no book exists

                status_label.config(text="Please create a book before ripping pages.", fg="red")

        else:

            status_label.config(text="No valid image files found in the selected folder.", fg="red")

    else:

        status_label.config(text="Please select a folder.", fg="red")



# Create your Tkinter GUI

root = tk.Tk()

root.title("Book Creator")



frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)

label = tk.Label(frame, text="Select an image for the book cover:")



create_button = tk.Button(frame, text="Create Book", bg="#28a745", fg="white", command=create_book)

rip_pages_button = tk.Button(frame, text="Rip Pages", bg="#dc3545", fg="white", command=rip_pages)

status_label = tk.Label(frame, text="", fg="green")



frame.pack(expand=True, fill="both")

label.pack(pady=(0, 10))

create_button.pack(fill="x", pady=(0, 10))

rip_pages_button.pack(fill="x", pady=(0, 10))

status_label.pack()



root.mainloop()

