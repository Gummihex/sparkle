# AI + Local Model Pipeline

## Flow
Natural language -> intent extraction -> normalized command plan -> capability validation -> permission validation -> execution queue -> adapters -> realtime state.

## Providers
`AiProvider` interface supports cloud and local providers. Local provider adapters may target Ollama, llama.cpp or another user-selected runtime. The core application remains functional without AI.

## Guardrails
AI cannot execute arbitrary PowerShell, shell, filesystem or network commands. Device actions are allow-listed by capability and require explicit application authorization. Sensitive credentials never enter prompts/logs.

## Voice
Speech-to-text is an input provider only. Transcribed text enters the same intent pipeline as typed commands. Optional text-to-speech can announce results.

## Scene generation
Example: “Mach Gaming aggressiver” -> inspect current gaming scene -> propose or apply validated changes such as higher saturation, contrast and effect speed on compatible devices. Unsupported devices are skipped and reported.

## Automation generation
AI can generate a draft automation, but the final rule is validated against triggers, conditions, actions and device capabilities before saving.

## Local privacy
Screen frames and audio features remain local by default. A local model can process them without cloud upload where supported.
