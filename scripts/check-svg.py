#!/usr/bin/env python3
"""Validate core visualizer-design SVG rules without external dependencies."""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


DISALLOWED_PATTERNS = {
    "comments": re.compile(r"<!--"),
    "blur/filter": re.compile(r"\b(filter|blur|drop-shadow)\s*[:=]", re.I),
    "doctype/html wrapper": re.compile(r"<!DOCTYPE|<html\b|<head\b|<body\b", re.I),
    "position fixed": re.compile(r"position\s*:\s*fixed", re.I),
    "emoji-like codepoint": re.compile(r"[\U0001F300-\U0001FAFF]"),
}

FONT_SIZE_RE = re.compile(r"font-size\s*:\s*([0-9.]+)px", re.I)
STYLE_FONT_RE = re.compile(r"\.([A-Za-z0-9_-]+)\s*\{[^}]*font-size\s*:\s*([0-9.]+)px", re.I)


def strip_ns(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def parse_style_classes(text: str) -> dict[str, float]:
    classes: dict[str, float] = {}
    for name, size in STYLE_FONT_RE.findall(text):
        classes[name] = float(size)
    return classes


def style_font_size(style: str | None) -> float | None:
    if not style:
        return None
    match = FONT_SIZE_RE.search(style)
    return float(match.group(1)) if match else None


def class_font_size(class_attr: str | None, classes: dict[str, float]) -> float | None:
    if not class_attr:
        return None
    sizes = [classes[name] for name in class_attr.split() if name in classes]
    return min(sizes) if sizes else None


def validate(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    for label, pattern in DISALLOWED_PATTERNS.items():
        if pattern.search(text):
            errors.append(f"Disallowed {label} found.")

    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        return [f"Invalid XML: {exc}"]

    if strip_ns(root.tag) != "svg":
        errors.append("Root element must be <svg>.")

    view_box = root.attrib.get("viewBox", "")
    if not re.fullmatch(r"0 0 680 [1-9][0-9]*", view_box):
        errors.append('viewBox must match "0 0 680 H".')

    if root.attrib.get("role") != "img":
        errors.append('Root <svg> must include role="img".')

    children = list(root)
    child_tags = [strip_ns(child.tag) for child in children]
    if "title" not in child_tags[:3] or "desc" not in child_tags[:4]:
        errors.append("<title> and <desc> should appear near the start of the SVG.")

    class_sizes = parse_style_classes(text)
    marker_ids = {node.attrib.get("id") for node in root.iter() if strip_ns(node.tag) == "marker"}
    uses_arrow = False

    for node in root.iter():
        tag = strip_ns(node.tag)
        if tag in {"path", "polyline"}:
            marker_attrs = " ".join(value for key, value in node.attrib.items() if key.startswith("marker"))
            if marker_attrs:
                uses_arrow = True
            class_attr = node.attrib.get("class", "")
            is_connector = marker_attrs or "arr" in class_attr.split() or "leader" in class_attr.split()
            if is_connector and node.attrib.get("fill") != "none":
                errors.append(f"<{tag}> connector must include fill=\"none\".")

        if tag == "text":
            if "dominant-baseline" not in node.attrib:
                errors.append("<text> should include dominant-baseline.")
            if "text-anchor" not in node.attrib:
                errors.append("<text> should include text-anchor.")

        size = style_font_size(node.attrib.get("style"))
        size = size if size is not None else class_font_size(node.attrib.get("class"), class_sizes)
        if size is not None and size < 11:
            errors.append(f"font-size below 11px found: {size:g}px.")

    if uses_arrow and "arrow" not in marker_ids:
        errors.append('Arrow connectors require <marker id="arrow"> in <defs>.')

    return sorted(set(errors))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate visualizer-design SVG rules.")
    parser.add_argument("svg", type=Path)
    args = parser.parse_args()

    errors = validate(args.svg)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: {args.svg}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
