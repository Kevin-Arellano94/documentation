# Don't Avoid Failure, Embrace It

## Status

Accepted

## Context

Systems fail, plan for it instead of being surprised by it.

## Decision

A key tenet of modern application design is that failure will occur. The layer cake
that modern applications rely on – from cloud‑hosted virtual machines to
containers to application libraries to dynamic networking – means that the moving
parts in any application are legion. You need to assume that one or more parts
of your application will fail in some manner at some point. Expecting failure, and
building in mechanisms to mitigate its effects, goes a long way toward making
your application more resilient.

## Consequences

Not embracing failure means that we don't plan for things to break and inherently
design fragile systems.
