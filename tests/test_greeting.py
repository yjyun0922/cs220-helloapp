GREETING = b"Hello"
APPNAME = GREETING + b"App"

def test_index(client):
    """ 
    Test that we can get the index for the app 
    """

    rv = client.get("/")

    # Not an exhaustive test, but if the app returns
    # something with the app name in it and a <form> in it, 
    # we're probably ok.
    assert APPNAME in rv.data
    assert b"<form" in rv.data
    assert b"</form>" in rv.data


def test_greeting(client):
    """ 
    Test that we get the correct greeting 
    if we submit the form.
    """
 
    name = b"Random J. Hacker"
    greeting = GREETING + b", " + name + b"!"

    rv = client.post("/", data={"name": name})

    # Test that the resulting page contains the app name
    # and the correct greeting.
    assert APPNAME in rv.data
    assert greeting in rv.data


