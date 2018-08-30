# README #

### What is this repository for? ###

This application focuses on cloning an entity and all its related entity.

### How do I get set up? ###

This project uses python3. You need to have 
python3.6 virtual environment installed on your machine.
To install python3.6 virtual environment follow this link:
 
https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3 

After installing the virtual environment, go to the project folder and type: 

    source <virtual_env_directory> activate
    
Run the application by typing:
    
    python src/main.py <input_file_path> <entity_id_to_be_cloned>


#### How to run tests
Test cases are located in tests folder.
In order to run the test cases simply type:

    python tests/runner.py

### Project Structure and Logic

The whole code lies in the src folder. Two files handle all the code
1. main.py - Handles the starting logic of gathering the input file path and entity id that needs to be cloned. Then calling the necessary functions.

2. graph.py - Handles all the graph related logic like creating graph, adding vertices, adding edge between two vertices,etc. 

### Who do I talk to? ###

* Tarun Chaudhary (http://curioustechie.in)