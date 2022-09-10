import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    pass

@pytest.fixture(scope="module")
def uni(unidirectional, accounts):
    return unidirectional.deploy(accounts[1], {'from':accounts[0], 'value':'10 ether'})