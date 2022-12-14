from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)

def unique_koala_facts(number):
    unique_facts = []
    i = 0
    while len(unique_facts) < number:
        fact = random_koala_fact()
        if len(unique_facts) > number:
            return unique_facts
        elif i >= 1000:
            break
            print("You looped a thousand times")
        elif fact in unique_facts:
            i += 1
        elif fact not in unique_facts:
             unique_facts.append(fact)
          
        i += 1
    return unique_facts

def num_joey_facts():
    list_with_facts = []
    list_with_double_facts = []
    while len(list_with_facts) < 1000:
        fact = random_koala_fact()
        if "joey" in fact:
            if list_with_double_facts.count(fact) < 10:
                list_with_double_facts.append(fact)
                continue
            elif list_with_double_facts.count(fact) == 10:
                list_with_facts = list(dict.fromkeys(list_with_double_facts))
                return len(list_with_facts)

def koala_weight():
    i = 0
    found = False
    while found == False:
        fact = random_koala_fact()
        if "kg" in fact:
            kg_location = fact.find("kg")
            start_index = kg_location - 2
            # end_index = kg_location + 2
            return int(fact[start_index:kg_location])
        
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())
    print(unique_koala_facts(10))
    print(num_joey_facts())
    print(koala_weight())