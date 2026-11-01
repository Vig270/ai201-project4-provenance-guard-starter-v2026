"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": [
            "Cosmos uses a consensus mechanism called Tendermint Core. The tendermint core is a proof-of-stake variant that provides BFT and instant finality.",

            "This project is an independent study focused on designing and building a secure, database backed banking application from scratch.",

            "Modern telecom networks experience complex failures such as fiber cuts, overloads and cascading outages.",

            "One of the most impactful uses of AI in retail and e-commerce is customer purchase prediction.",

            "The purpose of this project is to find and compare different neural network for image classification using the MNIST dataset of handwritten digits.",

            "In this project, this is to build a predictive model for the COVID-19 positive cases in ML.",

            "By editing the php in the terminal, you can change the user's name to gain full admin.",

            "No, it is not correct to say AI is about developing human-like agents because AI focuses on rational agents that select actions to maximize expected utility, regardless of whether they mimic humans.",

            "It is possible to build a search system with perfect recall by returning all docs of each query. This way, all relevant docs are included.",

            "Where the double dash comments out rest of the query and limiting to only updating Alice’s password. With that, Alice’s new password is dog and therefore bypassed it.",
        ],
    },

    {
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            "The implementation of an effective information system requires careful consideration of its underlying architecture, data management processes, and operational requirements. Furthermore, organizations must evaluate system performance to ensure that technological solutions align with their strategic objectives.",

            "I worked on several projects during college, and each one taught me something different. Some were frustrating at first, especially when my code did not work, but I learned to break problems into smaller steps and figure things out as I went.",

            "Technology has changed the way people communicate and work. Although these changes have created many opportunities, they have also introduced challenges that organizations must consider when adopting new systems.",
        ],
    },

]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
