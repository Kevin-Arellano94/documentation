# Features

## Overview

![Feature Dependencies](/diagrams/Architecture%20Overview-Feature%20Dependencies.png)

A core component of being able to refactor the existing infrastructure to gain control and ensure auditability is the New Account Structure.  This structure will be implemented in 45-60 days by Opti9 (a 3rd party partner of AWS).  This structure allows us to ensure separation of concerns within the stack while also providing us with a safety net and auditing framework that we can use in the future.

In order to implement CICD we need a place to deploy code and assets to.  We could utilize the existing accounts or create another new account, but the accounts would not be secured nor monitored and we would be creating technical debt in the form of another area to have to secure once the New Account Structure is in place.  For this reason production CICD will be developed but will not be implemented until the new structure is in place.

Having CICD in place will allow us to deploy the functions that we need to capture the event details from the existing (and future state) accounts.  The CICD ensures that human hands can not touch production assets.  This is important as it will minimize the chance of a manual effort causing an unexpected outage.

Business Intelligence will provide business with a system that it can utilize to measure and determine efficacy of the platform.

Monitoring is the ability to take information from an audit trail or event system and utilize that information to produce alerts.  These alerts can be used to wake people up when things break or notify interested parties of notable or significant changes.  Really Monitoring will be developed along side of the Security Account and the New Account Structure but it will evolve as assets are deployed into the new accounts over time.
