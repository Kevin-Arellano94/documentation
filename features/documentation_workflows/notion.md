# Notion

![Notion to Git workflow](/diagrams/Documentation_Workflows-Notion.png)

When a change is committed to a Documentation Repository then a Github
action will be kicked off that will push any change in documentation to
Notion.

When a change is committed to Notion (via automation or manually) then
Notion will notify Github via a callback URI that will initiate a
Github action that will backup all of Notion to a single repository.
