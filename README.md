# Overview

Parses DNS domain names into three parts: the prefix, the registered
domain and it's registration point.

# Usage

``` python
import dnssplitter
splitter = dnssplitter.DNSSplitter()

splitter.init_tree() # uses internal data
# or load your own:
# splitter.load_psl_file("/path/to/public_suffix_list.dat")
results = splitter.search_tree("www.foo.co.uk")

# Returns an array of [prefix, registered_domain, public_point]:
# results == ['www', 'foo.co.uk', 'co.uk']
```

# Reason for being

There are a number of PSL breakdown libraries.  But this one is faster
than the others based on some initial tests, and returns more information.
