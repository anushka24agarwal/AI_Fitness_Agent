from fpdf import FPDF
import tempfile

class PDF(FPDF):
    def __init__(self, title="Plan"):
        super().__init__()
        self.title = title

    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "AI Fitness and Diet Planner", ln=1, align="C")

    def add_table(self, data):
        # Extract headers
        headers = list(data[0].keys())

        # Set font and column widths
        self.set_font("Arial", "B", 12)
        col_widths = [40, 60, 40, 50]  # Adjust based on your table structure

        # Header row
        self.set_fill_color(200, 220, 255)
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, border=1, align='C', fill=True)
        self.ln()

        # Set font for data rows
        self.set_font("Arial", "", 11)

        for row in data:
            y_start = self.get_y()
            x_start = self.get_x()
            max_height = 0

            # Calculate height needed for each cell
            heights = []
            for i, key in enumerate(headers):
                txt = str(row.get(key, ""))
                num_lines = len(self.multi_cell(col_widths[i], 6, txt, border=0, align='L', split_only=True))
                heights.append(num_lines * 6)
            max_height = max(heights)

            # Draw cells
            for i, key in enumerate(headers):
                self.set_xy(x_start + sum(col_widths[:i]), y_start)
                txt = str(row.get(key, ""))
                self.multi_cell(col_widths[i], 6, txt, border=1, align='L')

            self.ln(max_height)
        if not data:
            return

        # Extract headers
        headers = list(data[0].keys())

        # Set font and column widths
        self.set_font("Arial", "B", 12)
        col_widths = [40, 60, 40, 50]  # Adjust based on your table structure

        # Header row
        self.set_fill_color(200, 220, 255)
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, border=1, align='C', fill=True)
        self.ln()

        # Set font for data rows
        self.set_font("Arial", "", 11)

        for row in data:
            y_start = self.get_y()
            x_start = self.get_x()
            max_height = 0

            # Calculate height needed for each cell
            heights = []
            for i, key in enumerate(headers):
                txt = str(row.get(key, ""))
                num_lines = len(self.multi_cell(col_widths[i], 6, txt, border=0, align='L', split_only=True))
                heights.append(num_lines * 6)
            max_height = max(heights)

            # Draw cells
            for i, key in enumerate(headers):
                self.set_xy(x_start + sum(col_widths[:i]), y_start)
                txt = str(row.get(key, ""))
                self.multi_cell(col_widths[i], 6, txt, border=1, align='L')

            self.ln(max_height)

    def add_bullets(self, tips):
        if not tips:
            return

        self.ln(5)
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Tips:", ln=True)

        self.set_font("Arial", "", 11)
        for tip in tips:
            self.cell(5)  # left padding
            self.cell(0, 10, f"- {tip}", ln=True)


def generate_pdf(meal_plan_dict, title="Meal Plan"):
    pdf = PDF(title=title)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, title, ln=True, align="L")
    pdf.ln(10)

    pdf.add_table(meal_plan_dict.get("plan", []))
    pdf.add_bullets(meal_plan_dict.get("tips", []))

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        pdf.output(tmp.name)
        return tmp.name