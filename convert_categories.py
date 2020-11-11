'''
Created on 23 Jan 2020

@author: Alex
'''
from useful_inkleby.files import QuickGrid


root = r""


def combine():
    all = QuickGrid(header=["category", "a", "b", "c"])

    lookup = {}

    qg = QuickGrid().open([root, "SHEF_A.csv"])
    lookup['a'] = {x[0].strip(): x[1].strip() for x in qg.data}
    natural_catagories = list(set([x[0].strip() for x in qg]))

    qg = QuickGrid().open([root, "SHEF_B.csv"])
    lookup['b'] = {x[0].strip(): x[1].strip() for x in qg.data}

    qg = QuickGrid().open([root, "SHEF_C.csv"])
    lookup['c'] = {x[0].strip(): x[1].strip() for x in qg.data}

    for n in natural_catagories:
        row = [n]
        for t in 'abc':
            row.append(lookup[t].get(n, ""))
        all.add(row)

    all.save([root, "full_table.csv"], force_unicode=True)


def find_clean_mapping():

    qg = QuickGrid().open([root, "full_table.csv"], force_unicode=True)
    for t in 'bc':
        map = QuickGrid(header=["a", t])
        for g, q in qg.split_on_unique('a'):
            a_items = list(set([x[t] for x in q if x[t]]))
            if len(a_items) == 1:
                pass
                map.add([g, a_items[0]])
        map.save([root, "clean_a_to_{0}.csv".format(t)], force_unicode=True)


def fill_in_combined():

    combined = QuickGrid().open([root, "full_table.csv"], force_unicode=True)

    for t in 'bc':
        count = 0
        total = 0
        map = QuickGrid().open([root, "clean_a_to_{0}.csv".format(t)])
        lookup = {x[0]: x[1] for x in map.data}
        for r in combined:
            if r[t] == "":
                total += 1
                r[t] = lookup.get(r["a"])
                if r[t]:
                    count += 1
        print("for {0}, {1}/{2} filled in".format(t, count, total))

    combined.save(force_unicode=True)


def generate_code_lookups():

    for a in 'ABC':
        done = []
        lookup = QuickGrid(header=["name", "code"])
        qg = QuickGrid().open([root, "SHEF_{0}.csv".format(a)])
        for r in qg:
            if r[2] not in done:
                lookup.add([r[1], r[2]])
                done.append(r[2])
        lookup.data.sort(key=lambda x: int(x[1][1:]))
        lookup.save([root, "CODES_SHEF_{0}.csv".format(a)], force_unicode=True)


def create_lookups_from_combined():
    combined = QuickGrid().open([root, "full_table.csv"])
    
    for t in 'ABC':
        code = QuickGrid().open([root, "CODES_SHEF_{0}.csv".format(t)])
        code = {x[0].strip(): x[1] for x in code}
        lookup = QuickGrid(header=["category", "SHEF_{0}".format(t), "SHEF_{0}_CODE".format(t)])
        for r in combined:
            category = r[t].strip()
            if category:
                cat_code = code[category]
                lookup.add([r[0], category, cat_code])
        lookup.save([root, "SHEF_{0}.csv".format(t)], force_unicode=True)

if __name__ == "__main__":
    combine()
    generate_code_lookups()
    find_clean_mapping()
    fill_in_combined()
    create_lookups_from_combined()
