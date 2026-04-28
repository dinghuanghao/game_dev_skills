# SFXR Design Guide

## Common Recipes

| Sound | Wave | Key Parameters |
|---|---|---|
| Coin / pickup | `SQUARE` | high `base_freq`, short `env_sustain`, medium `env_decay`, `env_punch`, positive `arp_mod` |
| Jump | `SQUARE` or `SINE` | low `base_freq`, positive `freq_ramp`, short envelope |
| Laser | `SQUARE` or `SAW` | medium/high `base_freq`, negative `freq_ramp`, short sustain, duty sweep |
| Explosion | `NOISE` | low `base_freq`, long sustain/decay, `env_punch`, low `lpf_freq` |
| Impact | `NOISE` | medium `base_freq`, strong negative `freq_ramp`, short decay, some `hpf_freq` |
| Metal | `SQUARE`/`SAW` | high-pass, phaser, short transient plus separate ring layer if needed |
| Ice/glass | `SQUARE`/`SINE` | high `base_freq`, fast downward ramp, high-pass, short envelope |
| Water | `NOISE` + low tone | low-pass noise, mild high-pass, soft attack |

## Tuning Order

1. Pick `wave_type`.
2. Set envelope first: `env_attack`, `env_sustain`, `env_decay`, `env_punch`.
3. Shape pitch: `base_freq`, `freq_limit`, `freq_ramp`, `freq_dramp`.
4. Add tone color: `duty`, `duty_ramp`, `lpf_freq`, `hpf_freq`.
5. Add motion only if needed: `vib_strength`, `vib_speed`, `pha_offset`, `pha_ramp`, `arp_speed`, `arp_mod`.

## When SFXR Is Not Enough

Use layered offline synthesis when a sound needs separate physical components:

- fireball = low sine boom + filtered noise + crackle
- water burst = low pop + splash noise + high droplets
- metal clash = transient noise + two ringing tones
- flying kiss = lip pop + pitch sweep + sparkle notes

The project-local script `scripts/audio/generate_web_audio_style_pack.py` in `meowart-server` is a good example of this layer-based approach.
