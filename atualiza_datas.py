from datetime import datetime
import re

# Formato de data usado
data_atual = datetime.now().strftime("%Y-%m-%d")

# Arquivos HTML que terão a data atualizada
arquivos_html = ["index.html", "termos.html", "exclusao-conta.html"]

for arquivo in arquivos_html:
    with open(arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Substitui "Última atualização: DD/MM/AAAA" mantendo o formato
    conteudo = re.sub(
        r"Última atualização:\s*\d{2}/\d{2}/\d{4}",
        f"Última atualização: {datetime.now().strftime('%d/%m/%Y')}",
        conteudo
    )

    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"[OK] Data atualizada em {arquivo}")

# Atualiza o sitemap.xml
with open("sitemap.xml", "r", encoding="utf-8") as f:
    sitemap = f.read()

sitemap = re.sub(
    r"<lastmod>\d{4}-\d{2}-\d{2}</lastmod>",
    f"<lastmod>{data_atual}</lastmod>",
    sitemap
)

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)

print("[OK] Datas do sitemap.xml atualizadas")
