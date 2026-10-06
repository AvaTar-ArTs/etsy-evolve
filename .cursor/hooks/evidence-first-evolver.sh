#!/bin/sh
# Evidence-first creation gate.
# This does not create files or publish anything. It reminds the host agent to
# locate and comprehend existing capability before proposing new machinery.
set -eu

input=$(cat)
prompt=$(printf '%s' "$input" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("prompt", ""))' 2>/dev/null || true)

case "$prompt" in
  *create*|*build*|*implement*|*evolve*|*hook*|*agent*|*workflow*|*listing*|*product*)
    printf '%s\n' '{"permission":"allow","agent_message":"Evidence-first gate: before creating or evolving anything, inspect existing hooks, agents, skills, docs, and prior outputs; identify the assumption being made; choose reuse, adapt, or create; then verify the result and record the next unresolved gap."}'
    ;;
  *)
    printf '%s\n' '{"permission":"allow"}'
    ;;
esac
