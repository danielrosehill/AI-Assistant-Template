# AI Assistant Template (Demo Project = Beer Advisor!)

![alt text](icon/beer-agent.jpg)

27-Jan-25

## Purpose Statement

The purpose of this repository is to provide a basic repository model for creating AI assistants.

This folder structure provides a simple model for versioning configuration texts (system prompts) Designed to achieve consistent performance for AI assistants in various deployments.

## Demo Use Case

The demonstration project is a simple configuration for an assistant to provide beer recommendations from a menu.

It is a simple use case that only requires a very small amount of contextual data.  

## Organisation

The `system prompts` folder contains a version history for the different system prompts, which are the core part of assistant configuration. 

The `context data` folder contains context data intended to be added as knowledge for the assistant. In a more elaborate setup, this folder could be configured as a data pipeline directly feeding its contextual data into a vector database. 

The `icon` folder contains an icon for the agent. 

Finally, the repository also contains an agent builder script. This contains a prompt which can be used for code generation in order to create Python scripts to programmatically create `JSON` configurations from natural language markdown files. 

Together, this folder structure comprises a basic structured "workbench" that can be used to draft and provision effective AI assistants. Doing so in something like a Github repository is also a valuable way, in my opinion, of decoupling your configurations, which are valuable intellectual property, from any one platform you're deploying your assistants on.

## Author

Daniel Rosehill  
(public at danielrosehill dot com)

## Licensing

This repository is licensed under CC-BY-4.0 (Attribution 4.0 International) 
[License](https://creativecommons.org/licenses/by/4.0/)

### Summary of the License
The Creative Commons Attribution 4.0 International (CC BY 4.0) license allows others to:
- **Share**: Copy and redistribute the material in any medium or format.
- **Adapt**: Remix, transform, and build upon the material for any purpose, even commercially.

The licensor cannot revoke these freedoms as long as you follow the license terms.

#### License Terms
- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **No additional restrictions**: You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

For the full legal code, please visit the [Creative Commons website](https://creativecommons.org/licenses/by/4.0/legalcode).