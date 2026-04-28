# Axium Preset Reference

Axium is a PyWeek space shooter that uses `pyfxr.SFX(...)` presets in `sfx.py`. The bundled generator includes these mapped names:

| Preset | Role | Starting Point |
|---|---|---|
| `axium_laser` | player shot | square wave, downward frequency ramp, phaser |
| `axium_enemy_laser` | enemy shot | square wave, slower decay, high duty |
| `axium_explosion` | large explosion | noise, long attack/sustain/decay, low-pass ramp |
| `axium_explosion_small` | small pop/explosion | noise, punch, phaser, arpeggio |
| `axium_powerup` | upgrade/charge | square wave, upward frequency ramp, vibrato |
| `axium_rocket` | rocket launch | noise, attack ramp, pitch movement |
| `axium_phaser` | phaser weapon | sine wave, downward ramp, high-pass |
| `axium_pause` | pause/menu cue | square wave, punch, negative arpeggio |
| `axium_impact` | hit impact | noise, hard downward ramp, high-pass |
| `axium_placement` | build/place cue | saw wave, very short envelope |
| `axium_pickup` | pickup/coin cue | square wave, punch, arpeggio |

Use:

```bash
python scripts/generate_sfxr_pack.py --group axium --output-dir generated_sfxr/axium --manifest
```

The exact parameter dictionaries live in `scripts/generate_sfxr_pack.py` under `AXIUM_PRESETS`.
