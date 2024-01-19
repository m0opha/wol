#!/bin/bash

build_binary() {

    local pythonfile="$1"

    if ! command -v pyinstaller &> /dev/null; then
        echo "PyInstaller is not installed. Installing..."
        pip install pyinstaller
        echo "PyInstaller installed successfully."
    else
        echo "PyInstaller is already installed."
    fi

    pyinstaller --noconfirm --noupx --nowindow --console --onefile -i NONE $pythonfile
}


while [[ "$#" -gt 0 ]]; do
    case "$1" in            
        -b|--build)
            echo "Building a binary of the project with pyinstaller..."
            build_binary "wol.py"
            exit 0
            ;;
        --size|-s)
            du -sh ./dist/wol
            ;;

        -r|--run)
         
            echo "Running app..."
            ./dist/wol
            exit 0
            ;;
        *)
            echo "Invalid option: $1" >&2
            exit 1
            ;;
    esac
    shift
done