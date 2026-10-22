# Lab 3 report

- [Final English report](lab3_report.pdf): 13 A4 pages with ten figures. Team work is
  rebuilt on the GPU TESSE run of 2026-10-20 (`../runs/unity-gpu-20261020`).
- [Editable LaTeX](lab3_report.tex) and [references](references.bib).
- [Figure source](make_figures.py): regenerates the nine vector figures from existing records
  and runs the panel-alignment gate; collision and alignment audits are in `qa/`.
- [Recomputed metrics](qa/recomputed_metrics.json) and [validation notes](qa/validation.md).

The report follows `../../ReportTemplate/template.tex`: 12 pt article, 25 mm
margins, and the five main sections. The original template is unchanged.
Name, student number and lab group are set in the macros at the top of the
LaTeX source. The lab and report dates are omitted, and Section 1 states the
author's own responsibility instead of a team-member list.

## Material-to-file index

Paths below are relative to this directory. Existing evidence stays in place.

| Report content | Existing source |
| --- | --- |
| Exercise specification | [MIT VNAV Lab 3](https://vnav.mit.edu/labs_2023/lab3/exercises.html) |
| Deliverable 1 answers | [deliverable_1.txt](../../deliverable_1.txt) |
| Rotor rank and drag derivation | [deliverable_2.tex](../deliverable_2.tex), verified against the official rotor diagram |
| Controller equations and allocation | [geometric_controller.h](../../controller_pkg/include/controller_pkg/geometric_controller.h) |
| ROS conversions and input handling | [controller_node.cpp](../../controller_pkg/src/controller_node.cpp) |
| Circular trajectory derivatives | [traj_publisher.cpp](../../controller_pkg/src/traj_publisher.cpp) |
| Final gains and tuning record | [gains_used.yaml](../runs/unity-gpu-20261020/gains_used.yaml), [gains_gpu.yaml](../../controller_pkg/config/gains_gpu.yaml) |
| Figure 2: independent-model drag comparison | [numerical_validation.txt](../numerical_validation.txt) |
| Figures 4–7: final flight | [unity_flight.csv](../runs/unity-gpu-20261020/unity_flight.csv), [unity_metrics.json](../runs/unity-gpu-20261020/unity_metrics.json), [recomputed metrics](qa/recomputed_metrics.json) |
| Figure 8: gain selection | tuning comments in [gains_used.yaml](../runs/unity-gpu-20261020/gains_used.yaml) |
| Figure 9: video frames | [unity_gpu_frame.png](../video/unity_gpu_frame.png) (40 s), [rviz_gpu_frame.png](../video/rviz_gpu_frame.png) (64 s) |
| Flight video (GPU, 2026-10-20) | [Unity](../video/unity_gpu_sim.mp4), [RViz](../video/rviz_gpu.mp4) |
| Bag inventory and build evidence | [unity_bag_info.txt](../unity_bag_info.txt), [build_unity_noetic.txt](../build_unity_noetic.txt) |

## Rebuild

Run from this directory, with Python, NumPy, matplotlib and LaTeX installed:

```sh
MPLCONFIGDIR=/tmp/lab3-mpl python make_figures.py
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=qa lab3_report.tex
bibtex qa/lab3_report
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=qa lab3_report.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=qa lab3_report.tex
cp qa/lab3_report.pdf lab3_report.pdf
```

These commands process existing data and compile the report. They do not launch
ROS, a simulator or new experiments. All figures have PDF/SVG vector exports and
600 dpi PNG previews. The screenshot is included directly from its existing path.
