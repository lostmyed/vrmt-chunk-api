# VR Training System Overview

This document describes how users interact with the VR training environment for glass bottle manufacturing, what actions are available, and how lessons are structured.

---

## 1. Movement & Interaction

### Teleportation
#### Fixed Position Teleportation
- User can use the 9 fixed positions on the `Wrist Menu`
##### Main Factory Locations
1. `Blank Side`
2. `Blow Side`
3. `Reject Station`
4. `Orifice Platform`
5. `Feeder Platform`
6. `Bottle Tester`
7. `Stacker` / `Transfer`
##### Training Room Locations
8. `Training Section`
9. `Training Feeder`
#### Point Type Teleportation
- Users move by holding the `Y` button on the **left-hand controller** or `B` button on **right-hand controller**.
- The arc shows the target location. Releasing the button teleports the user.
### Interaction
- User can use **left** or **right** hand for interactions.
- `Pointing Mode`: Use `Grip Button` only to form hand pointing gesture.
- `Grip Action`: Use `Grip Button` to pick up or grab items.
#### Interactable Objects
- `Press Button`: Use `Pointing Mode` to press button.
- `Toggle Switch`: Use `Pointing Mode` to select & then `Joystick` up, down, left or right to adjust.
- `Hand Lever`: Use `Grip Action` to hold lever arm then rotate hand to adjust.
- `PDA`, `Bottle Tester Control Panel`, `Training Feeder Control Panel`, `Media Player`, `Training Video Player`, `Exercise Training PDA`: Use `Grip Action` to hold and move around, use `Pointing Mode` to interact.
- `Bottle Tongs`: Use  `Grip Action` to hold tongs and `Trigger Button` to grab bottle.
- `Fire Hose`: Use  `Grip Action` to hold hose and `Trigger Button` to release Water jet.
- `Fire Exinguisher`: Use `Grip Action` to hold extinguisher with one hand, remove the lock pin by grabbing it and pulling it out with your other hand, then hold the hose using `Grip Action`. Pull `Trigger Button`: on the hand holding the extinguisher to release Water jet.
- `Air Hose`: Use  `Grip Action` to hold hose and `Trigger Button` to release Air jet.
- `Swab Brush`: Use  `Grip Action` to hold brush.
- `Deluge Handle`: Use  `Grip Action` to hold handle and pull down to activate.
- `Whiteboard`: Use  `Grip Action` to hold and move board, Use  `Grip Action` to hold Pens.


---
## 2. UI Panels & Menus

### Wrist Menu
- Tap the watch on your left hand to open the `Wrist Menu`.
#### Main Page
  - `Teleport Locations` 9 fixed teleport locations.
  - Retrieve `PDA`
  - Retrieve `Temperature Gun`
  - Retrieve `Whiteboard`
  - Retrieve `Media Player`
  - External Camera Controls
	  - Toggle eye view and external camera view.
	  - Retrieve external camera.
	  - Send external  camera home.
  - Retrieve  `Training Video Player`
  - VR App Settings button.
#### VR App Settings
  - Change Language
  - Teleport Comfort Mode
  - PC Performance Setting
  - External Camera Resolution
  - Screen Shot Mode
### PDA
- The `PDA` is the main User UI.
- The **bottom menu** is available on every Tab.
#### Bottom Menu
- `Analogue Speed Control`: When selected pushing up or down on the **left-hand controller** `Joystick` will adjust the speed of the **`system simulation`**.
- Play and Pause buttons for the **`system simulation`**.
- Fault notification indicator.
- Increase and Decrease speed of the **`system simulation`**.
#### Home Tab
##### Section Sub Tab
-  General status of the sections.
- Adjust cycle time for the sections: This increases or decreases the rate at what glass products are created.
- "Section Through" toggle button (only available in the `Training Room`).
- Adjust `Training Section` height (only available in the `Training Room`).
##### Temperature Sub Tab
- This shows the temperature of components that have been checked via the `Temperature Gun`.
- Toggle button to link this data to the gun so temperatures get sent to this page.
- Toggle `mould cooling` visualisation.
- Adjust time it takes for the moulds to reach full temperature in the **`system simulation`**.
##### Fire Sub Tab
- Shows the statues of the section fire.
- Shows the status of the Air and Oil valves.
- Adjust the effectiveness of the fire fighting equipment in the **`system simulation`**. 
#### Timings Tab
- Adjust timing values for section components.
- Note: Changes must be uploaded to apply.
- Load, change, and save Timing pre-sets.
#### Feeder Tab
- Adjust gob target temperature.
- Adjust `needle` stroke, datum, offset.
- Change `needle` cam.
- Adjust `shear` stroke.
- Load, change, and save Feeder pre-sets.
#### Identify Tab
- Select and highlight components of the `section`.
#### Settings Tab
- Change `Section Control Panel` type. (machine state: `section_control_panel_type`)
- Change `Section Manifold Panel` type. (machine state: `section_manifold_panel_type`)
- Toggle between `Press and Blow` or `Blow and Blow`.
- Change Blank Side Guard type.
- Toggle `section` component Collision Simulation.
- Change Plunger type.
- Adjust ambient factory sound.
- Reset the VR system.
- Change units (metric/imperial).
#### VRMT Training Tab
- Select, start and stop a training lesson.

### Bottle Tester Control Panel
- View the full Fault Library.
- View the current fault for the bottle that is in the `Bottle Tester`.

 ### Training Feeder Control Panel
- Adjust gob target temperature.
- Adjust `needle` stroke, datum, offset.
- Change `needle` cam.
- Adjust `shear` stroke and height.
- Adjust `tube` height and rotation.
- Visualisation of `gob` shape and orientation.
- Shows `gob` width, length and weight.
- Adjust height of training feeder.
### Media Player
- This allows the user to view there own video and PDF files.
- The User needs to add their files into the media folder on their PC. 

---
## 3. In-App Locations and Control Interfaces
### Main Factory
#### Feeder Platform
- Forehearth.
- Main Feeder (Top Section).
- `tube height` and `tube rotation` Control Panels.
- Shear Height Control Panel.
#### Orifice Platform
- Main Feeder (Bottom Section).
- Orifice.
- Shear Mechanism.
- Distributor.
- Shear and Distributor Control Panels.
#### Blank Side
- `Section Control Panel`s. (machine state: `section_control_panel_type`)
- Manifold Control Panels.
- Remote Control Panels for the Shear, Distributer and Tube Controls.
	- These must be enabled on the orifice control panels to function.
- Blank Swabbing Station.
	- Includes `Swab Brush`.
- Fire Extinguisher and `Fire Hose`.
- `Air Hose`.
- Air and Oil Valves.
	- Operated via there `Hand Lever`s
- Fire Alarm Button.
- Access to `Blank Side` of Sections 1,2 and 3.
#### Blow Side
- `Section Control Panel`s. (machine state: `section_control_panel_type`)
- Fire Extinguisher and `Fire Hose`.
- `Air Hose`.
- Fire Alarm Button.
- Product Scales.
- Bottle Tongs.
- Access to `Blow Side` of Sections 1,2 and 3.
#### Bottle Tester
- `Bottle Tester`.
- `Bottle Tongs`.
- Bottle Tester Reject.
### Training Room
#### Training Section
- `Training Section`
- Training `Section Control Panel` (machine state: `section_control_panel_type`)
#### Feeder Section
- Training Feeder.
- Training Feeder Control Panel.
### Maintenance Room
- Maintenance Table.
- Presentation Screen.

---
## 4. Lesson Structure

### Overview
- Lessons are divided into sequential tasks: `Task Description`
- Task instruction (TTS) explain to the user what to do.
- Multiple `Task Description` may need to completed before the next Task instruction.
- Task instructions are listed in `Previous Instructions` list.

### Example Task: E-Stop
- Last task in `Previous Instructions`: "Good, now hit the red emergency stop button."
- `Task Description`: "User needs to engage the E-Stop"
- System confirms a relevant E-Stop has been engaged before continuing.

---
## 5. Available Training Actions
### Basic
- Complete structured training lessons
- Start a machine section
- Turn the gob on for a section
- Stop a section (controlled or emergency stop)
- Test and reset E-Stops
- Respond to fire safety events
### Advanced
- Adjust the deflector
- Adjust the needles and shear controls
- Adjust timings on a section
- Adjust section component speeds via `Section Manifold Panel` (machine state: `section_manifold_panel_type`)

---
## 6. System Interlocks and Operational Dependencies
### Feeder Tube

**Overview:**
The tube must be raised to allow molten glass to stream from the feeder through the orifice into the shear zone.

**Requirements:**
- Feeder temperature must be at operational range.
- Tube must be raised via the feeder control panel. (machine state: `tube_height > 0`)

**Effect:**
- When raised, glass will begin streaming vertically toward the shear blades.
### Needles

**Overview:**
Oscillating mechanism that initialises the shape of the gob.

**Requirements:**
- Glass must be streaming (machine state: `tube_height > 0`)
- Needles must be activated via the needles control panel (machine state: `needles_on = true`)

**Effect:**
- Pushes the glass through the orifice to shape the gob.
### Shears

**Overview:**
The shears cut the continuous glass stream into gobs at regular intervals.

**Requirements:**
- Glass must be streaming (tube raised).
- Shears must be active via the shears control panel (machine state: `shears_on = true`)

**Effect:**
- Gobs are formed from the molten glass stream and delivered toward the distributor.
### Distributor

**Overview:**
Rotating mechanism that delivers formed gobs to available machine sections. It has 2 positions **In Position** and **Not In Position**. When shears are off it will automatically move to **Not In Position** to allow the stream of glass to enter the gob chute and be recycled.

**Requirements:**
- Shears must be cutting gobs to allow the distributer to be in position `distributor positioned` 
- Distributor must be powered on and positioned via the distributor control panel (machine state: `distributor_positioned = true` and  `distributor_enabled = true`).

**Effect:**
- When the requirements have been met `Gob Delvery` is **Active** or **On**
- Routes each gob to a selected section in sequence via the **scoops**. The **Flap** deflects the gob to the **scoops** to feed the required section.
### Delivery

**Overview:**
The delivery chutes guide the gobs into the section blank moulds.

**Requirements:**
- The gobs must be guided into the centre of the moulds.
- If delivery needs adjusting the controls are on the individual sections on the `Blank Side`.

**Effect:**
- Incorrectly adjusted delivery chutes can cause damage to the gobs and in some cases enable the gob to land on top of the moulds and cause a fire.
### Section Start (Per Section)

**Overview:**
- Each machine section can be started individually.
- Then sections are the machinery assemblies the form the bottles from the gobs. 

**Requirements:**
- No E-Stops are engaged for the section (machine state: `blank_estop_engaged = false` `blow_estop_engaged = false` `manifold_estop_engaged = false`)
- Section must be activated via the section control panel.

**Effect:**
- Section is cycling or **Started**. (machine state: `running = true`)

### Gob On (Per Section)

**Overview:**
Enables glass delivery to an individual section.

**Requirements:**
- Section must be cycling or **Started**. (machine state: `running = true`)
- `Gob Delivery` must be **Active**.

**Effect:**
- Section is now forming Bottles.
---
## 7. Bottle Fault Procedure

- Bottle faults are automatically detected by inspection equipment located along the system conveyors. These devices are visible in the VR environment but are **non-interactive** and provided for reference only.
- When a fault is detected, it is indicated on the `PDA` located in the bottom menu, marked as **"Fault Detected"**.
- Faulty bottles are automatically diverted onto the **Reject Conveyor**.
- The user must then use the `Bottle Tongs` to manually transfer the rejected bottle onto the `Bottle Tester`.
- The `Bottle Tester` will display all detected faults for that bottle through the **Bottle Tester Control Panel**.

---
## 8. Section Control Panel Button Positions

- The user may be using different types of section control panels. The current panel in use is defined by the machine state value: `section_control_panel_type`.
- **Only provide button instructions for the control panel that matches the current value of `section_control_panel_type`.** Do not reference or describe any other control panels, even if they are listed below.
- The user's position is defined by `user_location`. If this is set to `"Blank Side"` or `"Blow Side"`, describe the corresponding control panel for that side:
- If `user_location = "Blank Side"`, describe the **Blank Side Control Panel**.
- If `user_location = "Blow Side"`, describe the **Blow Side Control Panel**.
- If `user_location` is missing or does not match either of these values, **default to describing the Blank Side Control Panel**, and clearly inform the user that the instructions assume they are on the Blank Side.

### Emhart Red 1

_(Use only if `section_control_panel_type` = `"Emhart Red 1"`)_
#### Blank Side Control Panel

- **Start Section:** Press the 2 green start buttons simultaneously, located bottom left and bottom right.
- **Turn Gob On/Off:** Press the yellow button on the bottom row of buttons.
- **Controlled Stops:**
	- There are 2 controlled stop buttons on the panel, one stops the invert arm on the Blank Side, the other stops the invert arm on the Blow Side.
	- **Controlled Stop** (Invert stops Blank Side): Press the red button on the bottom row forth from the right.
	- **Controlled Stop** (Invert stops Blow Side): Press the red button on the bottom row sixth from the right.
- **Swab:** Press the white button on the bottom row third from the right.
- **Reject Bottle** (inside cavity): Press the black switch on the bottom row second from the left.
- **Reject Bottle** (outside cavity): Press the black switch on the bottom row third from the left.
- **E-Stop:** Press the large red button on the right of the panel.
#### Blow Side Control Panel

- **Start Section:** Press the 2 green start buttons simultaneously, located bottom row and top row.
- **Turn Gob On/Off:** Press the yellow button on the top row of buttons.
- **Controlled Stop:** Press the red button on the top row.
- **Swab:** Press the white button on the top row forth from the right.
- **E-Stop:** Press the large red button on the right of the panel.
### Emhart Red 2

_(Use only if `section_control_panel_type` = `"Emhart Red 2"`)_
#### Blank Side Control Panel

- **Start Section:** Press the 2 green start buttons simultaneously, located bottom left and bottom right.
- **Turn Gob On/Off:** Press the yellow button on the bottom row of buttons.
- **Controlled Stops:**
	- There are 2 controlled stop buttons on the panel, one stops the invert arm on the Blank Side, the other stops the invert arm on the Blow Side.
	- **Controlled Stop** (Invert stops Blank Side): Press the red button on the bottom row forth from the right.
	- **Controlled Stop** (Invert stops Blow Side): Press the red button on the bottom row sixth from the right.
- **Swab:** Press the white button on the bottom row third from the right.
- **Reject Bottle** (inside cavity): Press the black switch on the bottom row second from the left.
- **Reject Bottle** (outside cavity): Press the black switch on the bottom row third from the left.
- **E-Stop:** Press the large red button on the right of the panel.
#### Blow Side Control Panel

- **Turn Gob On/Off:** Press the yellow button on the top row of buttons.
- **Controlled Stop:** Press the red button on the top row.
- **Swab:** Press the white button on the top row forth from the right.
- **E-Stop:** Press the large red button on the right of the panel.
### Bottero

_(Use only if `section_control_panel_type` = `"Bottero"`)_
#### Blank Side Control Panel

- **Start Section:** Press the Blue button, positioned on the bottom left, while depressed press the button with the white outline around it towards the centre on the bottom row.
- **Turn Gob On/Off:** Press the Blue button, positioned on the bottom left, while depressed press the button with the white outline around it towards the centre on the top row.
- **Controlled Stop:** Press the button with the black outline around it on the bottom row.
- **Swab:** Press the button on the bottom row third from the right, with the icon depicting a swab brush in the moulds.
- **Reject Bottle** (inside cavity): Press the button on the bottom row sixth from the left, with the icon depicting a blow off.
- **Reject Bottle** (outside cavity): Press the button on the bottom row seventh from the left, with the icon depicting a blow off.
- **E-Stop:** Press the large red button on the left of the panel.
#### Blow Side Control Panel

- **Start Section:** Press the Blue button, positioned on the bottom left, while depressed press the button with the white outline around it towards the centre on the bottom row.
- **Turn Gob On/Off:** Press the Blue button, positioned on the bottom left, while depressed press the button with the white outline around it towards the centre on the top row.
- **Controlled Stop:** Press the button with the black outline around it on the bottom row.
- **Reject Bottle** (inside cavity): Press the button on the bottom row sixth from the left, with the icon depicting a blow off.
- **Reject Bottle** (outside cavity): Press the button on the bottom row seventh from the left, with the icon depicting a blow off.
- **E-Stop:** Press the large red button on the left of the panel.

*End of document.*