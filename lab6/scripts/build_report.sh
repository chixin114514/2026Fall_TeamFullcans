#!/usr/bin/env bash
# scripts/build_report.sh
set -euo pipefail
cd "$(dirname "$0")/../report"
latexmk -xelatex -interaction=nonstopmode -outdir=../.build/report lab6_report.tex
cp ../.build/report/lab6_report.pdf ./lab6_report.pdf
echo "→ report/lab6_report.pdf"
