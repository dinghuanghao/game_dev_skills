#!/usr/bin/env python3
"""Generate procedural game SFX packs from pyfxr/SFXR-style presets.

This script requires real ``pyfxr``. It fails with installation guidance if
pyfxr is unavailable, so generated assets always come from the expected SFXR
engine.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any


SAMPLE_RATE = 44_100


AXIUM_PRESETS: dict[str, dict[str, Any]] = {
    "axium_laser": {
        "base_freq": 0.61,
        "freq_limit": 0.224,
        "freq_ramp": -0.304,
        "duty": 0.656,
        "duty_ramp": -0.2,
        "env_attack": 0.0,
        "env_sustain": 0.26,
        "env_decay": 0.184,
        "pha_offset": 0.01,
        "pha_ramp": -0.132,
        "wave_type": "SQUARE",
        "volume": 0.1,
    },
    "axium_enemy_laser": {
        "base_freq": 0.46,
        "freq_limit": 0.2,
        "freq_ramp": -0.187,
        "duty": 0.88,
        "duty_ramp": -0.067,
        "env_attack": 0.0,
        "env_sustain": 0.285,
        "env_decay": 0.145,
        "env_punch": 0.043,
        "wave_type": "SQUARE",
        "volume": 0.1,
    },
    "axium_explosion": {
        "base_freq": 0.06,
        "freq_ramp": -0.011,
        "env_attack": 0.16,
        "env_sustain": 0.31,
        "env_decay": 0.67,
        "env_punch": 0.19,
        "lpf_resonance": 0.0,
        "lpf_freq": 0.31,
        "lpf_ramp": -0.15,
        "wave_type": "NOISE",
        "volume": 0.4,
    },
    "axium_explosion_small": {
        "base_freq": 0.06,
        "freq_limit": 0.0,
        "freq_ramp": 0.0,
        "freq_dramp": -0.16,
        "env_attack": 0.0,
        "env_sustain": 0.2,
        "env_decay": 0.38,
        "env_punch": 0.37,
        "pha_offset": -0.045,
        "pha_ramp": -0.197,
        "arp_speed": 0.72,
        "arp_mod": 0.404,
        "wave_type": "NOISE",
        "volume": 0.2,
    },
    "axium_powerup": {
        "base_freq": 0.241,
        "freq_ramp": 0.16,
        "vib_strength": 0.33,
        "vib_speed": 0.51,
        "env_attack": 0.0,
        "env_sustain": 0.08,
        "env_decay": 0.46,
        "pha_offset": 0.01,
        "arp_speed": 0.28,
        "arp_mod": 0.0,
        "wave_type": "SQUARE",
        "volume": 0.3,
    },
    "axium_rocket": {
        "base_freq": 0.25,
        "freq_limit": 0.07,
        "freq_ramp": 0.16,
        "freq_dramp": -0.2,
        "duty": 0.46,
        "duty_ramp": 0.06,
        "env_attack": 0.19,
        "env_sustain": 0.17,
        "env_decay": 0.51,
        "env_punch": 0.15,
        "wave_type": "NOISE",
        "volume": 0.15,
    },
    "axium_phaser": {
        "base_freq": 0.31,
        "freq_limit": 0.19,
        "freq_ramp": -0.19,
        "duty": 0.701,
        "duty_ramp": -0.192,
        "env_attack": 0.0,
        "env_sustain": 0.32,
        "env_decay": 0.16,
        "hpf_freq": 0.189,
        "wave_type": "SINE",
        "volume": 0.2,
    },
    "axium_pause": {
        "base_freq": 0.5,
        "env_attack": 0.0,
        "env_sustain": 0.29,
        "env_decay": 0.193,
        "env_punch": 0.473,
        "arp_speed": 0.58,
        "arp_mod": -0.18,
        "wave_type": "SQUARE",
        "volume": 0.3,
    },
    "axium_impact": {
        "base_freq": 0.44,
        "freq_ramp": -0.652,
        "env_attack": 0.0,
        "env_sustain": 0.098,
        "env_decay": 0.131,
        "hpf_freq": 0.197,
        "wave_type": "NOISE",
        "volume": 0.3,
    },
    "axium_placement": {
        "base_freq": 0.29,
        "freq_ramp": -0.489,
        "env_attack": 0.0,
        "env_sustain": 0.019,
        "env_decay": 0.234,
        "wave_type": "SAW",
        "volume": 0.05,
    },
    "axium_pickup": {
        "base_freq": 0.83,
        "env_attack": 0.0,
        "env_sustain": 0.039,
        "env_decay": 0.272,
        "env_punch": 0.468,
        "arp_mod": 0.253,
        "wave_type": "SQUARE",
        "volume": 0.2,
    },
}


DESIGN_PRESETS: dict[str, dict[str, Any]] = {
    "coin_chime": {
        "base_freq": 0.82,
        "env_attack": 0.0,
        "env_sustain": 0.05,
        "env_decay": 0.34,
        "env_punch": 0.52,
        "arp_speed": 0.42,
        "arp_mod": 0.31,
        "wave_type": "SQUARE",
        "volume": 0.26,
    },
    "jump_sweep": {
        "base_freq": 0.26,
        "freq_ramp": 0.34,
        "env_attack": 0.0,
        "env_sustain": 0.12,
        "env_decay": 0.18,
        "wave_type": "SQUARE",
        "volume": 0.22,
    },
    "fireball_explosion": {
        "base_freq": 0.11,
        "freq_ramp": -0.18,
        "env_attack": 0.03,
        "env_sustain": 0.33,
        "env_decay": 0.62,
        "env_punch": 0.34,
        "lpf_freq": 0.38,
        "lpf_ramp": -0.12,
        "wave_type": "NOISE",
        "volume": 0.42,
    },
    "ice_shatter": {
        "base_freq": 0.72,
        "freq_limit": 0.18,
        "freq_ramp": -0.46,
        "duty": 0.16,
        "duty_ramp": 0.08,
        "env_attack": 0.0,
        "env_sustain": 0.07,
        "env_decay": 0.24,
        "env_punch": 0.36,
        "hpf_freq": 0.2,
        "pha_offset": 0.05,
        "pha_ramp": -0.12,
        "wave_type": "SQUARE",
        "volume": 0.22,
    },
    "water_burst": {
        "base_freq": 0.18,
        "freq_ramp": -0.05,
        "env_attack": 0.02,
        "env_sustain": 0.22,
        "env_decay": 0.36,
        "env_punch": 0.18,
        "lpf_freq": 0.44,
        "hpf_freq": 0.07,
        "wave_type": "NOISE",
        "volume": 0.3,
    },
    "metal_clash": {
        "base_freq": 0.44,
        "freq_ramp": -0.652,
        "env_attack": 0.0,
        "env_sustain": 0.098,
        "env_decay": 0.131,
        "hpf_freq": 0.197,
        "pha_offset": 0.03,
        "wave_type": "SQUARE",
        "volume": 0.25,
    },
    "flying_kiss": {
        "base_freq": 0.46,
        "freq_ramp": 0.19,
        "vib_strength": 0.18,
        "vib_speed": 0.36,
        "env_attack": 0.01,
        "env_sustain": 0.08,
        "env_decay": 0.28,
        "env_punch": 0.18,
        "arp_speed": 0.34,
        "arp_mod": 0.18,
        "wave_type": "SINE",
        "volume": 0.24,
    },
}


PRESET_GROUPS = {
    "axium": AXIUM_PRESETS,
    "design": DESIGN_PRESETS,
    "all": {**AXIUM_PRESETS, **DESIGN_PRESETS},
}


def load_pyfxr():
    try:
        import pyfxr
    except Exception as exc:
        raise SystemExit(
            "pyfxr is required to render this skill's presets.\n"
            "Install it in the Python environment used to run this script, for example:\n"
            "  python -m pip install pyfxr\n"
            "If pyfxr cannot be installed for this platform/Python version, use a supported "
            "Python version with a pyfxr wheel or consider a different runtime approach such "
            "as sfxrlua or a Web Audio API generator. This skill intentionally does not "
            "fallback to another synthesis engine.\n"
            f"Original import error: {type(exc).__name__}: {exc}"
        ) from exc
    return pyfxr


def render_with_pyfxr(pyfxr, preset: dict[str, Any], output: Path) -> None:
    params = {key: value for key, value in preset.items() if key != "volume"}
    wave_type = params.get("wave_type")
    if isinstance(wave_type, str):
        params["wave_type"] = getattr(pyfxr.WaveType, wave_type)
    output.parent.mkdir(parents=True, exist_ok=True)
    pyfxr.SFX(**params).build().save(str(output))


def resolve_presets(group: str, only: list[str]) -> dict[str, dict[str, Any]]:
    presets = PRESET_GROUPS[group]
    if not only:
        return presets
    unknown = sorted(set(only) - set(presets))
    if unknown:
        raise SystemExit(f"Unknown preset(s): {', '.join(unknown)}")
    return {name: presets[name] for name in only}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--group", choices=sorted(PRESET_GROUPS), default="all")
    parser.add_argument("--preset", action="append", default=[], help="Preset to render. Repeatable.")
    parser.add_argument("--output-dir", type=Path, default=Path("generated_sfxr"))
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--manifest", action="store_true")
    parser.add_argument("--play", help="Render and play one preset with afplay.")
    args = parser.parse_args()

    presets = resolve_presets(args.group, args.preset)
    if args.list:
        print("\n".join(presets))
        return

    if args.play:
        presets = resolve_presets(args.group, [args.play])

    pyfxr = load_pyfxr()
    manifest = {}
    for name, preset in presets.items():
        output = args.output_dir / f"{name}.wav"
        render_with_pyfxr(pyfxr, preset, output)
        print(f"Wrote {output} [pyfxr]")
        manifest[name] = {"path": str(output), "backend": "pyfxr", "preset": preset}

    if args.manifest:
        manifest_path = args.output_dir / "manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
        print(f"Wrote {manifest_path}")

    if args.play:
        subprocess.run(["afplay", str(args.output_dir / f"{args.play}.wav")], check=True)


if __name__ == "__main__":
    main()
