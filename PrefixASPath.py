import mrtparse

class PrefixASPath:
    def __init__(self, filename):
        self.reader = mrtparse.Reader(filename)

    def __iter__(self):
            return self

    def __next__(self):
        for m in self.reader:
            mrt = m.data
            prefix = None
            prefixlen = None
            aspaths = None

            if mrt['subtype'][0] == mrtparse.TD_V2_ST['RIB_IPV4_UNICAST']:
                prefix = mrt['prefix']
                prefixlen = mrt['prefix_length']

                for entry in mrt['rib_entries']:
                    for attr in entry['path_attributes']:
                        if attr['type'][0] == mrtparse.BGP_ATTR_T['AS_PATH']:
                            for path_seg in attr['value']:
                                if path_seg['type'][0] == mrtparse.AS_PATH_SEG_T['AS_SEQUENCE']:
                                    aspaths = path_seg['value']
            if prefix is not None and prefixlen is not None and aspaths is not None:
                return prefix, prefixlen, aspaths
        raise StopIteration()
