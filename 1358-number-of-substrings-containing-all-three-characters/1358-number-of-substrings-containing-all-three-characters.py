import numpy

ids = bytearray(256)
ids[98:100] = 1, 2

def numberOfSubstrings(
    s: str, ids=bytes(ids),
    indices=numpy.arange(1, 50_001, dtype=numpy.uint16)
) -> int:
    s = numpy.frombuffer(s.encode().translate(ids), dtype=numpy.uint8)
    places = numpy.zeros((3, s.size + 1), dtype=numpy.uint16)
    indices = indices[:s.size]
    places[s, indices] = indices
    return numpy.maximum.accumulate(places, axis=1, out=places)\
        .min(axis=0)\
        .sum()\
        .item()    
    
Solution = repeat(namedtuple('Solution', ('numberOfSubstrings',))(
    numberOfSubstrings
)).__next__
        