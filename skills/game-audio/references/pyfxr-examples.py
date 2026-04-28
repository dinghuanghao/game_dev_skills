"""Reference pyfxr code snippets for procedural game SFX.

This file is intentionally importable/copyable reference code. The skill's
main generator is ../scripts/generate_sfxr_pack.py.
"""

from __future__ import annotations

from pathlib import Path

import pyfxr


def save_sfx(name: str, params: dict, output_dir: str | Path = "generated_sfxr") -> Path:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{name}.wav"
    pyfxr.SFX(**params).build().save(str(path))
    return path


def coin_pickup(output_dir: str | Path = "generated_sfxr") -> Path:
    return save_sfx(
        "coin_pickup",
        {
            "wave_type": pyfxr.WaveType.SQUARE,
            "base_freq": 0.83,
            "env_attack": 0.0,
            "env_sustain": 0.039,
            "env_decay": 0.272,
            "env_punch": 0.468,
            "arp_mod": 0.253,
        },
        output_dir,
    )


def laser(output_dir: str | Path = "generated_sfxr") -> Path:
    return save_sfx(
        "laser",
        {
            "wave_type": pyfxr.WaveType.SQUARE,
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
        },
        output_dir,
    )


def explosion(output_dir: str | Path = "generated_sfxr") -> Path:
    return save_sfx(
        "explosion",
        {
            "wave_type": pyfxr.WaveType.NOISE,
            "base_freq": 0.06,
            "freq_ramp": -0.011,
            "env_attack": 0.16,
            "env_sustain": 0.31,
            "env_decay": 0.67,
            "env_punch": 0.19,
            "lpf_resonance": 0.0,
            "lpf_freq": 0.31,
            "lpf_ramp": -0.15,
        },
        output_dir,
    )


def powerup(output_dir: str | Path = "generated_sfxr") -> Path:
    return save_sfx(
        "powerup",
        {
            "wave_type": pyfxr.WaveType.SQUARE,
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
        },
        output_dir,
    )


def render_reference_set(output_dir: str | Path = "generated_sfxr") -> list[Path]:
    return [
        coin_pickup(output_dir),
        laser(output_dir),
        explosion(output_dir),
        powerup(output_dir),
    ]


if __name__ == "__main__":
    for written in render_reference_set():
        print(written)
