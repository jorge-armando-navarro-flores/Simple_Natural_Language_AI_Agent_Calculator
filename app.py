from agents import Chain

chain = Chain()


def set_api_key(api_key):
    chain.set_chain(api_key)


def response(message):
    return chain.get_chain().invoke(message)
