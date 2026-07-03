#!/usr/bin/env python3
"""Generate OP36 keymap SVG and draw.io diagrams."""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path


SVG_WIDTH = 820
LAYER_STEP_Y = 330
BOTTOM_MARGIN = 58
KEY_W = 48
KEY_H = 42
KEY_CENTER_X = KEY_W / 2
KEY_CENTER_Y = KEY_H / 2
ASSETS_DIR = Path(__file__).parent / "assets"
SVG_PATH = ASSETS_DIR / "op36-layout.svg"
DRAWIO_PATH = ASSETS_DIR / "op36-layout.drawio"


@dataclass(frozen=True)
class Key:
    label: str = ""
    sub: str = ""
    style: str = "normal"


@dataclass(frozen=True)
class Layer:
    id: str
    name: str
    bar: str
    note: str
    keys: list[Key]
    combo: str = ""


def k(label: str, sub: str = "", style: str = "normal") -> Key:
    return Key(label, sub, style)


def empty(label: str = "", sub: str = "") -> Key:
    return Key(label, sub, "empty")


KEY_POSITIONS = [
    (80, 110, 0),
    (132, 85, 0),
    (184, 70, 0),
    (236, 85, 0),
    (288, 93, 0),
    (484, 93, 0),
    (536, 85, 0),
    (588, 70, 0),
    (640, 85, 0),
    (692, 110, 0),
    (80, 156, 0),
    (132, 131, 0),
    (184, 116, 0),
    (236, 131, 0),
    (288, 139, 0),
    (484, 139, 0),
    (536, 131, 0),
    (588, 116, 0),
    (640, 131, 0),
    (692, 156, 0),
    (80, 202, 0),
    (132, 177, 0),
    (184, 162, 0),
    (236, 177, 0),
    (288, 185, 0),
    (484, 185, 0),
    (536, 177, 0),
    (588, 162, 0),
    (640, 177, 0),
    (692, 202, 0),
    (242, 252, 0),
    (300, 267, 15),
    (360, 284, 25),
    (464, 284, -25),
    (524, 267, -15),
    (582, 252, 0),
]


LAYERS = [
    Layer(
        id="base-layer",
        name="Base",
        bar="bar-base",
        note="QWERTY with balanced home row mods",
        combo="Combos: D+K Esc | A+; Caps | E+I Lang | U+P Adj L | Q+R Adj R | Z+/ Plain",
        keys=[
            k("Q"),
            k("W"),
            k("E"),
            k("R"),
            k("T"),
            k("Y"),
            k("U"),
            k("I"),
            k("O"),
            k("P"),
            k("A", "Sft"),
            k("S", "Ctl"),
            k("D", "Gui"),
            k("F", "Alt"),
            k("G"),
            k("H"),
            k("J", "Alt"),
            k("K", "Gui"),
            k("L", "Ctl"),
            k(";", "Sft"),
            k("Z"),
            k("X"),
            k("C"),
            k("V"),
            k("B"),
            k("N"),
            k("M"),
            k(","),
            k("."),
            k("/"),
            empty(),
            k("Sym", style="layer-red"),
            k("Space", style="special"),
            k("Enter", style="special"),
            k("Nav", style="layer-gold"),
            empty(),
        ],
    ),
    Layer(
        id="plain-base-layer",
        name="Base plain",
        bar="bar-base",
        note="Toggle Z+/ combo; QWERTY without home row mods",
        keys=[
            k("Q"),
            k("W"),
            k("E"),
            k("R"),
            k("T"),
            k("Y"),
            k("U"),
            k("I"),
            k("O"),
            k("P"),
            k("A"),
            k("S"),
            k("D"),
            k("F"),
            k("G"),
            k("H"),
            k("J"),
            k("K"),
            k("L"),
            k(";"),
            k("Z"),
            k("X"),
            k("C"),
            k("V"),
            k("B"),
            k("N"),
            k("M"),
            k(","),
            k("."),
            k("/"),
            empty(),
            k("Sym", style="layer-red"),
            k("Space", style="special"),
            k("Enter", style="special"),
            k("Nav", style="layer-gold"),
            empty(),
        ],
    ),
    Layer(
        id="symbols-layer",
        name="Symbols",
        bar="bar-sym",
        note="Hold left thumb from Base",
        keys=[
            k("!"),
            k("@"),
            k("#"),
            k("$"),
            k("%"),
            empty(),
            k("&"),
            k("*"),
            k("("),
            k(")"),
            k("Esc", "Sft", "special"),
            k("LCtl"),
            k("LGui"),
            k("LAlt"),
            k("^"),
            k("-"),
            k("=", "Alt"),
            k("{", "Gui"),
            k("}", "Ctl"),
            k("'", "Sft"),
            k("Tab", style="special"),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            k("Bspc", style="special"),
            k("["),
            k("]"),
            k("\\"),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
        ],
    ),
    Layer(
        id="nav-layer",
        name="Nav",
        bar="bar-nav",
        note="Hold right thumb from Base",
        keys=[
            k("1"),
            k("2"),
            k("3"),
            k("4"),
            k("5"),
            k("6"),
            k("7"),
            k("8"),
            k("9"),
            k("0"),
            k("LSft"),
            k("LCtl"),
            k("LGui"),
            k("LAlt"),
            k("6"),
            k("Left", style="special"),
            k("Down", "Alt", "special"),
            k("Up", "Gui", "special"),
            k("Right", "Ctl", "special"),
            k("RSft"),
            k("`"),
            empty(),
            empty(),
            k("Del", style="special"),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
        ],
    ),
    Layer(
        id="adjust-left-layer",
        name="Adjust L",
        bar="bar-adj",
        note="Hold U+P combo",
        keys=[
            k("F1"),
            k("F2"),
            k("F3"),
            k("F4"),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            k("F5"),
            k("F6"),
            k("F7"),
            k("F8"),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            k("F9"),
            k("F10"),
            k("F11"),
            k("F12"),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
        ],
    ),
    Layer(
        id="adjust-right-layer",
        name="Adjust R",
        bar="bar-adj",
        note="Hold Q+R combo",
        keys=[
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            k("Vol-", style="special"),
            k("Mute", style="special"),
            k("Vol+", style="special"),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            k("BT", "0", "layer-blue"),
            k("Prev", style="special"),
            k("Play", style="special"),
            k("Next", style="special"),
            k("BT", "CLR", "layer-blue"),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
            empty(),
        ],
    ),
]


STYLE_TO_USE = {
    "normal": "key-normal",
    "special": "key-special",
    "empty": "key-empty",
    "layer-red": "key-layer-red",
    "layer-gold": "key-layer-gold",
    "layer-blue": "key-layer-blue",
}


DRAWIO_STYLE = {
    "normal": "rounded=1;whiteSpace=wrap;html=1;arcSize=12;fillColor=#383e47;strokeColor=#05070a;fontColor=#edf2f7;fontStyle=1;fontSize=13;align=center;verticalAlign=middle;",
    "special": "rounded=1;whiteSpace=wrap;html=1;arcSize=12;fillColor=#495566;strokeColor=#121820;fontColor=#edf2f7;fontStyle=1;fontSize=11;align=center;verticalAlign=middle;",
    "empty": "rounded=1;whiteSpace=wrap;html=1;arcSize=12;fillColor=#202833;strokeColor=#596170;dashed=1;dashPattern=4 4;fontColor=#edf2f7;fontStyle=1;fontSize=10;align=center;verticalAlign=middle;",
    "layer-red": "rounded=1;whiteSpace=wrap;html=1;arcSize=12;fillColor=#a20025;strokeColor=#6f0000;fontColor=#edf2f7;fontStyle=1;fontSize=13;align=center;verticalAlign=middle;",
    "layer-gold": "rounded=1;whiteSpace=wrap;html=1;arcSize=12;fillColor=#d9a725;strokeColor=#b08312;fontColor=#111820;fontStyle=1;fontSize=13;align=center;verticalAlign=middle;",
    "layer-blue": "rounded=1;whiteSpace=wrap;html=1;arcSize=12;fillColor=#5c8cca;strokeColor=#456893;fontColor=#111820;fontStyle=1;fontSize=11;align=center;verticalAlign=middle;",
}


def svg_height() -> int:
    return len(LAYERS) * LAYER_STEP_Y + BOTTOM_MARGIN


def assert_layout() -> None:
    expected = len(KEY_POSITIONS)
    for layer in LAYERS:
        if len(layer.keys) != expected:
            raise ValueError(f"{layer.id} has {len(layer.keys)} keys, expected {expected}")


def text_class(key: Key) -> str:
    if key.style in {"layer-gold", "layer-blue"}:
        return "key-text-dark-small" if key.sub or len(key.label) > 3 else "key-text-dark"
    if key.style == "special" and len(key.label) > 3:
        return "key-text-small"
    if len(key.label) > 3:
        return "key-text-small"
    return "key-text"


def svg_key(key: Key, x: int, y: int, rotation: int) -> str:
    transform = f"translate({x} {y})"
    if rotation:
        transform += f" rotate({rotation} {KEY_CENTER_X:g} {KEY_CENTER_Y:g})"

    label = escape(key.label)
    sub = escape(key.sub)
    use = STYLE_TO_USE[key.style]
    if not key.label:
        text = ""
    elif key.sub:
        text = (
            f'<text class="{text_class(key)}" x="{KEY_CENTER_X:g}" y="18">{label}</text>'
            f'<text class="key-subtext" x="{KEY_CENTER_X:g}" y="32">{sub}</text>'
        )
    else:
        text = f'<text class="{text_class(key)}" x="{KEY_CENTER_X:g}" y="{KEY_CENTER_Y:g}">{label}</text>'

    return f'<g transform="{transform}"><use href="#{use}"/>{text}</g>'


def svg_layer(layer: Layer, offset_y: int) -> str:
    lines = [
        f'<g id="{layer.id}" transform="translate(0 {offset_y})">',
        '<rect class="layer-panel" x="32" y="38" width="756" height="274" rx="18"/>',
        f'<rect class="{layer.bar}" x="52" y="54" width="6" height="242" rx="3"/>',
        f'<text class="title-text" x="410" y="62">{escape(layer.name)}</text>',
        f'<text class="note-text" x="410" y="84">{escape(layer.note)}</text>',
        "",
    ]
    for idx, key in enumerate(layer.keys):
        x, y, rotation = KEY_POSITIONS[idx]
        lines.append(svg_key(key, x, y, rotation))
        if idx in {9, 19, 29}:
            lines.append("")
    if layer.combo:
        lines.append(f'<text class="combo-text" x="410" y="298">{escape(layer.combo)}</text>')
    lines.append("</g>")
    return "\n".join(lines)


def generate_svg() -> str:
    assert_layout()
    layers = "\n\n".join(svg_layer(layer, idx * LAYER_STEP_Y) for idx, layer in enumerate(LAYERS))
    height = svg_height()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{SVG_WIDTH}" height="{height}" viewBox="0 0 {SVG_WIDTH} {height}" role="img" aria-labelledby="title desc">
<title id="title">OP36 keymap layout</title>
<desc id="desc">Six-layer layout diagram for the Ergohaven OP36 ZMK keymap.</desc>
<defs>
  <rect id="key-normal" class="key-normal" width="{KEY_W}" height="{KEY_H}" rx="7"/>
  <rect id="key-layer-red" class="key-layer-red" width="{KEY_W}" height="{KEY_H}" rx="7"/>
  <rect id="key-layer-gold" class="key-layer-gold" width="{KEY_W}" height="{KEY_H}" rx="7"/>
  <rect id="key-layer-blue" class="key-layer-blue" width="{KEY_W}" height="{KEY_H}" rx="7"/>
  <rect id="key-special" class="key-special" width="{KEY_W}" height="{KEY_H}" rx="7"/>
  <rect id="key-empty" class="key-empty" width="{KEY_W}" height="{KEY_H}" rx="7"/>
</defs>
<style>
  .sheet {{ fill: #10141b; }}
  .layer-panel {{ fill: #151b24; stroke: #293241; stroke-width: 1; }}
  .bar-base {{ fill: #3f4a59; stroke: #556173; }}
  .bar-sym {{ fill: #a20025; stroke: #6f0000; }}
  .bar-nav {{ fill: #d9a725; stroke: #b08312; }}
  .bar-adj {{ fill: #5c8cca; stroke: #456893; }}
  .key-normal {{ fill: #383e47; stroke: #05070a; stroke-width: 1; }}
  .key-layer-red {{ fill: #a20025; stroke: #6f0000; stroke-width: 1; }}
  .key-layer-gold {{ fill: #d9a725; stroke: #b08312; stroke-width: 1; }}
  .key-layer-blue {{ fill: #5c8cca; stroke: #456893; stroke-width: 1; }}
  .key-special {{ fill: #495566; stroke: #121820; stroke-width: 1; }}
  .key-empty {{ fill: #202833; stroke: #596170; stroke-width: 1; stroke-dasharray: 4 4; }}
  .title-text {{ fill: #ffffff; font: 700 16px Verdana, Arial, sans-serif; text-anchor: middle; dominant-baseline: middle; }}
  .note-text {{ fill: #aeb8c6; font: 12px Verdana, Arial, sans-serif; text-anchor: middle; dominant-baseline: middle; }}
  .combo-text {{ fill: #aeb8c6; font: 11px Verdana, Arial, sans-serif; text-anchor: middle; dominant-baseline: middle; }}
  .key-text {{ fill: #edf2f7; font: 700 13px Verdana, Arial, sans-serif; text-anchor: middle; dominant-baseline: middle; }}
  .key-text-small {{ fill: #edf2f7; font: 700 10px Verdana, Arial, sans-serif; text-anchor: middle; dominant-baseline: middle; }}
  .key-text-dark {{ fill: #111820; font: 700 13px Verdana, Arial, sans-serif; text-anchor: middle; dominant-baseline: middle; }}
  .key-text-dark-small {{ fill: #111820; font: 700 10px Verdana, Arial, sans-serif; text-anchor: middle; dominant-baseline: middle; }}
  .key-subtext {{ fill: #cbd5e1; font: 9px Verdana, Arial, sans-serif; text-anchor: middle; dominant-baseline: middle; }}
</style>
<rect class="sheet" x="0" y="0" width="{SVG_WIDTH}" height="{height}"/>
{layers}
</svg>
'''


def drawio_value(key: Key) -> str:
    if not key.label:
        return ""
    if key.sub:
        return f"{escape(key.label)}&lt;br&gt;&lt;font style=&quot;font-size: 9px;&quot;&gt;{escape(key.sub)}&lt;/font&gt;"
    return escape(key.label)


def mx_cell(cell_id: str, value: str, style: str, x: int, y: int, w: int, h: int, parent: str = "1") -> str:
    return (
        f'<mxCell id="{cell_id}" value="{value}" style="{style}" vertex="1" parent="{parent}">'
        f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>'
        "</mxCell>"
    )


def generate_drawio() -> str:
    assert_layout()
    height = svg_height()
    cells = [
        '<mxCell id="0"/>',
        '<mxCell id="1" parent="0"/>',
    ]
    for layer_idx, layer in enumerate(LAYERS):
        offset_y = layer_idx * LAYER_STEP_Y
        layer_id = f"layer-{layer_idx}"
        cells.append(
            mx_cell(
                f"{layer_id}-panel",
                "",
                "rounded=1;whiteSpace=wrap;html=1;arcSize=8;fillColor=#151b24;strokeColor=#293241;",
                32,
                offset_y + 38,
                756,
                274,
            )
        )
        cells.append(
            mx_cell(
                f"{layer_id}-title",
                escape(layer.name),
                "text;html=1;strokeColor=none;fillColor=none;fontColor=#ffffff;fontSize=16;fontStyle=1;align=center;verticalAlign=middle;",
                328,
                offset_y + 48,
                164,
                24,
            )
        )
        cells.append(
            mx_cell(
                f"{layer_id}-note",
                escape(layer.note),
                "text;html=1;strokeColor=none;fillColor=none;fontColor=#aeb8c6;fontSize=12;align=center;verticalAlign=middle;",
                210,
                offset_y + 70,
                400,
                24,
            )
        )
        if layer.combo:
            cells.append(
                mx_cell(
                    f"{layer_id}-combo",
                    escape(layer.combo),
                    "text;html=1;strokeColor=none;fillColor=none;fontColor=#aeb8c6;fontSize=11;align=center;verticalAlign=middle;",
                    118,
                    offset_y + 284,
                    584,
                    20,
                )
            )
        for key_idx, key in enumerate(layer.keys):
            x, y, _rotation = KEY_POSITIONS[key_idx]
            cells.append(
                mx_cell(
                    f"{layer_id}-key-{key_idx}",
                    drawio_value(key),
                    DRAWIO_STYLE[key.style],
                    x,
                    offset_y + y,
                    KEY_W,
                    KEY_H,
                )
            )

    return f'''<mxfile host="app.diagrams.net" modified="2026-07-03T00:00:00.000Z" agent="Cursor" version="24.7.17">
  <diagram id="op36-keymap" name="OP36 keymap">
    <mxGraphModel dx="1422" dy="794" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{SVG_WIDTH}" pageHeight="{height}" math="0" shadow="0">
      <root>
        {"".join(cells)}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
'''


def main() -> None:
    ASSETS_DIR.mkdir(exist_ok=True)
    SVG_PATH.write_text(generate_svg(), encoding="utf-8")
    DRAWIO_PATH.write_text(generate_drawio(), encoding="utf-8")
    print(f"Wrote {SVG_PATH}")
    print(f"Wrote {DRAWIO_PATH}")


if __name__ == "__main__":
    main()
