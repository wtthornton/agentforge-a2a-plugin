from agentforge_a2a.agents.caller_agent import CallerRunner
from agentforge_a2a.agents.callee_agent import CalleeRunner


def test_caller_prefixes():
    assert CallerRunner().run("hello") == "called->hello"


def test_callee_uppercases():
    assert CalleeRunner().run("hello") == "HELLO"


def test_runners_are_deterministic():
    c = CallerRunner()
    assert c.run("x") == c.run("x") == "called->x"
    e = CalleeRunner()
    assert e.run("abc") == e.run("abc") == "ABC"
