# Security Model

1. Local-first: bind backend to loopback by default.
2. Never expose the control API directly to the public Internet.
3. Store API keys/tokens in OS secure storage; never in source or logs.
4. Pairing requires explicit user confirmation.
5. AI uses a policy gateway; model output is data, not authority.
6. Commands are validated against capability, range and target before execution.
7. Audit every automation/AI command with timestamp, actor and result.
8. Network discovery must not imply authorization to control a device.
9. Manufacturer cloud APIs are opt-in and clearly marked.
