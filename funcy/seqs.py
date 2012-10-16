from itertools import repeat, islice, ifilter, imap, chain
from whatever import _, that

# NOTE: Should I import here anything from itertools or elsewhere,
#       if it exactly implements some function I want?
# PROS: Convenient
# CONS: Possibly confusing

# pythons itertools.repeat() is basically the same as in clojure

def repeatedly(f, n=None):
    _repeat = repeat(None, n) if n else repeat(None)
    return (f() for _ in _repeat)

def iterate(f, x):
    while True:
        yield x
        x = f(x)

def take(n, coll):
    return list(islice(coll, n))

# TODO: tree-seq equivalent

def distinct(seq):
    "Order preserving distinct"
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]

def remove(pred, coll):
    return filter(complement(pred), coll)

def iremove(pred, coll):
    return ifilter(complement(pred), coll)

def concat(*colls):
    return list(chain(*colls))
iconcat = chain                # clojure's concat
iiconcat = chain.from_iterable # clojure's lazy-cat

def mapcat(f, *colls):
    return concat(*map(f, *colls))

def imapcat(f, *colls):
    return chain.from_iterable(map(f, *colls))

# interleave = izip

def interpose(sep, coll):
    pass


def drop(n, seq):
    return islice(seq, n, None)


def keep(f, seq):
    return remove(_ is None, map(f, seq))

def ikeep(f, seq):
    return iremove(_ is None, imap(f, seq))

def keep_indexed(f, seq):
    raise NotImplementedError

def ikeep_indexed(f, seq):
    raise NotImplementedError


from itertools import count


def test_repeatedly():
    c = count().next
    assert take(2, repeatedly(c)) == [0, 1]