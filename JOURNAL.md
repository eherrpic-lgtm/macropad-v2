# Build Journal - 12-Key Custom Macropad

## Total Estimated Time: ~15 Hours

---

### Entry 1: Project Concept & Component Layout
**Date:** ~22/7/26
**Time Spent:** ~2.5 Hours

- Defined project scope: A 12-key custom macropad with two rotary encoders for quick productivity shortcuts and media controls.
- Mapped out the hardware constraints and pin requirements for the microcontroller, key matrix, and encoder inputs (utilizing rotation pins A/B, bypassing encoder push-clicks).
- Selected components, switches, and keycaps for an ergonomic desktop footprint.

<img width="1710" height="1112" alt="Macropad inspo" src="https://github.com/user-attachments/assets/583c94c9-6709-4e96-8cc3-2f383b5b332e" />

---

### Entry 2: KiCad Schematic Design
**Date:** ~23/7/26
**Time Spent:** ~3.5 Hours

- Built the schematic in KiCad including the 12-key matrix and diodes.
- Added the microcontroller symbol and assigned dedicated GPIO pins for matrix rows/columns and the rotary encoder rotation lines.
- Ran Electrical Rules Check (ERC) to verify net connections, power symbols, and pin assignments.

<img width="1004" height="578" alt="Schematic" src="https://github.com/user-attachments/assets/7dd0d23e-1504-4a35-b25e-02147324a573" />

---

### Entry 3: PCB Layout, Copper Fills & DRC
**Date:** ~25/7/26
**Time Spent:** ~4.5 Hours

- Positioned the 12 key footprints on a clean grid layout with the rotary encoder in position.
- Defined the custom PCB outer contour and set up trace routing for matrix lines and ground/power.
- Added ground copper fills on top and bottom layers, along with custom silkscreen labeling.
- Ran KiCad Design Rules Check (DRC) to ensure trace clearances, drill holes, and pad dimensions met manufacturing standards.

<img width="688" height="580" alt="PCB" src="https://github.com/user-attachments/assets/080a7b04-9697-44f5-993b-7c3634387ff4" />

---

### Entry 4: 3D Chassis Design in Fusion 360
**Date:** ~27/7/26
**Time Spent:** ~3 Hours

- Designed a multi-layer sandwich-mount chassis in Fusion 360 to enclose the macropad.
- Aligned mounting holes for hardware standoffs across the top switch plate, main PCB clearance layer, and bottom plate.
- Exported DXF files for plate fabrication and double-checked tolerance clearances around the switches and rotary knob.

<img width="1822" height="1102" alt="Assembly2" src="https://github.com/user-attachments/assets/2492cacc-3f7f-49ad-a800-0045f910cd4c" />
<img width="1822" height="1102" alt="Assembly1" src="https://github.com/user-attachments/assets/b42cfd7b-9006-4a44-8f87-7ae33bd4f797" />
<img width="1822" height="1102" alt="Assembly0" src="https://github.com/user-attachments/assets/14155b1d-961c-4d49-a890-c0538d238454" />

---

### Entry 5: Firmware Setup & Final Documentation
**Date:** ~29/7/26
**Time Spent:** ~1.5 Hours

- Configured the firmware matrix pins and encoder rotary mapping.
- Generated Gerber files, NC drill files, and the bill of materials (BOM).
- Organized repository files and finalized documentation for submission.

- <img width="1060" height="369" alt="Screenshot 2026-11-09 at 11 43 58" src="https://github.com/user-attachments/assets/3d84a600-5132-440f-a718-1393cd988de7" />
