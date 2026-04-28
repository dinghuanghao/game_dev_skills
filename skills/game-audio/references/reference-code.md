# Reference Code Index

Use these files as code references for how to generate sound effects. Do not store or rely on pre-rendered WAVs in this skill.

## Bundled pyfxr Generator

- `scripts/generate_sfxr_pack.py` - production entry point for this skill. It contains Axium-derived `pyfxr.SFX(...)` dictionaries and general-purpose game SFX presets.

## Reusable pyfxr Examples

- `references/pyfxr-examples.py` - compact examples showing how to create individual WAV files and how to add new presets.

## Project-Local Layered Examples

If this skill is being used inside the `meowart-server` workspace, these earlier experimental scripts show layered offline synthesis patterns. They are not part of this skill and should not be copied wholesale unless the user asks for a non-pyfxr approach.

- `/Users/less/develop/meowart-server/scripts/audio/generate_web_audio_style_pack.py` - data-driven `tone/noise/notes` layer presets.
- `/Users/less/develop/meowart-server/scripts/audio/generate_fireball_explosion_sfxr.py`
- `/Users/less/develop/meowart-server/scripts/audio/generate_ice_shatter_sfxr.py`
- `/Users/less/develop/meowart-server/scripts/audio/generate_water_ball_burst_sfxr.py`
- `/Users/less/develop/meowart-server/scripts/audio/generate_metal_clash_sfxr.py`
- `/Users/less/develop/meowart-server/scripts/audio/generate_flying_kiss_sfxr.py`
