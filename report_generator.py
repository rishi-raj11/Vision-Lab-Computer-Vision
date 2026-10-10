from pathlib import Path

def save_report(stats, methods, output_path):
    """Write a readable text report of the analysis run."""
    lines = [
        "VISIONLAB IMAGE ANALYSIS REPORT",
        "=" * 32,
        "",
        "Image statistics:",
    ]
    lines.extend(f"- {key.replace('_', ' ').title()}: {value}" for key, value in stats.items())
    lines += ["", "Edge methods executed: " + ", ".join(methods), "",
              "Note: Edge maps are algorithmic outputs and may need threshold tuning for different images."]
    Path(output_path).write_text("\\n".join(lines) + "\\n", encoding="utf-8")
