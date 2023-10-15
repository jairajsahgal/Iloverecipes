from PIL import Image, ImageTk

from tkinter import filedialog

import os

import tkinter as tk

from io import BytesIO

from recipes.models import Book, BookPage

from django.core.files.base import ContentFile

from OCR import perform_ocr


def compress_and_optimize_image(image_path):


    """

    C O M P R E S S I O N

    ───────────────

    This function takes an image file path as input, compresses and optimizes it as a JPEG with quality 20,

    and returns it as a ContentFile. This is used for reducing the size of images.

    ───────────────

    """

    img = Image.open(image_path)

    buffer = BytesIO()

    img.save(buffer, format='JPEG', quality=20, optimize=True)

    buffer.seek(0)

    return ContentFile(buffer.read(), name=os.path.basename(image_path))


def create_book():


    """

    C R E A T E    -|-   B O O K

    ───────────────

    This function opens a file dialog to select an image file (e.g., for a book cover). It extracts the base name

    of the file without the extension, compresses the image, and creates a new Book object in Django with the

    image as the cover. It returns the newly created book.

    ───────────────

    """

    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])



    if file_path:

        # Get the base name of the file without the extension

        file_name_without_extension = os.path.splitext(os.path.basename(file_path))[0]

        

        # Compress and optimize the image before using it

        compressed_image = compress_and_optimize_image(file_path)

        

        # Create a new book with the selected image

        new_book = Book(title=file_name_without_extension, year=2023)

        new_book.cover_photo = compressed_image

        new_book.save()

        

        return new_book  # Return the newly created book




def rip_pages(new_book):

    """

    R I P   -|-   P A G E S 

    ───────────────

    This function opens a folder dialog to select a folder with image files. It then checks if a Book object

    already exists in Django. If a book exists, it associates the selected images as BookPages with the existing

    book. If no book exists, it displays an error message.

    ───────────────

    """

    folder_path = filedialog.askdirectory(title="Select a folder with images")



    if folder_path:

        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

        



        if image_files:

            if new_book:

                # Use the newly created book to associate ripped pages

                for image_file in image_files:

                    image_path = os.path.join(folder_path, image_file)

                    #_.-._.-._ O C R _.-._.-._.-._.-._.-._.-.

                    ocr_result = perform_ocr(image_path)

                    print(ocr_result)

                    #_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.

                    file_name = os.path.splitext(image_file)[0]

                    # Compress and optimize the image

                    compressed_image = compress_and_optimize_image(image_path)

                    # Create a new page and associate it with the newly created book

                    new_page = BookPage(book=new_book, keywords=ocr_result)

                    new_page.page_photo = compressed_image

                    new_page.save()
                 

                    


            else:

                # Display an error message if book creation failed

                label.config(text="Book creation failed.", fg="red")

        else:

            label.config(text="No valid image files found in the selected folder.", fg="red")

    else:

        label.config(text="Please select a folder.", fg="red")

    label.config(text="Sweet! Now select another book if you want!")




def enable_rip_pages_button():

    """
    E N A B L E   -|-  R I P   -|-   P A G E S 

    Triggers the rip pages button to become usable.

    """
    print("Rip pages enables.. meow!")

    new_book = create_book()

    if new_book:

        # U P D A T E    -|-   M E S S A G E 

        label.config(text="Now select a file path/folder where your images are stored", fg="green")  # Clear any previous status message

        rip_pages_button.config(state=tk.NORMAL, command=lambda: rip_pages(new_book))


"""
T K I N T E R    -|-   G U I

   Here is where the tkinter gui gets created.
   We create the frame with bg color #fofofof
   we create our two buttons and pack them in the frame.

"""

root = tk.Tk()

root.title("Book Creator")

frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)

label = tk.Label(frame, text="Select an image for the book cover:", width=30, wraplength=200)


create_button = tk.Button(frame, text="Select Book Cover", bg="#28a745", fg="white", command=create_book)

rip_pages_button = tk.Button(frame, text="Select Folder for Pages", bg="#dc3545", fg="white", state=tk.DISABLED)


frame.pack(expand=True, fill="both")

label.pack(pady=(0, 10))

create_button.pack(fill="x", pady=(0, 10))

rip_pages_button.pack(fill="x", pady=(0, 10))


# enables rip pages
create_button.config(command=enable_rip_pages_button)



root.mainloop()