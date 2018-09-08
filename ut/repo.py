from ut import default


owners = default.get("conf.json").owners
helper = default.get("conf.json").helpers

# owner is a thottie
def is_owner(ctx):
    return ctx.author.id in owners

# helper is a daddy
def is_helper(ctx):
    return ctx.author.id in helper
