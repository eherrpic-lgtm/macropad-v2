# Build Journal - 12-Key Custom Macropad

## Total Estimated Time: ~15 Hours

---

### Entry 1: Project Concept & Component Layout
**Date:** ~22/7/26
**Time Spent:** ~2.5 Hours

- Defined project scope: A 12-key custom macropad with two rotary encoders for quick productivity shortcuts and media controls.
- Mapped out the hardware constraints and pin requirements for the microcontroller, key matrix, and encoder inputs (utilizing rotation pins A/B, bypassing encoder push-clicks).
- Selected components, switches, and keycaps for an ergonomic desktop footprint.

---

### Entry 2: KiCad Schematic Design
**Date:** ~23/7/26
**Time Spent:** ~3.5 Hours

- Built the schematic in KiCad including the 12-key matrix and diodes.
- Added the microcontroller symbol and assigned dedicated GPIO pins for matrix rows/columns and the rotary encoder rotation lines.
- Ran Electrical Rules Check (ERC) to verify net connections, power symbols, and pin assignments.

---

### Entry 3: PCB Layout, Copper Fills & DRC
**Date:** ~25/7/26
**Time Spent:** ~4.5 Hours

- Positioned the 12 key footprints on a clean grid layout with the rotary encoder in position.
- Defined the custom PCB outer contour and set up trace routing for matrix lines and ground/power.
- Added ground copper fills on top and bottom layers, along with custom silkscreen labeling.
- Ran KiCad Design Rules Check (DRC) to ensure trace clearances, drill holes, and pad dimensions met manufacturing standards.

---

### Entry 4: 3D Chassis Design in Fusion 360
**Date:** ~27/7/26
**Time Spent:** ~3 Hours

- Designed a multi-layer sandwich-mount chassis in Fusion 360 to enclose the macropad.
- Aligned mounting holes for hardware standoffs across the top switch plate, main PCB clearance layer, and bottom plate.
- Exported DXF files for plate fabrication and double-checked tolerance clearances around the switches and rotary knob.

---

### Entry 5: Firmware Setup & Final Documentation
**Date:** ~29/7/26
**Time Spent:** ~1.5 Hours

- Configured the firmware matrix pins and encoder rotary mapping.
- Generated Gerber files, NC drill files, and the bill of materials (BOM).
- Organized repository files and finalized documentation for submission.