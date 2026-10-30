# PlayGTA6 browser client

This repository is a community-maintained enhancement fork of an archived browser client snapshot. It is not an official Rockstar Games product.

## Current enhancements

The browser page includes:
- Fullscreen toggle and a quick controls guide.
- Graphics/performance preferences for render scale, frame rate, and the existing low-memory profile.
- Saved graphics preferences in the browser, with an apply-and-reload flow.
- Touchscreen joystick and action buttons for coarse-pointer devices.
- The original browser engine loader, WebAssembly worker architecture, and keyboard/mouse input path remain in place.

## Important: game data is not included

The original snapshot separates its browser client from the large .mirror game-data directory. This repository does not contain that directory. The original README describes it as approximately 19.7 GB. The game will not reach playable world content until the required data is supplied through a lawful copy that the user is authorized to access.

No Rockstar game assets are included or redistributed by this fork. Do not upload copyrighted game data to this repository or a public host.

## Run locally

1. Download or clone this repository.
2. Place the required, lawfully obtained mirror data in the expected local folder: mirror/playgta5.com/.
3. Keep the original directory layout intact, including the browser build under b/8b0b5899ed/ and the data/ tree.
4. On Windows, run Launch-Local.cmd.
5. The launcher starts the local server and opens http://localhost:8000/.

The server sets the cross-origin isolation headers required by the SharedArrayBuffer/pthread build and supports byte-range reads. Opening the HTML file directly with file:// will not work.

## Controls

### Keyboard and mouse
- Click the game canvas to capture the mouse.
- Esc releases pointer lock.
- Shift + P switches the engine keyboard mode.
- = toggles the FPS counter.
- Use the in-game loading choices to select Story Mode or Sandbox Mode.

### Touchscreen
- Left virtual joystick: move.
- RUN: hold sprint.
- JUMP: jump.
- VEHICLE: vehicle enter/exit action.
- ACTION: context action.

Touch controls appear on devices that report a coarse pointer. The original engine remains the source of gameplay behavior, so the exact action available depends on the current game state.

## Graphics settings

Open SETTINGS in the top-right corner:
- Graphics quality: High or Performance.
- Render scale: 100%, 85%, 75%, or 60%.
- Frame rate: 60 or 30 FPS.
- Shadows: off or low (only relevant when the Performance profile is not forcing the low-memory preset).

Apply & Reload restarts the page because the engine reads these values during startup. Performance mode uses the existing low-memory arguments and reduces texture, vehicle, pedestrian, shadow, reflection, particle, grass, density, and LOD workloads.

## Validation status

The UI changes are committed, but a full gameplay test has not been possible in this environment because the required mirror data is not present in the repository. Actual browser gameplay, touch input on a phone, GPU compatibility, and frame-rate behavior still need testing on a machine with the complete local data set.

## Credits and provenance

The original archived snapshot credits its upstream collector and links to the separate V2 project:
https://github.com/SebasKitten/Grand-V

This fork preserves the original snapshot's provenance notes. It is an independent enhancement, not an official GTA V or GTA VI release.