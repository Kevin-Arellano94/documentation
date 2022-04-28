# 1 Table Per Microservice

## Status

Proposed

## Context

Should a microservice only access a single table?

## Decision

Considering that we are using DynamoDB, and that DynamoDB pushes for single
table design, it makes sense to align the boundary constraints for a microservice
to include a single table design under the hood.

## Consequences

It is easier to test the service standalone.  Deploying a service also becomes
more predictable as you know the asset that is attached.
