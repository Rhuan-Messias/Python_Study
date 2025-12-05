# pip install pikepdf

import pikepdf
from pathlib import Path

pasta = Path("/caminho/da/sua/pasta")
pdf_final = pikepdf.Pdf.new()

for i in range(1, 15):
    arquivo = pasta / f"nome_do_arquivo{i:02d}.pdf"
    with pikepdf.open(arquivo) as pdf:
        for page in pdf.pages:
            pdf_final.pages.append(page)

pdf_final.save(pasta / "nome_do_arquivo.pdf")
