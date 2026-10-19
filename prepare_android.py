#!/usr/bin/env python3
"""Prepare the flat Polito package as a standard Android Studio/GitHub Actions project.
Run from the directory containing this script: python3 prepare_android.py
"""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent

def copy(src: str, dst: str) -> None:
    source = ROOT / src
    target = ROOT / dst
    if not source.is_file():
        raise FileNotFoundError(f"Required project file is missing: {src}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)

# Android Gradle requires these standard directories. They are created only when
# the user prepares/builds the project; the distributed ZIP itself is flat.
copy("app-build.gradle.kts", "app/build.gradle.kts")
copy("AndroidManifest.xml", "app/src/main/AndroidManifest.xml")
copy("MainActivity.kt", "app/src/main/java/ir/polito/finance/MainActivity.kt")
copy("android.yml", ".github/workflows/android.yml")
print("Polito Android project structure created successfully.")
print("Open this folder in Android Studio, or commit the generated .github/workflows/android.yml to enable GitHub Actions.")
