# -*- coding: utf-8 -*-
"""Install Dependencies - pip install -r requirements.txt"""

import subprocess
import sys
from pathlib import Path

from utils.ui import print_success, print_error, print_info, show_install_result_table


def action_install_dependencies():
    """Run pip install -r requirements.txt"""
    print_info("Installing dependencies from requirements.txt...")

    base_dir = Path(__file__).parent.parent
    req_file = base_dir / "requirements.txt"

    if not req_file.exists():
        print_error("requirements.txt not found")
        return

    packages = []
    with open(req_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                pkg = line.split(">=")[0].split("==")[0].strip()
                packages.append(pkg)

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", str(req_file), "-q"],
            capture_output=True,
            text=True,
            timeout=120,
            cwd=str(base_dir),
        )
        success = result.returncode == 0
        show_install_result_table(packages, success)
        if success:
            print_success("All dependencies installed successfully")
        else:
            err = result.stderr[:200] if result.stderr else "Unknown error"
            print_error(f"Install failed: {err}")
    except subprocess.TimeoutExpired:
        print_error("Install timed out (120s)")
    except Exception as e:
        print_error(f"Install error: {e}")
