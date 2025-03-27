## Web Architecture

- Front-end (HTML, CSS, JS)
- Back-end (Pyton)
- Database

JS doesn't understand python & python doesn't understand JS
Universal language between two: JSON
Why?
Because it's a string -> all languages have strings in it, so it will understand JSON

When we get to front-end (with JavaScript), JSON will be converted into Object (equivalent to dictionary)
When we get to back-end (with Flask or Python), JSON will be converted into dictionary.
When we get to back-end with JAVA, JSON will be converted into HashMap.

Send request in JSON (from JS to Flask)
Flask will send request to Database
Database will send data back to Flask
Flask will send data back to front-end

JSON -> Medium Data Transfer

- used for transferring data
- why? Because it's in string from

XML was the old universal language

Advantages of JSON:

1. Universal Language
2. Same BE -> Multiple FE: `One Back-end can talk to multiple Front-End`
3. Mixing Back-ends (Flask + GO) - Micro services
   - it doesn't matter which language BE is using, FE only needs JSON.
4. Loose Coupling
   - FE and BE can be independently changed
   - Can change FE languages (without affecting BE)
   - Can upgrade FE/BE without it affecting each other
   - Both ends just expect JSON

Micro services architecutre

- mix Backend languages to improve performance
- BE can have the same database or different databases
- Why would someone mix BEs?
  - Some BEs may have advantages over the other, so you can combine them.
  - GO is more performant than Flask.
  - Flask is more DX friendly (can quickly develop with Flask).

There should be no leakages in the data.
