# Camera QC Application

Quality control and maintenance application with guided workflows and camera integration.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
```

2. Activate virtual environment:
- Windows: `venv\Scripts\activate`
- Linux: `source venv/bin/activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
camera_qc_app/
├── main.py                          # Application entry point
├── requirements.txt                 # Python dependencies
├── camera/                          # Camera abstraction layer
│   ├── camera_interface.py         # Base camera interface
│   ├── opencv_camera.py            # Webcam/borescope implementation
│   └── camera_manager.py           # Camera discovery and management
├── gui/                             # GUI modules
│   ├── mode_selection.py           # Initial mode selection screen
│   ├── mode1_capture.py            # General image capture
│   ├── mode2_qc.py                 # QC workflow
│   └── mode3_maintenance.py        # Maintenance workflow
├── workflows/                       # Workflow definitions
│   ├── qc_workflows/               # QC process definitions (JSON)
│   └── maintenance_workflows/      # Maintenance process definitions (JSON)
├── reports/                         # PDF report generator
│   └── pdf_generator.py
├── resources/                       # Reference images and assets
│   ├── qc_reference_images/
│   └── maintenance_reference_images/
└── output/                          # Generated reports and captured images
    ├── reports/
    └── captured_images/
```

## Workflow Configuration

Workflows are defined in JSON files. You can edit these directly or add new workflows by creating new JSON files in the appropriate directory.

### QC Workflow Format
See `workflows/qc_workflows/robot_component_qc.json` for example.

### Maintenance Workflow Format
See `workflows/maintenance_workflows/motor_bearing_replacement.json` for example.

## Adding Reference Images

Place reference images in:
- `resources/qc_reference_images/` for QC workflows
- `resources/maintenance_reference_images/` for maintenance workflows

Reference the image filename in your workflow JSON files.

## Usage

Run the application:
```bash
python main.py
```

## Camera Support

- **Webcam**: Standard USB webcams (OpenCV)
- **Borescope**: USB borescope cameras (OpenCV)
