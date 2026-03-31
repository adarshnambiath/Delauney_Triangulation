# Delaunay Triangulation Playground

This repository contains:

- A Python implementation and plot for 2D Delaunay triangulation
- A 2D interactive HTML playground
- A 3D interactive HTML playground using Three.js

## Files

- `delauney.py`: Python Bowyer-Watson triangulation + matplotlib visualization
- `delaunay_interactive.html`: 2D click-to-add triangulation demo
- `delaunay_interactive_3d.html`: 3D terrain-style triangulation demo

## Run Python Demo

From the project root:

```bash
python3 delauney.py
```

## Run Interactive HTML Pages

You can open HTML files directly, but serving them via a local server is recommended.

From the project root:

```bash
python3 -m http.server 8000
```

Then open:

- http://localhost:8000/delaunay_interactive.html
- http://localhost:8000/delaunay_interactive_3d.html

## 3D Controls

- Drag: orbit camera
- Scroll: zoom
- Click: place one point
- Shift + drag: paint multiple points
- `R`: random points
- `U`: undo last point
- `C`: clear points
- `H`: toggle auto-height mode
- `[` / `-`: lower height offset
- `]` / `=`: raise height offset
