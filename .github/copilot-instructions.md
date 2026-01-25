# Copilot Instructions for GOPH547-w2026-lab00-stCM

## Project Overview
This is an **educational lab project** for GOPH 547 (w2026) demonstrating NumPy array operations and image processing with Matplotlib. The package is named `goph547lab00` and serves as a template for geophysics lab work using Python scientific computing tools.

**Key Dependencies**: NumPy, Matplotlib, Pillow (PIL)

## Architecture

### Directory Structure
- `src/goph547lab00/`: Core package
  - `arrays.py`: Utility functions for array operations (e.g., `square_ones()`)
  - `__init__.py`: Package initialization (currently empty)
- `examples/driver.py`: Main demonstration script showing NumPy and image processing workflows
- `pyproject.tmol`: Project metadata and dependencies (setuptools-based)

### Data Flow Pattern
The driver script demonstrates a **linear workflow**:
1. **Create arrays**: Using `np.ones()`, `np.zeros()`, `np.arange()`, `np.identity()`
2. **Perform operations**: Element-wise multiplication, dot products, cross products
3. **Load images**: Via PIL into NumPy arrays
4. **Transform images**: RGB to grayscale conversion using weighted dot product `[0.2989, 0.5870, 0.1140]`
5. **Visualize**: Using `matplotlib.pyplot.imshow()` and `.show()`

## Developer Workflows

### Running the Project
```bash
# From project root
python examples/driver.py
```

**Prerequisites**: Ensure `rock_canyon.jpg` exists at `src/goph547lab00/rock_canyon.jpg` (referenced in driver.py line 37).

### Package Installation (for development)
```bash
pip install -e .
```
This installs the `goph547lab00` package in editable mode, making utilities available for import.

### Project Configuration
- **Python version**: ≥3.8
- **Build system**: setuptools
- **License**: GNU GPL v3

## Project-Specific Conventions

### NumPy Operations
- Use standard NumPy constructors: `np.ones()`, `np.zeros()`, `np.arange()`
- For image slicing: Use fancy indexing (e.g., `array[:, col_start:col_end, :]`)
- RGB to grayscale: Apply weighted sum with coefficients `[0.2989, 0.5870, 0.1140]` via `np.dot()`

### Image Processing Pattern
- Load images with `PIL.Image.open()` → convert to NumPy array with `np.asarray()`
- Access shape via `.shape` property (returns tuple: rows, cols, channels)
- Extract spatial slices before processing (e.g., center column extraction in driver.py lines 40-43)
- Display with `plt.imshow()` followed by `plt.show()` for interactive display

### Code Organization
- Core utilities go in `src/goph547lab00/` as importable functions
- Demonstrations and scripts go in `examples/`
- Commented-out print statements in driver.py indicate optional debugging output (lines 20-27)

## Integration Points & External Dependencies

### NumPy
- Primary tool for array operations and mathematical functions
- Critical for RGB→grayscale transformation (`np.dot()` with weight coefficients)

### Matplotlib
- Used exclusively for visualization via `pyplot` interface
- Interactive display requires `.show()` call

### Pillow (PIL)
- Image loading only (`Image.open()`)
- Conversion to NumPy array via `np.asarray()`

## Common Patterns to Follow

1. **Array creation for testing**: Use utility functions like `square_ones()` from `arrays.py`
2. **Image processing workflows**: Load → reshape → transform → visualize
3. **Slicing multi-dimensional arrays**: Use NumPy fancy indexing with `[:, start:end, :]` notation
4. **Visualization workflow**: Create figure → imshow → show (don't assume non-interactive environments)

## Notes for Contributors
- This is a **teaching project** — prioritize clarity and educational value
- Commented-out debugging statements are acceptable (see driver.py)
- The image file (`rock_canyon.jpg`) is required but not in repo; ensure it exists for full functionality
- Update `arrays.py` with new utility functions as lab assignments expand
