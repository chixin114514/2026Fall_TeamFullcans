#!/usr/bin/env bash
# scripts/build_report.sh
set -euo pipefail
cd "$(dirname "$0")/../report"
latexmk -xelatex -interaction=nonstopmode -outdir=../.build/report lab5_report.tex
cp ../.build/report/lab5_report.pdf ./lab5_report.pdf
echo "→ report/lab5_report.pdf"
