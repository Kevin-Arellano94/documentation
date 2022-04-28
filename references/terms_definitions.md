# Terms and Definitions

## Absent

When a device does not send back any Sync Data or Heartbeats for a period of time (defaults to 24 hours) it is marked as absent.  This value is configurable by monitoring level and by agency.

When the device moves to an Absent status then a notification is sent to the Human Actor in charge of the Participant.

## Administrative Human Actor

An Administrative Human Actor is a human that interacts with the system who acts as a representative of an agency.  These are typically going to be Call Center employees, Officers, Agency Administrators.

## Answer

A reaction to a question.

## Attached Device Telemetry Data

Attached Device Telemetry Data is data that is available from a device that is attached to the monitored mobile device, one example of this is heartrate data.

## Challenge

An puzzle, game, or action that is requested to determine Impairment.

## Check-in

A Check-in is a series of 1-3 (currently, this value should be configurable in the future) Check-in Attempts that result in a cumulative success or failure.  All Check-in Attempts must fail to count the Check-in as a failure.  If any Check-in Attempt is a success then the overall Check-in is a success.

Check-in's contain image and location metrics.

## Check-in Attemp - Successful

A Successful Check-in Attempt is one that has been marked as the same person by Rekognition or manually by a human actor.

## Check-in Attempt

A Check-in Attempt is any time that a Check-in has been requested of a participant and has resulted in an outcome.  The current outcomes are; Successful and Failed AI, Failed Manual.

## Check-in Attempt - Failed AI

A Failed AI Check-in Attempt is one that has been sent to Rekognition for analysis and has been rejected due to confidence returned being below the configured required confidence value (currently 0.70).

## Check-in Attempt - Failed Manual

A Failed AI Check-in Attempt is one that has been reviewed by a administrative human actor and has been determined to be not the same person, not a person, or for some reason is not of the participant.

## Check-in Attempt - Successful AI

## Check-in Attempt - Successful Manual Override

## Completed Check-in

Any collection of Check-in Attempts that have either resulted in an overall fail status or success status.  This could be through a maximum retry all in failed status or in any attempt reesulting in a success.

## Compliant

## Court Reporting

## Device

## Device Sync

Any time the state changes on the device then the data will be sent back to the system for processing and retention.  Device Sync's can result in success or failure.  In the case of failure the Sync will be retried until it is successful.  In the case where there is a future Sync then it will pickup the existing failed data and include it thus negating the retry.

## Events View

The tab/view in the user interfaces that displays the composite view of event data into a singular view.  These "events" are made up from one to many raw events but are rolled up to make the view easier to understand.

## Exclusion Zone

An Exclusion Zone is a radial area (to be expanded later) that a Participant is prohibited to be present within.

## Failed Check-in

A Failed Check-in is any Check-in where all Check-in Attempts have resulted in a failure.

## Failed Sync

An attempt to send the data that currently resides on the device back to the system that results in a failure.  This could be due to network connectivity or other unknown circumstances.

## Human Actor

A Human Actor is a human that interacts with the system.

## Impairment

The state or fact of being impaired in a specified faculty.

## Inclusion Zone

An Inclusion Zone is a radial area (to be expanded later) that a Participant is allowed to be present within.

Inclusion Zones can be time boxed for curfew operations.

## Incomplete Check-in

Any Check-in that has been requested but has not been completed that is within a 15 minute grace period.  Once the 15 minute grace period has expired the Check-in is considered a missed Check-in.

**NOTE:** In the case where a Check-in occurs offline (the user could not get to the network to send the data) a Check-in may move to Missed until the device sync's.  At the point where the device is synced then the Check-in would move to the appropriate status after analysis from the AI and/or human.

## Interactions

## Missed Check-in

A Missed Check-in is one that the user never performed the Check-in action for.

**NOTE:** There are scenarios where a Check-in may move to missed and then move to another status later.  See Incomplete Check-in and Failed Sync for more details.

## Missing Answers

A Missing Answer occurs when a Question is sent to a Device and the Participant either ignores or dismisses the Question with an Answer.

## Monitored Device

A Device that is being Monitored.  The two currently known Monitored Devices are Mobile Phones and Monitoring Bracelets.

## Monitored Mobile Device

A Monitored Mobile Device is a Mobile Phone that is enrolled within the program, attached to a Participant, and should be reporting information.

## Parole

## Participant

A monitored Human Actor within the system.

## Pre-trail

## Probation

## Question

A sentence worded so as to elicit information, presented to the Participant for an answer.

## Raw Event Stream

The Raw Event Stream is a collection of Raw Events (events that are not rolled up and may or may not be complete) that are used to manage state transitions, create entities, manage entities, and other events within the system.

Some examples: Photo Taken, Check-in Requested

## Successful Check-in

A Successful Check-in is a Check-in where any of the Check-in Attempts resulted in a success.

## Telemetry Data

Telemetry Data is data that is available from the monitored mobile device, one example of this is accelerometer data.

Attached Device Telemetry Data is not the same as Telemetry Data.

## Zone Violation

A Zone Violation is where a Participant has either left an explicit Inclusion Zone or has entered an Exclusion Zone.
