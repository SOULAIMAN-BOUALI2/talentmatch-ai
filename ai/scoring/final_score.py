def compute(
    semantic,
    skills,
    experience,
    education,
    languages
):

    return (

        semantic * 0.40 +

        skills * 0.30 +

        experience * 0.15 +

        education * 0.10 +

        languages * 0.05

    )