from ai.scoring.skills_score import compute

def test_scoring():

    score = compute(

        ["Python","Docker"],

        ["Python","Docker","FastAPI"]

    )

    assert score > 60