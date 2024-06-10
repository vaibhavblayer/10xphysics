import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfFileReader

class PhysicsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Physics App")
        self.chapters = []

        # Load the chapters from the database
        self.load_chapters()

        # Create the UI
        self.create_ui()

    def load_chapters(self):
        # Load the chapters from the database
        # For simplicity, we'll use a list of tuples
        self.chapters = [
            ("Chapter 1: Introduction", "chapter1.pdf"),
            ("Chapter 2: Kinematics", "chapter2.pdf"),
            # Add more chapters here
        ]

    def create_ui(self):
        # Create the main frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)

        # Create the listbox to display the chapters
        self.listbox = tk.Listbox(main_frame)
        self.listbox.pack(side="left", fill="both", expand=True)

        # Create the button to view the PDF
        view_button = tk.Button(main_frame, text="View PDF", command=self.view_pdf)
        view_button.pack(side="right", fill="x")

        # Add the chapters to the listbox
        for chapter in self.chapters:
            self.listbox.insert(tk.END, chapter[0])

    def view_pdf(self):
        # Get the selected chapter
        selected_index = self.listbox.curselection()[0]
        selected_chapter = self.chapters[selected_index][0]

        # Load the PDF
        pdf_file = open(self.chapters[selected_index][1], "rb")
        pdf = PdfFileReader(pdf_file)

        # Display the PDF
        pdf_window = tk.Toplevel(self.root)
        pdf_window.title(selected_chapter)
        pdf_window.geometry("800x600")

        # Create a text widget to display the PDF
        text_widget = tk.Text(pdf_window, width=80, height=50)
        text_widget.pack(fill="both", expand=True)

        # Read the PDF and display it in the text widget
        for page in range(pdf.numPages):
            page_obj = pdf.getPage(page)
            text_widget.insert(tk.END, page_obj.extractText())

        pdf_file.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = PhysicsApp(root)
    root.mainloop()
