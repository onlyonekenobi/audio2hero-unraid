# GitHub Setup Guide

## Current Status

This repository is already connected to GitHub. To push your changes:

## Step 1: Add All New Files

```bash
cd audio2hero

# Add all new files and modifications
git add .

# Or add specific files:
git add .gitignore
git add app.py audio2hero.py mergeoggs.py
git add Dockerfile docker-compose*.yml .dockerignore
git add *.md *.sh *.ps1
```

## Step 2: Commit Changes

```bash
git commit -m "Add Docker support and Unraid deployment setup

- Add Dockerfile and docker-compose configurations
- Add comprehensive setup guides for Windows, WSL, and Unraid
- Fix audio format handling in mergeoggs.py
- Update app.py for Docker environment variables
- Add helper scripts for setup and deployment"
```

## Step 3: Push to GitHub

```bash
git push origin main
```

## If You Need to Create a New Repository

If you want to create a new repository instead:

1. **Create a new repository on GitHub:**
   - Go to https://github.com/new
   - Name it (e.g., `audio2hero-docker` or `audio2hero-unraid`)
   - Don't initialize with README (we already have files)

2. **Update the remote:**
   ```bash
   git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   ```

3. **Push:**
   ```bash
   git push -u origin main
   ```

## What Will Be Committed

### New Files:
- Docker configuration files (Dockerfile, docker-compose files)
- Setup guides (Windows, WSL, Unraid)
- Helper scripts (build, run, setup scripts)
- Documentation updates

### Modified Files:
- `.gitignore` - Updated to exclude generated files
- `app.py` - Added Docker environment variable support
- `audio2hero.py` - Added environment variable for output directory
- `mergeoggs.py` - Fixed to auto-detect audio formats

### Excluded (via .gitignore):
- `Outputs/` - Generated files
- `venv/` - Python virtual environment
- `__pycache__/` - Python cache
- Large data files and models

