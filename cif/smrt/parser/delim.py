from cif.smrt.parser.pattern import Pattern
import re
from pprint import pprint


class Delim(Pattern):

    def __init__(self, *args, **kwargs):
        super(Delim, self).__init__(*args, **kwargs)

    def process(self, rule, feed, data, limit=10000000):
        cols = rule.defaults['values']

        max = 0
        rv = []
        for l in data:
            if self.is_comment(l):
                continue

            m = self.pattern.split(l)
            if len(cols):
                obs = rule.defaults
                for c in range(0, len(cols)):
                    if cols[c] is not None:
                        obs[cols[c]] = m[c]
                obs.pop("values", None)
                rv.append(obs)

            max += 1
            if max >= limit:
                break
        return rv


class Csv(Delim):

    def __init__(self, *args, **kwargs):
        super(Csv, self).__init__(*args, **kwargs)

        self.pattern = re.compile(',')


class Pipe(Delim):

    def __init__(self, *args, **kwargs):
        super(Pipe, self).__init__(*args, **kwargs)

        self.pattern = re.compile('\||\s+\|\s+')