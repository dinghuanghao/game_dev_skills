---
name: game-audio
description: Generate, tune, compare, and package procedural game sound effects with pyfxr/SFXR-style presets. Use when Codex needs code-generated WAV game audio, pyfxr or SFXR parameter presets, Axium-inspired effects, arcade SFX packs, reference code for sound-effect generation, or guidance for creating procedural audio scripts for other agents.
---

# PySFXR Game Audio

Use this skill to produce short procedural game SFX as WAV files from compact SFXR-style presets. Prefer the bundled generator for repeatable output; use the references only when you need design guidance or code examples for how the sounds are made.

## Quick Start

Generate all bundled presets:

```bash
python scripts/generate_sfxr_pack.py --group all --output-dir generated_sfxr --manifest
```

Generate only Axium-inspired presets:

```bash
python scripts/generate_sfxr_pack.py --group axium --output-dir generated_sfxr/axium --manifest
```

Generate one preset and audition it on macOS:

```bash
python scripts/generate_sfxr_pack.py --group all --preset axium_laser --output-dir /tmp/sfxr-test --play axium_laser
```

The script requires real `pyfxr`. If `pyfxr` cannot import, stop and help the user install a supported Python/pyfxr environment. If that is not practical, briefly suggest using another runtime approach such as `sfxrlua` or Web Audio API, but do not implement those approaches inside this skill.

## Workflow

1. Choose an existing preset first: run `scripts/generate_sfxr_pack.py --list --group all`.
2. Render a small comparison set before tuning.
3. If the user wants Axium-like arcade sounds, start with `--group axium`.
4. If the user wants general game sounds, start with `--group design`.
5. Save generated WAVs in the target project’s asset/audio folder or a clearly named output folder.
6. If making new presets, add them to `scripts/generate_sfxr_pack.py` as data dictionaries, not as separate one-off scripts.

## Resources

- `scripts/generate_sfxr_pack.py` - deterministic pyfxr pack generator with Axium and general game presets.
- `references/axium-presets.md` - source mapping for Axium-inspired pyfxr parameters.
- `references/design-guide.md` - compact SFXR tuning guidance and when to use Web Audio style layering.
- `references/reference-code.md` - index of code references for generating comparable sounds.
- `references/pyfxr-examples.py` - copyable pyfxr examples for common game effects.

## Preset Rules

- Keep presets short: most one-shot SFX should be `0.05s` to `1.2s`.
- Store intent in the preset name: `coin_chime`, `metal_clash`, `axium_rocket`.
- Tune with `wave_type`, `base_freq`, `freq_ramp`, `env_*`, `lpf_freq`, `hpf_freq`, `arp_*`, and `pha_*` before adding custom DSP.
- Use true `pyfxr` for all new generated output. Do not silently substitute another synthesis engine.
- Keep references as code and parameters. Do not add pre-rendered WAV assets to this skill.
