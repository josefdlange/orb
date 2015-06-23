##Orb is a Python library for CircleCI.

Right now, Orb is in its infancy. But the basics of using Orb are like so:

```
import orb

o = orb.connect(token='YOUR_CIRCLECI_TOKEN')  # You can also put your token in ~/.orb

o.user()            # Outputs JSON from the CircleCI REST API.
o.list_projects()   # Lists all projects your user has access to.
                    # There are more methods, see CircleCI's REST API docs and the source of this module.
```

More to come, including mapping JSON to Python objects (probably via lazily wrapping in a DictObject) and additional parameters, endpoints, and documentation. This base should hopefully serve as the foundation for a CircleCI command-line client as well.

Contribution is _always_ appreciated. Make a pull request and help out!