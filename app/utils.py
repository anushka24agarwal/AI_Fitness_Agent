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
        if not data:
            return

        # Get headers
        headers = list(data[0].keys())

        # Estimate column widths based on max content length
        col_widths = []
        for header in headers:
            max_len = max(len(str(row.get(header, ""))) for row in data)
            col_width = max(len(header), max_len) * 2.5
            col_widths.append(min(col_width, 60))  # Limit width

        # Print header
        self.set_font("Arial", "B", 12)
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 8, header, border=1, align="C")
        self.ln()

        # Print rows
        self.set_font("Arial", "", 11)
        for row in data:
            y_before = self.get_y()
            x_before = self.get_x()

            # Determine max height for this row (based on cell line-wrapping)
            cell_heights = []
            for i, key in enumerate(headers):
                text = str(row.get(key, ""))
                num_lines = len(self.multi_cell(col_widths[i], 8, text, border=0, align='L', split_only=True))
                cell_heights.append(num_lines * 8)
            max_height = max(cell_heights)

            # Reset position to start of row
            self.set_y(y_before)
            self.set_x(x_before)

            # Draw each cell in the row
            for i, key in enumerate(headers):
                text = str(row.get(key, ""))
                self.multi_cell(col_widths[i], 8, text, border=1, align='L')
                self.set_xy(x_before + sum(col_widths[:i+1]), y_before)

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
