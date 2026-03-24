from pathlib import Path
import urllib.parse

root = Path('../')

def recursiveDeepening(dir: Path, lvl: int, structuredReadme: list) -> list:
    paths = sorted(
        [p for p in dir.iterdir() if p.name[0] != "." and p.name != "README.md"],
        key=lambda x: (x.is_file(), x.name.lower())
    )
    
    for i, obj in enumerate(paths):
        prefix = "╚" if i == len(paths) - 1 else "╠"
        
        # Lógica visual: pontas com '═', meio com '-'
        if lvl == 0:
            stem = "══"
        else:
            # Cresce 2 traços por nível. Ex: lvl 1 = ═--═, lvl 2 = ═----═
            stem = "═" + "-" * (lvl * 2) + "═"
            
        line_visual = f"{prefix}{stem} {obj.name}"
        
        # CORREÇÃO DO LINK: obj.relative_to(root) remove o '../' problemático.
        # Agora o caminho gerado parte do mesmo local onde o README.md está salvo.
        rel_path = obj.relative_to(root)
        url_path = urllib.parse.quote(rel_path.as_posix(), safe='/')
        
        line_md = f"[{line_visual}]({url_path})  "
        structuredReadme.append(line_md)
        
        if obj.is_dir():
            recursiveDeepening(obj, lvl + 1, structuredReadme)
            
    return structuredReadme

if __name__ == "__main__":
    readme_content = ["# Estrutura do Repositório\n", "╔ ROOT  "]
    readme_content = recursiveDeepening(root, 0, readme_content)

    readme_file_path = root / "README.md"

    with open(readme_file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(readme_content))

    print(f"README.md gerado com sucesso em: {readme_file_path.resolve()}")
