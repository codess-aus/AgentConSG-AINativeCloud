"""Publish the original slide assets without keeping a second copy in docs."""

from pathlib import Path

from mkdocs.structure.files import File


def on_files(files, config):
    assets = Path(config.config_file_path).parent / "assets"
    for image in sorted(assets.glob("*.png")):
        files.append(
            File(
                f"assets/{image.name}",
                str(assets.parent),
                config.site_dir,
                config.use_directory_urls,
            )
        )
    return files
