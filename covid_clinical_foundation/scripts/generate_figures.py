"""Generate SVG figures for the COVID clinical foundation package.

This script intentionally uses only the Python standard library so the report can
be regenerated in a minimal environment. It reads the aggregate CSV files in
../data and writes slide-ready SVG files into ../figures.
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

COLORS = {
    "red": "#c0392b",
    "blue": "#2c7fb8",
    "green": "#2ca25f",
    "orange": "#f39c12",
    "purple": "#756bb1",
    "gray": "#7f8c8d",
    "light": "#f7f7f7",
    "black": "#222222",
}


def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def svg_header(width: int, height: int, title: str) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        f'<rect width="100%" height="100%" fill="white"/>',
        f'<text x="{width/2}" y="34" text-anchor="middle" font-family="Arial" font-size="22" font-weight="700">{title}</text>',
    ]


def bar_chart(rows: list[dict[str, str]], path: Path) -> None:
    width, height = 980, 560
    margin_l, margin_b = 110, 90
    plot_w, plot_h = 800, 380
    max_y = 10.0
    labels = [r["group"] for r in rows]
    actual = [float(r["actual_tests_per_1000_week"]) for r in rows]
    fair = [float(r["fair_cmab_tests_per_1000_week"]) for r in rows]
    burden = [float(r["burden_cases_per_100k"]) for r in rows]
    max_b = max(burden)
    out = svg_header(width, height, "Figure 2. Context-blind vs context-aware test routing")
    out.append(f'<line x1="{margin_l}" y1="{height-margin_b}" x2="{margin_l+plot_w}" y2="{height-margin_b}" stroke="#333"/>')
    out.append(f'<line x1="{margin_l}" y1="{height-margin_b}" x2="{margin_l}" y2="{height-margin_b-plot_h}" stroke="#333"/>')
    for tick in range(0, 11, 2):
        y = height - margin_b - plot_h * tick / max_y
        out.append(f'<line x1="{margin_l-5}" y1="{y}" x2="{margin_l+plot_w}" y2="{y}" stroke="#ddd"/>')
        out.append(f'<text x="{margin_l-12}" y="{y+5}" text-anchor="end" font-family="Arial" font-size="12">{tick}</text>')
    group_w = plot_w / len(rows)
    for i, label in enumerate(labels):
        x0 = margin_l + i * group_w + 25
        aw = 28
        h1 = plot_h * actual[i] / max_y
        h2 = plot_h * fair[i] / max_y
        y1 = height - margin_b - h1
        y2 = height - margin_b - h2
        out.append(f'<rect x="{x0}" y="{y1}" width="{aw}" height="{h1}" fill="{COLORS["red"]}" opacity="0.85"/>')
        out.append(f'<rect x="{x0+34}" y="{y2}" width="{aw}" height="{h2}" fill="{COLORS["green"]}" opacity="0.85"/>')
        by = height - margin_b - plot_h * burden[i] / max_b
        out.append(f'<circle cx="{x0+31}" cy="{by}" r="5" fill="{COLORS["black"]}"/>')
        out.append(f'<text x="{x0+31}" y="{height-margin_b+22}" text-anchor="middle" font-family="Arial" font-size="11">{label}</text>')
    out.append(f'<text x="30" y="260" transform="rotate(-90,30,260)" text-anchor="middle" font-family="Arial" font-size="14">tests per 1,000 per week</text>')
    out.append('<rect x="700" y="70" width="18" height="18" fill="#c0392b"/><text x="725" y="84" font-family="Arial" font-size="13">Actual / context-blind</text>')
    out.append('<rect x="700" y="96" width="18" height="18" fill="#2ca25f"/><text x="725" y="110" font-family="Arial" font-size="13">Fair CMAB + EQUITAS</text>')
    out.append('<circle cx="709" cy="130" r="5" fill="#222"/><text x="725" y="134" font-family="Arial" font-size="13">relative burden index</text>')
    out.append('</svg>')
    path.write_text('\n'.join(out), encoding='utf-8')


def main() -> None:
    rows = read_csv("routing_inputs.csv")
    bar_chart(rows, FIG / "fig2_routing_counterfactual.svg")
    # The remaining report figures are included as committed SVG files in this package.


if __name__ == "__main__":
    main()
