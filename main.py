# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():                                         # Inputs
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = []                                           # Saglaba eksistejosos kontaktus
    for cur_query in queries:  
        if cur_query.type == 'add':                         # Pievieno kontaktus
            for contact in contacts:
                if contact.number == cur_query.number:      # Ja kontakts jau eksiste ar so numuru, tad to parraksta
                    contact.name = cur_query.name
                    break
                else:                                       # Ja nav, tad izveido jaunu kontaktu lista
                    contacts.append(cur_query)
        elif cur_query.type == 'del':                       # Dzezs kontaktu
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

