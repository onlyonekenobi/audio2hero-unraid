# WSL Installation Script for Audio2Hero
# Run this script as Administrator

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "WSL Installation for Audio2Hero" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if running as administrator
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "ERROR: This script must be run as Administrator!" -ForegroundColor Red
    Write-Host ""
    Write-Host "To run as Administrator:" -ForegroundColor Yellow
    Write-Host "1. Right-click on PowerShell" -ForegroundColor Yellow
    Write-Host "2. Select 'Run as Administrator'" -ForegroundColor Yellow
    Write-Host "3. Navigate to this folder and run: .\install_wsl.ps1" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Or run this command in an elevated PowerShell:" -ForegroundColor Yellow
    Write-Host "wsl --install" -ForegroundColor White
    exit 1
}

Write-Host "Checking WSL status..." -ForegroundColor Green
$wslStatus = wsl --status 2>&1

if ($LASTEXITCODE -eq 0) {
    Write-Host "WSL appears to be installed!" -ForegroundColor Green
    Write-Host "Checking installed distributions..." -ForegroundColor Green
    wsl --list --verbose
    Write-Host ""
    Write-Host "If you see a distribution listed above, WSL is ready!" -ForegroundColor Green
    Write-Host "If not, continue with installation below." -ForegroundColor Yellow
    Write-Host ""
} else {
    Write-Host "WSL is not installed. Proceeding with installation..." -ForegroundColor Yellow
}

Write-Host "Installing WSL..." -ForegroundColor Green
Write-Host "This will install WSL and Ubuntu by default." -ForegroundColor Yellow
Write-Host ""

$response = Read-Host "Do you want to proceed? (Y/N)"
if ($response -ne "Y" -and $response -ne "y") {
    Write-Host "Installation cancelled." -ForegroundColor Yellow
    exit 0
}

Write-Host ""
Write-Host "Running: wsl --install" -ForegroundColor Cyan
wsl --install

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "Installation initiated successfully!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "IMPORTANT: You need to RESTART your computer for WSL to complete installation." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "After restart:" -ForegroundColor Cyan
    Write-Host "1. Ubuntu will launch automatically" -ForegroundColor White
    Write-Host "2. Create a Linux username and password" -ForegroundColor White
    Write-Host "3. Then run the setup script in WSL:" -ForegroundColor White
    Write-Host "   cd /mnt/c/Users/Luke/Documents/Cursor/audio2hero" -ForegroundColor Gray
    Write-Host "   bash setup_wsl.sh" -ForegroundColor Gray
    Write-Host ""
    
    $restart = Read-Host "Would you like to restart now? (Y/N)"
    if ($restart -eq "Y" -or $restart -eq "y") {
        Write-Host "Restarting in 5 seconds..." -ForegroundColor Yellow
        Start-Sleep -Seconds 5
        Restart-Computer
    } else {
        Write-Host "Please restart manually when ready." -ForegroundColor Yellow
    }
} else {
    Write-Host ""
    Write-Host "Installation encountered an error." -ForegroundColor Red
    Write-Host "You may need to:" -ForegroundColor Yellow
    Write-Host "1. Enable Virtual Machine Platform in Windows Features" -ForegroundColor White
    Write-Host "2. Or install Ubuntu manually from Microsoft Store" -ForegroundColor White
    Write-Host ""
    Write-Host "See WSL_INSTALL_GUIDE.md for alternative methods." -ForegroundColor Cyan
}




