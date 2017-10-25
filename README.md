# mutil - Music Utilities

**mutil** is a command-line program to manage your music collection--or so the legend says...

## Usage
Start the program with `python -m mutil.api` and supply standard help arguments: `-h` or `--help`

## FAQ
> Does it work?

Yes, the tests lie.

> Why not design it so tests don't rely on implementation?

Program was never supposed to use an argument list for passing around arguments.

> It's overly convoluted.

That's not a question! Although the original goal was to have a scalable design (which I partly succeeded in) and thus mutil was never intended to be simple relative to it's size and feature-set, it did turn out rather more obscure then what I intended. But I suppose that's why you call it a hack. Right? right???.. 

> Why did you do it that way? I uh eh kind of..

Next time I should consider the implications of not eh uhhee doing anything upfront.

> Why'd you give up now? Tests are failing!

It'll probably take more time to fix it than rewrite it. but ye' know you can still use it to dedupe your playlists and stuff.

> Who are you writing this for?

Well future me of course! Not you you stalker!

> What'd you learn?

In no particular order

* Some stuff with decorators
* Indirection in practice
* Testing
  * Test fixtures
  * Test-driven-development for noobs
  * Test parametrization
* Git branching workflow
* Closures in practice
* Lambda functions
* Python's import system, specifically relative imports
* Passing function identifiers a la functional programming---hire me Church!
* Something something coupling
* How to ignore lint warnings
* *and that's just the things implemented in **this** project!*
