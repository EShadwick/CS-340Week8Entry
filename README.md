# CS-340Week8Entry
# Grazioso Salvare Animal Rescue Dashboard

This repository contains my Project Two artifacts for CS 340: a Python CRUD module and an interactive web dashboard built for Grazioso Salvare. The dashboard connects to a MongoDB database of animal shelter records and lets the user filter for dogs that are good candidates for specific rescue-training programs (water rescue, mountain and wilderness rescue, and disaster or individual tracking), view results in a sortable data table, and see the geographic location of any selected animal on a map.

**Tech stack:** Python, MongoDB (PyMongo), JupyterDash, Dash DataTable, Plotly, and Dash Leaflet for the geolocation chart.

---

## Reflection

### How do you write programs that are maintainable, readable, and adaptable?

The core of this project was the CRUD Python module I built in Project One, `CRUD_Python_Module.py`, which defines an `AnimalShelter` class that wraps the four basic database operations (create, read, update, and delete) against the MongoDB `aac` database. By putting all of the database logic inside that one class, the dashboard code in Project Two never had to talk to MongoDB directly. It just called methods like `read()` and got back a result, which kept a clean line between the data layer and the presentation layer.

The advantage of working this way is that each layer can change without breaking the other. When I needed to adjust a dashboard filter or add a callback, I was editing presentation code and never touched the database connection logic. When I built the read queries, I indexed the returned data by column name rather than by a fixed position, so the code does not silently break if the field order in a document changes. Writing the credentials and connection details into the class constructor in one place, rather than scattering them through the notebook, also made the module easier to read and safer to reuse.

In the future I could reuse this same CRUD module for any application that needs to work with the shelter database. It is not tied to the dashboard at all. The same `AnimalShelter` class could back a command-line reporting tool, a scheduled data-cleanup script, a REST API, or a completely different front end, because the create, read, update, and delete methods are generic. That portability is the real payoff of separating the module from the interface.

### How do you approach a problem as a computer scientist?

I approached the Grazioso Salvare work by starting from the client's actual requirements and translating them into data operations before writing any interface code. The client needed to identify trained rescue dogs by breed, sex, and age range for each rescue category, so I first made sure the database queries returned exactly the right records for each of those categories, then built the dashboard widgets on top of queries I already trusted. Getting the data layer correct first meant the dashboard was assembling results I had already verified, rather than debugging the database and the interface at the same time.

This differed from earlier coursework where assignments were often self-contained and the requirements were fixed for me. Here the requirements came from a client scenario, which meant I had to think about who would use the tool and what decisions they needed to make, not just whether the code ran. The map view and the interactive table existed because a Grazioso Salvare staff member needs to act on the results, not just see them.

For future client database work I would keep the same strategy: separate the data access layer from the interface from the start, verify queries independently before wiring them to the UI, and index results by field name rather than position so the code stays robust as the data evolves. I would also keep iterating in small, testable steps so that when something breaks I can find the cause quickly instead of unwinding a large change.

### What do computer scientists do, and why does it matter?

Computer scientists take a real-world problem and build systems that turn raw data into something people can use to make better decisions. For Grazioso Salvare, the raw material is thousands of animal shelter records. On its own that data is hard to act on. The dashboard turns it into a tool a staff member can use to quickly find dogs that fit a specific rescue-training profile and see where they are located, which directly supports the organization's mission of identifying and training rescue animals.

This kind of work matters because it saves people time and reduces error. Instead of manually sorting through records, a Grazioso Salvare employee can filter for the exact category they need and get an accurate, up-to-date result in seconds. Building the system on a clean, reusable data layer also means the organization can extend it later without starting over, so the value of the work keeps compounding as their needs grow.

---

## AI Acknowledgment

Generative AI (Anthropic's Claude) was used to help organize and refine the written reflection in this README. All project code, database work, and the underlying decisions described here are my own.

**Reference**
Anthropic. (2026). *Claude* [Large language model]. https://claude.ai
