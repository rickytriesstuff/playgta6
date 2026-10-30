# PlayGTA6: Open City

An original, self-contained browser-based open-city driving sandbox. This project is an independent game and is not affiliated with Rockstar Games.

## No external game data required

The playable prototype is built into `index.html`. It does not need the original mirror folder, copyrighted game assets, external downloads, a CDN, or a game-data archive.

## Play locally

1. Download or clone this repository.
2. On Windows, run `Launch-Local.cmd`.
3. The launcher opens `http://localhost:8000/`.

You can also run `python serve_local.py --open` if Python is installed. A local HTTP server is used so the game behaves consistently in browsers.

## Gameplay

- Explore a procedurally arranged city grid.
- Walk, sprint, enter vehicles, and drive around the streets.
- Traffic vehicles roam the city.
- Police patrols can pursue you as your wanted level rises.
- Find the green job marker, collect a delivery, and reach the destination to earn cash.
- On-screen HUD shows cash, wanted level, vehicle status, mission, and minimap.
- Responsive touch joystick and action buttons are included for phones and tablets.

## Controls

| Action | Keyboard | Touch |
|---|---|---|
| Move / steer | WASD or arrow keys | Left joystick |
| Sprint / accelerate | Shift | RUN |
| Enter / exit vehicle | E | ENTER |
| Interact with mission | F | Approach marker and use keyboard |
| Brake | Space | BRAKE |
| Horn | Not assigned | HORN |

## Technical notes

- Rendering uses the browser Canvas 2D API.
- World generation and game logic run locally in the browser.
- No backend, login, account, or network access is needed for the prototype.
- This is an original compact sandbox prototype, not a port of GTA V or GTA VI.