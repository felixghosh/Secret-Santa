import random

class Person:
    def __init__(self, name, candidates, forbidden) -> None:
        self.name = name
        self.forbidden = forbidden
        self.candidates = [person for person in candidates if not person in forbidden]
        self.candidates.remove(self.name)
    
    def __str__(self) -> str:
        return f"{self.name}: ({self.candidates})"

candidates = ["Felix", "Ida", "Olivia", "Malin", "Torbjörn", "Daniel", "Jojo", "Drew"]

Felix = Person("Felix", candidates, ["Ida"])
Ida = Person("Ida", candidates, ["Felix"])
Olivia = Person("Olivia", candidates, [])
Malin = Person("Malin", candidates, ["Torbjörn"])
Torbjörn = Person("Torbjörn", candidates, ["Malin"])
Daniel = Person("Daniel", candidates, [])
Jojo = Person("Jojo", candidates, ["Drew"])
Drew = Person("Drew", candidates, ["Jojo"])
people = [Felix, Ida, Olivia, Malin, Torbjörn, Daniel, Jojo, Drew]


print("Generating matches!\n")

done = False
while not done:
    matches = {}
    for person in people:
        match_found = False
        while not match_found:
            #Find out if candidates still contains a person who is elligable
            elligable_match = False
            for candidate in person.candidates:
                if candidate not in matches.values():
                    elligable_match = True
                    break
            if not elligable_match:
                break

            #Find a random match for person
            potential_match = person.candidates[random.randint(0, len(person.candidates)-1)]
            if potential_match not in matches.values():
                match_found = True
                matches[person] = potential_match
        if not match_found:
            break
    
    #Check that everyone received a leagal match
    illegal_match = False
    for person in matches:
        if matches[person] in person.forbidden:
            illegal_match = True
            break
    if not illegal_match and len(matches) == len(people):
        done = True

print("Done! The results are:")
for person in matches:
    print(f"\033[92m{person.name}\033[00m gives to \033[91m{matches[person]}\033[00m")
