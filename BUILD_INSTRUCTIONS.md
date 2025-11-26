# Snake Game - Build and Distribution Instructions

## Windows Executable (Already Created!)

Your Windows executable is ready to share:
- **Location**: `dist/SnakeGame.exe` (15 MB)
- **How to share**: Simply copy the `SnakeGame.exe` file and send it to anyone with Windows
- **No Python required**: The executable is completely standalone

### Testing the Windows executable:
1. Navigate to the `dist` folder
2. Double-click `SnakeGame.exe`
3. The game should launch immediately!

---

## macOS Executable (Build on a Mac)

To create a macOS version, you'll need to run the following commands **on a Mac computer**:

### Step 1: Set up the environment
```bash
# Clone or copy your project to the Mac
cd path/to/claude_snake

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install pygame pyinstaller
```

### Step 2: Build the macOS executable
```bash
# Build as a single application bundle
pyinstaller --onefile --windowed --name "SnakeGame" snake_game.py
```

### Step 3: Find and share the executable
- The macOS app will be in: `dist/SnakeGame` (or `dist/SnakeGame.app`)
- You can zip this file and share it with Mac users
- Recipients can simply double-click to play (no Python needed)

---

## Rebuilding (if you make changes to the game)

### For Windows:
```bash
# Activate virtual environment
venv\Scripts\activate

# Rebuild
pyinstaller --onefile --windowed --name "SnakeGame" snake_game.py

# The new executable will be in dist/SnakeGame.exe
```

### For macOS:
```bash
# Activate virtual environment
source venv/bin/activate

# Rebuild
pyinstaller --onefile --windowed --name "SnakeGame" snake_game.py

# The new executable will be in dist/SnakeGame or dist/SnakeGame.app
```

---

## PyInstaller Options Explained

- `--onefile`: Packages everything into a single executable file
- `--windowed`: Hides the console window (cleaner for GUI apps)
- `--name "SnakeGame"`: Sets the name of the output file

---

## Game Controls

- **Arrow Keys**: Move the snake (Up, Down, Left, Right)
- **Space**: Restart after game over

## Game Features

- Progressive difficulty: Speed increases every 10 food items
- Level system: Track your progress
- Score tracking
- Collision detection with walls and self

---

## Troubleshooting

### Windows Antivirus Warning
Some antivirus software may flag PyInstaller executables as suspicious. This is a false positive. You can:
1. Add an exception in your antivirus
2. Use `--icon` to add a custom icon (makes it look more professional)

### File Size
The executable is ~15 MB because it includes:
- Python interpreter
- Pygame library
- All dependencies

This is normal for PyInstaller executables.

---

## Distribution Checklist

- [ ] Test the executable on a clean machine (one without Python installed)
- [ ] Consider adding a custom icon with `--icon=icon.ico`
- [ ] Create a zip file with the executable and this README
- [ ] Test on different Windows versions if possible (Windows 10, 11)
- [ ] For macOS, test on both Intel and Apple Silicon Macs if possible
