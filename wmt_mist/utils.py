def get_language_name(code: str) -> str:
    # import here to avoid importing by default
    import iso639

    # TODO: drops variation as cs_CZ -> cs
    code = code.lower().split("_")[0]

    return iso639.to_name(code)
