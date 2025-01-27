# Example prompt to create JSON from written config

This is an example of a cogeneration prompt that could be used in order to create a script for the purpose of programmatically creating JSON assistant configurations from natural language. 

The intended workflow here would be that the user prompts for the creation of the script. 

Then the user has a script which they can run in their assistant repository whenever they update their system configuration and wish to generate a fresh JSON for importing to whatever platform they are using.

## Example

Generate a Python script which does the following:

Visit this folder on my filesystem:

/home/daniel/Git/ai-assistant-template/system-prompts

Within that folder is an ordered list of Configuration text for large language model assistants. Each version of the configuration is ordered sequentially in the following format:

v1.md, v2.md, v3.md

The file ordering might be somewhat inconsistent. For example, I might label v4 as V4.md rather than v4.md (with a capital V). So the logic should be fuzzy enough to accommodate these minor differences in file naming structure.

The script should find the latest configuration. The latest configuration is the version with the highest number. For example if the folder contains v1.md, v2.md and v3.md, the latest configuration would be v3.md

Once you have identified the latest configuration text, you must convert it to a representation in JSON that preserves the configuration. 

The JSON should be exported to the following directory:

/home/daniel/Git/ai-assistant-template/finished-configs

Its name should match the source file. For example, if the source file was v3.md, then the converted configuration should be v3.json