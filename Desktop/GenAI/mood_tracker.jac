// Define node types
node person {
    has name;
    has age;
}

node greeting {
    has message;
}

// Define edge relationships
edge friend;
edge says;

// Define a graph (walker) to create and connect nodes
walker init {
    // Create person nodes
    person1 = spawn here ++> node::person(name="Alice", age=25);
    person2 = spawn here ++> node::person(name="Bob", age=30);
    
    // Create a greeting
    greet = spawn here ++> node::greeting(message="Hello!");
    
    // Connect people as friends
    person1 +[friend]+> person2;
    
    // Connect greeting to person
    greet +[says]+> person1;
}
    
    // Traverse and display information
    std.out("Created graph with:");
    with entry {
        take --> node::person;
    }
    
    with exit {
        std.out("Person:", here.name, "Age:", here.age);
    }


// Another walker to demonstrate traversal
walker find_friends {
    has target_name;
    
    with entry {
        take --> node::person;
    }
    
    here: {
        if (here.name == target_name) {
            std.out("Found", target_name);
            take -[friend]-> node::person;
        }
        else {
            take --> node::person;
        }
    }
    
    with exit {
        std.out(target_name, "is friends with:", here.name);
    }
}