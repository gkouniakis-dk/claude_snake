# Snake Game

A classic Snake game built with Python and Pygame, featuring progressive difficulty levels.

## Game Features

- **Progressive Difficulty**: Speed increases every 10 food items
- **Level System**: Track your progress as you advance
- **Score Tracking**: Compete for high scores
- **Clean Graphics**: Grid-based design with smooth movement
- **Collision Detection**: Game over when hitting walls or yourself

## Controls

- **Arrow Keys**: Move the snake (Up, Down, Left, Right)
- **Space**: Restart after game over

## Download and Play

### Pre-built Executables (No Python Required!)

Download the latest executables from the [Releases](../../releases) page:
- **Windows**: Download `SnakeGame.exe` and double-click to play
- **macOS**: Download `SnakeGame` and double-click to play

The executables are automatically built for both platforms using GitHub Actions.

---

## For Developers

### Running from Source

#### Prerequisites
- Python 3.11 or higher
- pip

#### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/claude_snake.git
cd claude_snake
```

2. Create a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the game:
```bash
python snake_game.py
```

### Building Executables Locally

#### Windows:
```bash
pyinstaller --onefile --windowed --name "SnakeGame" snake_game.py
```
The executable will be in `dist/SnakeGame.exe`

#### macOS:
```bash
pyinstaller --onefile --windowed --name "SnakeGame" snake_game.py
```
The executable will be in `dist/SnakeGame`

---

## GitHub Actions - Automatic Builds

This repository is configured with GitHub Actions to automatically build executables for both Windows and macOS whenever you push code.

### How It Works

1. **Push your code** to the `main` or `master` branch
2. **GitHub Actions automatically**:
   - Builds a Windows .exe file
   - Builds a macOS executable
   - Creates downloadable artifacts
   - (Optional) Creates a release with both files

3. **Download the builds**:
   - Go to the "Actions" tab in your GitHub repository
   - Click on the latest workflow run
   - Scroll down to "Artifacts"
   - Download `SnakeGame-Windows` or `SnakeGame-macOS`

### Setting Up Your GitHub Repository

#### Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top-right and select "New repository"
3. Name it `claude_snake` (or whatever you prefer)
4. Choose Public or Private
5. **Don't** initialize with README (we already have one)
6. Click "Create repository"

#### Step 2: Push Your Code

In your project directory, run these commands:

```bash
# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Create your first commit
git commit -m "Initial commit: Snake game with level system"

# Add your GitHub repository as remote
# Replace YOUR_USERNAME with your actual GitHub username
git remote add origin https://github.com/YOUR_USERNAME/claude_snake.git

# Push to GitHub
git push -u origin main
```

**Note**: If you get an error about "master" vs "main", try:
```bash
git branch -M main
git push -u origin main
```

#### Step 3: Watch the Magic Happen!

1. Go to your repository on GitHub
2. Click the "Actions" tab
3. You should see a workflow running
4. Wait a few minutes for it to complete
5. Download your executables from the artifacts!

### Manual Build Trigger

You can also manually trigger a build:
1. Go to the "Actions" tab
2. Click on "Build Snake Game Executables"
3. Click "Run workflow"
4. Select the branch and click "Run workflow"

---

## Project Structure

```
claude_snake/
├── snake_game.py          # Main game file
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── BUILD_INSTRUCTIONS.md # Detailed build instructions
└── .github/
    └── workflows/
        └── build.yml     # GitHub Actions configuration
```

---

## Troubleshooting

### "Python not found" error
Make sure Python 3.11+ is installed and added to your PATH.

### Antivirus warnings on Windows
PyInstaller executables are sometimes flagged by antivirus software. This is a false positive. You can add an exception or build from source.

### macOS "App can't be opened" error
Right-click the app and select "Open" the first time you run it.

---

## License

Feel free to use and modify this game however you like!

---

## Credits

Built with:
- [Python](https://www.python.org/)
- [Pygame](https://www.pygame.org/)
- [PyInstaller](https://www.pyinstaller.org/)
- [GitHub Actions](https://github.com/features/actions)
