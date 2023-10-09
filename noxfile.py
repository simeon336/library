import nox

@nox.session

def unit_tests(session):
    session.run("echo", "Bruuh")