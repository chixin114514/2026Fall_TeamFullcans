#!/usr/bin/env bash
# scripts/build_report.sh
set -euo pipefail
cd "$(dirname "$0")/../report"
latexmk -xelatex -interaction=nonstopmode -outdir=../.build/report lab9_report.tex
cp ../.build/report/lab9_report.pdf ./lab9_report.pdf
echo "→ report/lab9_report.pdf"
