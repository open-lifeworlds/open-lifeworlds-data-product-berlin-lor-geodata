import json
import os

from lib.tracking_decorator import TrackingDecorator


@TrackingDecorator.track_time
def copy_data(source_path, results_path, clean=False, quiet=False):
    # Iterate over files
    for subdir, dirs, files in os.walk(source_path):
        for file_name in files:
            subdir = subdir.replace(f"{source_path}/", "")

            # Make results path
            os.makedirs(os.path.join(results_path, subdir), exist_ok=True)

            source_file_path = os.path.join(source_path, subdir, file_name)
            results_file_path = os.path.join(results_path, subdir, file_name)

            # Check if file needs to be copied
            if clean or not os.path.exists(results_file_path):
                with open(source_file_path, "r") as geojson_file:
                    geojson = json.load(geojson_file)

                with open(results_file_path, "w") as geojson_file:
                    json.dump(geojson, geojson_file)

                    if not quiet:
                        print(f"✓ Copy {results_file_path}")
            else:
                print(f"✓ Already exists {results_file_path}")