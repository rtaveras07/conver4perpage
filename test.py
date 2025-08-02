import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from io import BytesIO
from pdf2image import convert_from_path

def pdf_4_pages_tight_layout(input_pdf_path, output_pdf_path):
    images = convert_from_path(input_pdf_path, dpi=150)

    width, height = A4
    c = canvas.Canvas(output_pdf_path, pagesize=A4)

    # Márgenes externos (mantener un borde seguro para impresión)
    outer_margin = 1 * 72 / 2.54  # 1 cm ≈ 28 pts

    # 🔧 Márgenes internos mínimos (¡reducidos!)
    #gutter_x = 0.05 * 72 / 2.54  # ~1.4 pts (≈0.05 cm)
    #gutter_y = 0.05 * 72 / 2.54
    gutter_x = -1
    gutter_y = -1
    
    mini_width = (width - 2 * outer_margin - gutter_x) / 2
    mini_height = (height - 2 * outer_margin - gutter_y) / 2

    positions = [
        (outer_margin, outer_margin + mini_height + gutter_y),               # arriba izquierda
        (outer_margin + mini_width + gutter_x, outer_margin + mini_height + gutter_y),  # arriba derecha
        (outer_margin, outer_margin),                                        # abajo izquierda
        (outer_margin + mini_width + gutter_x, outer_margin),               # abajo derecha
    ]

    for i in range(0, len(images), 4):
        slots = images[i:i+4]

        for j, img in enumerate(slots):
            img_io = BytesIO()
            img.save(img_io, format='PNG')
            img_io.seek(0)
            img_reader = ImageReader(img_io)
            x, y = positions[j]
            c.drawImage(img_reader, x, y, width=mini_width, height=mini_height)

        c.showPage()

    c.save()
    print(f'✅ ¡PDF generado con espacio mínimo entre tablas!: {output_pdf_path}')


# 👇 USO
entrada = "my.pdf"
salida = "Final_4_x_pagina.pdf"
pdf_4_pages_tight_layout(entrada, salida)
