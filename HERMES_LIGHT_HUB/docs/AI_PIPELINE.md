# AI pipeline

```text
Voice / text
   -> intent extraction
   -> device + room resolution
   -> capability validation
   -> deterministic action plan
   -> user confirmation when risk/ambiguity is high
   -> Light Engine
   -> state verification
   -> event + telemetry
```

Examples:
- “Mach das Wohnzimmer gemütlich” -> choose a scene template, resolve room, validate CCT/brightness support, execute transitions.
- “Alle Nanoleaf auf Regenbogen” -> resolve manufacturer group, filter devices with effects/RGB capability, execute only supported devices.
- “Wenn ich mein Gaming-Spiel starte, aktiviere Gaming” -> automation proposal with trigger, conditions, scene action and rollback.

The AI never directly talks to vendor APIs. It produces typed intents/actions consumed by the deterministic engine.

## Local model
A provider interface allows a local model to handle intent parsing and scene generation. No local model is required for basic lighting control; deterministic controls remain functional without AI.
