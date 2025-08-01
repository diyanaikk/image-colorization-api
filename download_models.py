# download_models.py

import os

def ensure_model_files_exist():
    """
    Checks if model files exist in the 'models/' directory.
    """
    required_files = [
        "models/colorization_deploy_v2.prototxt",
        "models/colorization_release_v2.caffemodel",
        "models/pts_in_hull.npy"
    ]

    missing_files = [f for f in required_files if not os.path.exists(f)]

    if missing_files:
        print("\n🔒 Missing model files detected.\n")
        print("Please manually download the following files from the official repository:")
        print("➡ https://github.com/richzhang/colorization\n")
        for file in missing_files:
            print(f" - {file}")
        print("\nPlace them in a folder named 'models/' and rerun the app.")
    else:
        print("✅ All model files found.")
