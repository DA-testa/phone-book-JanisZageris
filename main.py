# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]
            
def read_queries():                                                 # Nosaka cik daudz darbibas tiks veiktas
    n = int(input())
    return [Query(input().split()) for _ in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = {}                                                   # Saglaba sarakstu kur glaba kontaktus izmantojot numurus
    for cur_query in queries:
        if cur_query.type == 'add':                                 # Pevieno kontaktu sarakstam
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':                               # Izdzes kontaktu no saraksta ja eksiste
            if cur_query.number in contacts:
                del contacts[cur_query.number]
        elif cur_query.type == 'find':                              # Atrod kontaktu no saraksta
            response = contacts.get(cur_query.number, 'not found')
            result.append(response)
        else:                                                       # Ja komanda neatbilst nevienam no dotajiem
            print("invalid command")
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
