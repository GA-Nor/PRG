def process_record(record):
    try:
        parts = record.split(",")
        name = parts[0].strip().title()
        login_count = int(parts[1])
    except IndexError:
        return "ERROR: Missing login count"
    except ValueError:
        return "ERROR: Login count must be numeric"

    return name, login_count
