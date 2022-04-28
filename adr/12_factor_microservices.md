# Microservice Boundaries

## Status

Accepted

## Context

Adapt the 12 Factor App to be used by our Microservice's

## Decision

### 1 – Codebase

One codebase, tracked in revision control; many deploys

Currently our approach is to utilize a monorepo in order to manage and maintain
code.  This code will reside within Git.  Our current implementation is built
on top of Github, this may change in the future.

### 2 – Dependencies

Explicitly declare and isolate dependencies

As suggested in the Twelve‑Factor App, regardless of what platform your
application is running on, use the dependency manager included with your
language or framework. How you install operating system or platform
dependencies depends on the platform:

  * In noncontainerized environments, use a configuration management tool
(Chef, Puppet, Ansible) to install system dependencies.
  * In a containerized environment, do this in the Dockerfile or equivalent.

**Note:** We recommend that you choose a dependency management mechanism
in the context of your comprehensive Infrastructure‑as‑Code strategy, not as
an isolated decision. See Martin Fowler’s writings on Infrastructure‑as‑Code
and download the O’Reilly report Infrastructure as Code by Kief Morris.

### 3 – Config

Store configuration in the environment

Anything that varies between deployments can be considered configuration.
The Twelve‑Factor App guidelines recommend storing all configuration in the
environment, rather than committing it to the repository. We recommend the
following specific practices:

 * Use non‑version-controlled .env files for local development. Docker supports
the loading of these files at runtime.
 * Keep all .env files in a secure storage system, such as Vault, to make the files
available to the development teams, but not commited to Git.
 * Use an environment variable for anything that can change at runtime, and for
any secrets that should not be committed to the shared repository.
 * Once you have deployed your application to a delivery platform, use the delivery
platform’s mechanism for managing environment variables.

### 4 – Backing Services

Treat backing services as attached resources

The Twelve‑Factor App guidelines define a backing service as “any service the
app consumes over the network as part of its normal operation”. The implication
for microservices is that anything external to a service is treated as an attached
resource, including other services. This ensures that every service is completely
portable and loosely coupled with the other resources in the system. Additionally,
the strict separation increases flexibility during development – developers only
need to run the services they are modifying, not others.

### 5 – Build, Release, Run

Strictly separate build and run stages

To support strict separation of build, release, and run stages, as recommended
by the Twelve‑Factor App, we recommend the use of a continuous integration/
continuous delivery (CI/CD) tool to automate builds. Docker images make it easy
to separate the build and run stages. Ideally, Docker images are created from
every commit and treated as deployment artifacts.

### 6 – Processes

Execute the app in one or more stateless processes

For microservices, the important point in the Processes factor is that your
application needs to be stateless. This makes it easy to scale a service horizontally
by simply adding more instances of that service. Store any stateful data, or data
that needs to be shared between instances, in a backing service such as Redis.

### 7 – Data Isolation

Each service manages its own data

As a modification to make the Port Binding factor more useful for microservices,
we recommend that you allow access to the persistent data owned by a service
only via the service’s API. This prevents implicit service contracts between
microservices and ensures that microservices can’t become tightly coupled.
Data isolation also allows the developer to choose, for each service, the type
of data store that best suits its needs.

### 8 – Concurrency

Scale out via the process model

The Unix process model is largely a predecessor to a true microservices
architecture, insofar as it allows specialization and resource sharing for different
tasks within a monolithic application. In a microservices architecture, you can
horizontally scale each service independently, to the extent supported by the
underlying infrastructure. With containerized services, you further get the
concurrency recommended in the Twelve‑Factor App, for free.

### 9 – Disposability

Maximize robustness with fast startup and graceful shutdown

Instances of a service need to be disposable so they can be started, stopped,
and redeployed quickly, and with no loss of data. Services deployed in Docker
containers satisfy this requirement automatically, as it’s an inherent feature of
containers that they can be stopped and started instantly. Storing state or session
data in queues or other backing services ensures that a request is handled
seamlessly in the event of a container crash. We are also proponents of using
a backing store to support crash‑only design.

### 10 – Dev/Prod Parity

Keep development, staging, and production as similar as possible

Keep all of your environments – development, staging, production, and so on –
as identical as possible, to reduce the risk that bugs show up only in some
environments. To support this principle, we recommend, again, the use of
containers – a very powerful tool here, as they enable you to run exactly the
same execution environment all the way from local development through
production. Keep in mind, however, that differences in the underlying data
can still cause differences at runtime.

### 11 – Logs

Treat logs as event streams

Instead of including code in a microservice for routing or storing logs, use one
of the many good log‑management solutions on the market, several of which
are listed in The Twelve‑Factor App. Further, deciding how you work with logs
needs to be part of a larger APM and/or PaaS strategy

### 12 – Admin Processes

Run admin and management tasks as one‑off processes

In a production environment, run administrative and maintenance tasks separately
from the app. Containers make this very easy, as you can spin up a container
just to run a task and then shut it down.

## Consequences

This minimizes the time and cost for new developers joining the project. Have a
clean contract with the underlying operating system, offering maximum portability
between execution environments.
