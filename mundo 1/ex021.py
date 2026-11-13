# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import os
from pathlib import Path

arquivo = Path(input("Digite o caminho do arquivo MP3: ").strip().strip('"'))

if not arquivo.is_file():
    raise SystemExit(f"Arquivo não encontrado: {arquivo}")

if arquivo.suffix.lower() != ".mp3":
    raise SystemExit("O arquivo informado não tem a extensão .mp3.")

try:
    os.startfile(str(arquivo.resolve()))
except OSError as erro:
    raise SystemExit(f"Não foi possível abrir o MP3: {erro}") from erro

print("MP3 aberto no reprodutor padrão do Windows.")