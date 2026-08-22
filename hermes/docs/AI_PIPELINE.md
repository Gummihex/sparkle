# AI Pipeline

`voice/text -> intent extraction -> target resolution -> capability validation -> deterministic command plan -> preview/confirmation -> execution -> audit`

## Scene generation
The model may propose scenes such as Movie, Gaming, Focus, Relax or Party. It must output structured JSON rather than raw device commands.

## Voice control
Speech-to-text is separated from intent planning. The voice layer can be replaced independently. Push-to-talk is the default; continuous listening is opt-in.

## Automations
Automations are deterministic rules with trigger, conditions, actions and cooldown. AI can draft an automation, but the automation engine executes only validated rules.

## Local model
LocalModel is an optional provider. Recommended interface: OpenAI-compatible HTTP endpoint on localhost, with configurable model name and context limits. No cloud dependency is required for normal lighting control.
