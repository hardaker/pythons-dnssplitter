# Overview

Parses DNS domain names into three parts: the prefix, the registered
domain and it's registration point.

# Usage

## From the CLI

```
dnssplit www.google.co.uk www.yahoo.com
www.google.co.uk:
  Prefix:    www
  Domain:    google.co.uk
  Reg Point: co.uk
www.yahoo.com:
  Prefix:    www
  Domain:    yahoo.com
  Reg Point: com
```

## Using the API

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
