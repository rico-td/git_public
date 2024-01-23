const hobbies = ["lesen", "essen", "schwimmen" ]


function listeHobbies(newItem) {
    if (hobbies.length > 5) {
        hobbies.shift();
    } else {
        hobbies.push(newItem) 
    }

    for (let i=0; i< hobbies.length; i++) {
        console.log("Hobbies: " + hobbies[i]);
    }
}

(listeHobbies("schlafen"));
