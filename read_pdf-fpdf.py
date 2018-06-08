from fpdf import FPDF

pdf = FPDF()

pdf.add_font('waree', '', 'waree.ttf', uni=True)
pdf.set_font('waree', '', 14)