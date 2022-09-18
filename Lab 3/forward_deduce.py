import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
    ATOM   = r"[a-z][a-zA-Z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")
        
        
        
        
        
def forward_deduce(x):
    kb_list = list(clauses(x))
    result = []
    i = False
    while not i:
        check_head = 0
        for head, body in kb_list:
            if head in result:
                check_head += 1
            else:
                count = 0
                for atom in body:
                    if atom in result:
                        count += 1
                if count == len(body):
                    result.append(head)
                else:
                    check_head += 1
        if check_head == len(kb_list):
            i = True
    return result



kb = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

print(", ".join(sorted(forward_deduce(kb))))

kb = """
a :- b.
b.
"""

print(", ".join(sorted(forward_deduce(kb))))