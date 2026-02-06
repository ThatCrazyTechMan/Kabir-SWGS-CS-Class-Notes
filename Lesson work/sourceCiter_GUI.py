import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
import pyperclip


class CitationGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Citation Generator")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        # Create main frame with padding
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Title
        title_label = ttk.Label(main_frame, text="Citation Generator", font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Is Current checkbox
        self.is_current_var = tk.BooleanVar(value=True)
        is_current_check = ttk.Checkbutton(main_frame, text="Is the article current?",
                                           variable=self.is_current_var)
        is_current_check.grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=(0, 15))

        # Author
        ttk.Label(main_frame, text="Author:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.author_entry = ttk.Entry(main_frame, width=40)
        self.author_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # Date Written
        ttk.Label(main_frame, text="Date Written (DD/MM/YYYY):").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.date_entry = ttk.Entry(main_frame, width=40)
        self.date_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # Title
        ttk.Label(main_frame, text="Title:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.title_entry = ttk.Entry(main_frame, width=40)
        self.title_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # Organisation
        ttk.Label(main_frame, text="Organisation:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.org_entry = ttk.Entry(main_frame, width=40)
        self.org_entry.grid(row=5, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # URL
        ttk.Label(main_frame, text="URL:").grid(row=6, column=0, sticky=tk.W, pady=5)
        self.url_entry = ttk.Entry(main_frame, width=40)
        self.url_entry.grid(row=6, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))

        # Generate button
        generate_btn = ttk.Button(main_frame, text="Generate Citation", command=self.generate_citation)
        generate_btn.grid(row=7, column=0, columnspan=2, pady=20)

        # Output text box
        ttk.Label(main_frame, text="Generated Citation:").grid(row=8, column=0, columnspan=2, sticky=tk.W, pady=(5, 5))
        self.output_text = tk.Text(main_frame, height=5, width=60, wrap=tk.WORD)
        self.output_text.grid(row=9, column=0, columnspan=2, pady=(0, 10))

        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)

    def generate_citation(self):
        if not self.is_current_var.get():
            messagebox.showinfo("Info", "Please check 'Is the article current?' to generate a citation.")
            return

        # Get values
        author = self.author_entry.get().strip()
        date_written = self.date_entry.get().strip()
        title = self.title_entry.get().strip()
        organisation = self.org_entry.get().strip()
        url = self.url_entry.get().strip()

        # Validate inputs
        if not all([author, date_written, title, organisation, url]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Extract year
        try:
            year_written = date_written[-4:]
            if not year_written.isdigit():
                raise ValueError
        except:
            messagebox.showerror("Error", "Invalid date format. Please use DD/MM/YYYY.")
            return

        # Get today's date
        today = date.today().strftime("%d/%m/%Y")

        # Generate citation
        citation = f"{author} ({year_written}) '{title}', {organisation}, ({date_written}) [Online] Available at: {url} (Accessed: {today})"

        # Display citation
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(1.0, citation)

        # Copy to clipboard
        try:
            pyperclip.copy(citation)
            messagebox.showinfo("Success", "Citation generated and copied to clipboard!")
        except:
            messagebox.showinfo("Success", "Citation generated! (Clipboard copy failed)")


if __name__ == "__main__":
    root = tk.Tk()
    app = CitationGeneratorGUI(root)
    root.mainloop()